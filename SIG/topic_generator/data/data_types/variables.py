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
    types: list[str] = [] #!< Track the tryps of topics that are found

    ##==================================================================================================================
    #
    def __init__(self, data: dict):
        # Define class variables

        self.name: str
        self.desc: str
        self._data: Any = data
        return

    ##==================================================================================================================
    #
    def populate(self) -> None:
        """! @brief Populate the name and description of the variable."""

        # Try to populate the variable data
        try:
            self.name = self._data["name"]

            if self._data["desc"]:
                self.desc = self._data["desc"]

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
    return
