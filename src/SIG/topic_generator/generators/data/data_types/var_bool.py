"""!@file var_bool.py"""

from dataclasses import dataclass

from variables import Variable


@dataclass
class VarBool(Variable):
    """!
    Defines the allowed parameters for an boolean.

    @param name String defining the name of the boolean
    @param value boolean value of the variable
    @param description Description of the variable
    """

    name: str
    value: bool
    desc: str
