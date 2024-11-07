"""! @file variables.py"""

from typing import Any

from dataclasses import dataclass

##======================================================================================================================
#
@dataclass
class VariableTypes:
    """! @brief Dataclass to standardize the formatting of the variable types."""
    bool: str = "bool"
    int: str = "int"
    float: str = "float"
    str: str = "string"


##======================================================================================================================
#
class Variable:
    """! @brief Class to verify the data provided is complete and consistent."""

    ####################################################################################################################
    # PUBLIC
    ####################################################################################################################

    ##==================================================================================================================
    # Static Variables
    types: list[str] = [] #!< Track the types of variables found in the current topic

    ##==================================================================================================================
    #
    def __init__(self, data: dict, t: type):
        # Define class variables
        self.name: str
        self.desc: str
        self._data: Any = data
        self._type: type = t

        return

    ##==================================================================================================================
    #
    def populate(self, vb: str, default: Any):
        """! @brief Populate the name and description of the variable."""

        # Ensure the data is the correct type
        if not isinstance(self._data["value"], self._type):
            raise Exception("THE PROVIDED DATA IS NOT OF TYPE: BOOL")

        # Try to populate the variable data
        try:
            ## Required data
            self.name = self._data["name"]

            ## Optional Data
            self._data = self._data.get("value", default):
            self.desc = self._data.get("desc"):

        except Exception:
            raise

        # Subscribe the current data type to `Variable`
        if vb not in Variable.types:
            Variable.types.append(vb)

        return

    ##==================================================================================================================
    #
    def get_data(self) -> Any:
        """! @brief Return a copy of the variable data."""
        return self._data.copy()

    ##==================================================================================================================
    #
    def get_type(self) -> str:
        """! @brief Return a copy of the type of data as a string"""
        return self._type.copy()

    ####################################################################################################################
    # PRIVATE
    ####################################################################################################################
