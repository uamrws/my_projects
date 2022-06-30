# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


# pylint: disable=C0116,W0707
class BaseModelProxy(metaclass=ABCMeta):
    trigger_method = None
    state_key = None

    def __init__(self, model):
        self._order = model
        self.pre_order = model.copy()

    def __getattr__(self, item):
        try:
            return self._order[item]
        except KeyError:
            raise AttributeError

    @property
    def pre_state(self):
        return self.pre_order[self.state_key]

    @property
    def state(self):
        return self._order[self.state_key]

    @state.setter
    def state(self, value):
        self.set_attr(key=self.state_key, value=value)

    def set_attr(self, key, value):
        self._order[key] = value

    def set_attrs(self, **kwargs):
        self._order.update(kwargs)

    @abstractmethod
    def save(self):
        """保存model"""

    @abstractmethod
    def next_state(self, *args, **kwargs):
        """根据条件改变model状态"""
