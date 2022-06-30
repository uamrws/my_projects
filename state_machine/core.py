# -*- coding: utf-8 -*-
import enum
import logging
from dataclasses import asdict

from transitions.extensions import HierarchicalMachine
from transitions.extensions.nesting import NestedState

from common.state_machine.standard import (
    STANDARD_SEPARATOR,
    NestedStates,
    NestedString,
    Trans,
)

# flake8: noqa B902

HierarchicalMachine.state_cls.separator = (
    HierarchicalMachine.separator
) = STANDARD_SEPARATOR
logger = logging.getLogger(__name__)


class BaseMeta(type):
    _ignore: list

    @classmethod
    def __prepare__(mcs, name, bases):
        attr_dict = enum._EnumDict()
        attr_dict._ignore = mcs._ignore
        return attr_dict

    def __new__(mcs, name, bases, attrs):
        _members_dict_ = {key: attrs.pop(key) for key in attrs._member_names}

        new = super().__new__(mcs, name, bases, attrs)
        new._members_dict_ = _members_dict_
        return new

    def __getattr__(cls, item):
        if item in cls._members_dict_:
            return item

    def __iter__(cls):
        return iter(cls.items())

    def items(cls):
        return cls._members_dict_.items()

    def values(cls):
        return cls._members_dict_.values()

    def names(cls):
        return cls._members_dict_.keys()


class BaseStatesMeta(BaseMeta):
    _ignore = ["initial_state"]

    def __getattr__(cls, item):
        if item in cls._members_dict_:
            nested_states = cls._members_dict_[item]
            if isinstance(nested_states, (str, tuple)):
                return NestedString(super().__getattr__(item), None)
            else:
                assert isinstance(nested_states, NestedStates)
                return NestedString(item, nested_states.children.states)


class BaseTransactionsMeta(BaseMeta):
    _ignore = ["trigger_method"]


class BaseStates(metaclass=BaseStatesMeta):
    initial_state: str


class BaseTransactions(metaclass=BaseTransactionsMeta):
    trigger_method: str


class ComponentMeta(type):
    @staticmethod
    def load_transactions(machine, transitions):
        trigger_method = transitions.trigger_method
        for item in transitions:
            trigger, tran = item
            assert isinstance(tran, Trans)
            tans_dict = asdict(tran)
            machine.add_transition(trigger_method, **tans_dict)

    @staticmethod
    def load_states(machine, states):
        for state in states:
            kwargs = {}
            name, val = state
            kwargs["name"] = name

            if isinstance(val, NestedStates):
                kwargs.update(asdict(val))
                val = kwargs.pop("verbose", None)
            kwargs["value"] = val
            machine.add_state(kwargs)

        machine.initial = states.initial_state


class BaseNestedState(NestedState):
    def __init__(self, *args, **kwargs):
        self._value = kwargs.pop("value")
        super().__init__(*args, **kwargs)

    @property
    def value(self):
        return self._value


HierarchicalMachine.state_cls = BaseNestedState


class BaseComponent(metaclass=ComponentMeta):
    model_attribute = None

    def __new__(cls, states, transitions) -> HierarchicalMachine:
        """

        :param states:
        :param transitions:
        """
        machine = HierarchicalMachine(
            model=None,
            auto_transitions=False,
            model_attribute=cls.model_attribute,
            initial=None,
        )
        cls.load_states(machine, states)
        cls.load_transactions(machine, transitions)
        return machine


class StateNotChangeError(Exception):
    def __init__(self, message=None):
        message = message or "状态未变更成功"
        super().__init__(message)


class BaseMachine:
    _machine = None
    _model_proxy = None

    def __init__(self, model, save=True, skip_check_state=False):
        self.model = self._model_proxy(model)
        self._save = save
        self.skip_check_state = skip_check_state

    def __enter__(self):
        self._machine.add_model(self.model, initial=self.model.state)
        return self.model

    def check_state(self):
        """校验状态是否变更"""
        return self.model.state == self.model.pre_state

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._machine.remove_model(self.model)
        if exc_value:
            raise
        if not self.skip_check_state and self.check_state():
            raise StateNotChangeError()
        if self._save:
            self.model.save()

    @classmethod
    def get_state(cls, state):
        return cls._machine.get_state(state)

    @classmethod
    def get_states(cls, prefix="", states=None):
        result = []
        if not states:
            states = cls._machine.states

        for state in states.values():
            if state.states:
                if prefix:
                    result.extend(
                        cls.get_states(
                            prefix + STANDARD_SEPARATOR + state.name, state.states
                        )
                    )
                else:
                    result.extend(cls.get_states(state.name, state.states))
            else:
                if prefix:
                    result.append(
                        [prefix + STANDARD_SEPARATOR + state.name, state.value]
                    )
                else:
                    result.append([state.name, state.value])

        return result
