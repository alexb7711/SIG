"""!@file var_str.py"""

from dataclasses import dataclass


@dataclass
class VarStr:
    """!
    Defines the allowed parameters for an string.

    @param name String defining the name of the string
    @param string Text string
    @param description Description of the variable
    """

    name: str
    string: str
    desc: str
