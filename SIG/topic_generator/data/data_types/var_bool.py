"""!@file var_bool.py"""

from src.SIG.topic_generator.generators.data.data_types.variables import Variable
from src.SIG.topic_generator.generators.data.data_types.variables import VariableTypes


##======================================================================================================================
#
class VarBool(Variable):
    """!
    Defines the allowed parameters for an boolean.

    @param name String defining the name of the boolean
    @param value boolean value of the variable
    @param description Description of the variable
    """

    ##=================================================================================================================
    #
    def __init__(self, data: dict):
        Variable.__init__(self, data, bool, VariableTypes.bool)
        return
