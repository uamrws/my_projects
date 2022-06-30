import inspect
from dataclasses import dataclass, field
from typing import List, Union

STANDARD_SEPARATOR = ">>"


class BaseCallBack:
    def __init__(self, func):
        self.__and = True
        if isinstance(func, str):
            func = getattr(self, func)
        assert callable(func)
        self.argspec = self.check_func(func)
        self._func_ = [func]

    def __or__(self, other):
        assert isinstance(other, self.__class__)
        self.__and = False
        self._func_.append(other)
        return self.__class__(self)

    def __and__(self, other):
        assert isinstance(other, self.__class__)
        self.__and = True
        self._func_.append(other)
        return self.__class__(self)

    @classmethod
    def check_func(cls, func):
        raise NotImplementedError

    def generate_func(self, *args, **kwargs):
        for func in self._func_:
            if isinstance(func, self.__class__):
                yield func(*args, **kwargs)
            else:
                func_kwonlyargs = self.argspec.kwonlyargs
                kws = {i: kwargs[i] for i in kwargs if i in func_kwonlyargs}
                try:
                    yield func(*args, **kws)
                except (TypeError, AssertionError):
                    yield False

    def __call__(self, order, **kwargs):
        if self.__and:
            return all(self.generate_func(order, **kwargs))
        else:
            return any(self.generate_func(order, **kwargs))


class OrderCallBack(BaseCallBack):
    @classmethod
    def check_func(cls, func):
        if isinstance(func, cls):
            return
        argspec = inspect.getfullargspec(func)
        func_args = argspec.args
        assert len(func_args) == 1 and "order" in func_args, (
            f"func '{func.__name__}({', '.join(func_args)})'"
            f" can only set one arguments 'order'."
            f" you can defined like this: "
            f"{func.__name__}('order', '*', some_kwonlyargs)"
        )
        return argspec


class NestedString:
    def _format_(self, other):
        return self.name + STANDARD_SEPARATOR + other

    def __init__(self, name, nested_states):
        self.name = name
        self.nested_states = nested_states

    def __getattr__(self, item):
        if self.nested_states:
            try:
                return self.__class__(
                    self._format_(item), self.nested_states[item].states
                )
            except KeyError as e:
                raise AttributeError from e

    def __deepcopy__(self, memodict):
        return self.__class__(self.name, self.nested_states)


@dataclass(frozen=True)
class Trans:
    """
    source:         源状态
    dest:           目标状态
    conditions:     转换条件
    before:         转换前回调函数
    after:          转换后回调函数
    prepare:        准备转换回调函数
    """

    source: Union[NestedString, str, List[Union[NestedString, str]]]
    dest: Union[NestedString, str]
    conditions: BaseCallBack = field(default=None)
    unless: BaseCallBack = field(default=None)
    before: BaseCallBack = field(default=None)
    after: BaseCallBack = field(default=None)
    prepare: BaseCallBack = field(default=None)


@dataclass(frozen=True)
class NestedStates:
    """
    children:   下层状态
    remap:      状态重定向
    """

    children: "BaseComponent" = field(default=None)
    remap: dict = field(default=None)
    verbose: str = field(default=None)
