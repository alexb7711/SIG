"""!@file var_bool.py"""

from src.SIG.topic_generator.generators.data.data_types.variables import Variable
from src.SIG.topic_generator.generators.data.data_types.variables import VariableTypes


class VarBool(Variable):
    """!
    Defines the allowed parameters for an boolean.

    @param name String defining the name of the boolean
    @param value boolean value of the variable
    @param description Description of the variable
    """

    ####################################################################################################################
    # PUBLIC
    ####################################################################################################################

    ##==================================================================================================================
    #
    def __init__(self, data: dict):
        # Initialize variable
        Variable.__init__(self, data)

        # Subscribe to the current data type to `Variable`
        if VariableTypes.bool not in Variable.types:
            Variable.types.append(VariableTypes.bool)

        # Populate the name and description
        self.populate()

        # TODO: Add check to ensure the data is either:
        # - 0 or 1
        # - True or False

        # Populate the data
        self.value: bool = data["value"]

        return
