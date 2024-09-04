"""!@file var_str.py"""

from dataclasses import dataclass

from variables import Variable


@dataclass
class VarStr(Variable):
    """!
    Defines the allowed parameters for an string.

    @param name String defining the name of the string
    @param string Text string
    @param description Description of the variable
    """

    name: str
    string: str
    desc: str
