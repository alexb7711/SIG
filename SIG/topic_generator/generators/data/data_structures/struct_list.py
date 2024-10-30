"""!@file var_list.py"""

from dataclasses import dataclass

from structures import Variable


@dataclass
class VarList(Variable):
    """!
    Defines the allowed parameters for a list.

    @param name String defining the name of the listean
    @param type Data type the list contains
    @param list List composed of data type `type`
    @param description Description of the variable
    """

    name: str
    type: str
    list: list
    desc: str
