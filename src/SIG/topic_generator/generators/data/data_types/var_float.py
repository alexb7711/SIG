"""!@file var_float.py"""

from src.SIG.topic_generator.generators.data.data_types.variables import Variable
from src.SIG.topic_generator.generators.data.data_types.variables import VariableTypes


class VarFloat(Variable):
    """!
    Defines the allowed parameters for an float.

    @param name String defining the name of the float
    @param value float value of the variable
    @param description Description of the variable
    """

    ##==================================================================================================================
    #
    def __init__(self, data: dict):
        # Initialize variable
        Variable.__init__(self, data)

        # Subscribe to the current data type to `Variable`
        if VariableTypes.float not in Variable.types:
            Variable.types.append(VariableTypes.float)

        # Populate the name and description
        self.populate()

        # Populate the data
        self.value = data["value"]

        return
