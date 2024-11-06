"""!@file var_float.py"""

from SIG.topic_generator.generators.data.data_types.variables import Variable
from SIG.topic_generator.generators.data.data_types.variables import VariableTypes


class VarInt(Variable):
    """!
    Defines the allowed parameters for an integer.

    @param name String defining the name of the integer
    @param value Integer value of the variable
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
        if VariableTypes.int not in Variable.types:
            Variable.types.append(VariableTypes.int)

        # Populate the name and description
        self.populate()

        # Populate the data
        self.value: int = data["value"]

        return
