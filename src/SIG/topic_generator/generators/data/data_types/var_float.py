"""!@file var_float.py"""

from dataclasses import dataclass

from variables import Variable


@dataclass
class VarFloat(Variable):
    """!
    Defines the allowed parameters for an float.

    @param name String defining the name of the float
    @param value float value of the variable
    @param description Description of the variable
    """

    name: str
    value: float
    desc: str
