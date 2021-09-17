# -*- coding: utf-8 -*-
__all__ = ["BaseRegistryEnum"]

from typing import Any
from enum import Enum, EnumMeta


class _RegistryMetaEnum(EnumMeta):
    def __contains__(self, item):
        return any(x.value == item for x in self)


class BaseRegistryEnum(Enum, metaclass=_RegistryMetaEnum):
    """Creates registry enums.

    Parameters
    ----------
    value: str
        String value of the enum
    description: str
        String description of what the enum represents
    instance: Any
        Instance of the enum
    """

    def __init__(self, value: str, description: str, instance: Any = None):
        self._value_: str = value
        self.description: str = description
        self.instance = instance

    def __iter__(self):
        """Generator for iterating over an enum values

        Returns
        -------
        Generator
            Yields values of enum in value, instance, description order.
        """
        yield self.value
        if self.instance is not None:
            yield self.instance
        yield self.description

    def __str__(self):
        """Returns string value of enum.

        Returns
        -------
        str
            String version of enum
        """
        return self.value
