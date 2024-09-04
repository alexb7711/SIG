"""!@file var_float.py"""

from dataclasses import dataclass

from variables import Variable


@dataclass
class VarInt(Variable):
    """!
    Defines the allowed parameters for an integer.

    @param name String defining the name of the integer
    @param value Integer value of the variable
    @param description Description of the variable
    """

    name: str
    value: int
    desc: str
