"""!@file var_str.py"""

from src.SIG.topic_generator.generators.data.data_types.variables import Variable
from src.SIG.topic_generator.generators.data.data_types.variables import VariableTypes


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
        # Initialize variable
        super().__init__(self, data)

        # Subscribe to the current data type to `Variable`
        if VariableTypes.str not in Variable.types:
            Variable.types.append(VariableTypes.bool)

        # Populate the name and description
        self.populate()

        # Populate the data
        self.value: str = data["value"]

        return
