"""! @file variables.py"""

from dataclasses import dataclass


##======================================================================================================================
#
class Variable:
    """! @brief TODO"""

    ####################################################################################################################
    # PUBLIC
    ####################################################################################################################

    ##==================================================================================================================
    # Static Variables
    types: list[str] = []

    ##==================================================================================================================
    #
    def __init__(self, data: dict):
        # Define class variables

        self.name: str
        self.desc: str
        self._data: dict = data
        return

    ##==================================================================================================================
    #
    def populate(self) -> None:
        """! @brief Populate the name and description of the variable."""

        try:
            # Try to populate the variable name
            self.name = self._data["name"]
            self.desc = self._data["desc"]

            # Try to populate the variable description
            # if any("desc" in data)
        except Exception:
            raise

        return None

    ####################################################################################################################
    # PRIVATE
    ####################################################################################################################


##======================================================================================================================
#
@dataclass
class VariableTypes:
    """! @brief Dataclass to standardize the formatting of the variable types."""

    bool: str = "bool"
    int: str = "int"
    float: str = "float"
    str: str = "string"
