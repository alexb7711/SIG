"""!@file var_str.py"""

from SIG.topic_generator.data.data_types.variables import Variable
from SIG.topic_generator.data.data_types.variables import VariableTypes


class VarStr(Variable):
    """!
    Defines the allowed parameters for an string.

    @param name String defining the name of the string
    @param string Text string
    @param description Description of the variable
    """

    ####################################################################################################################
    # PUBLIC
    ####################################################################################################################

    ##==================================================================================================================
    #
    def __init__(self, data: dict):
        # Initialize the Variable object
        Variable.__init__(self, data, str, "")

        return
