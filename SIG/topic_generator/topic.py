"""!@file topic.py

This module is a data class that stores the metadata for each topic file found in the project.
The metadata includes information such as:

- Name of the topic
- Required language output
- Data types that are in the message
- Amount of messages that are allowed to be queued
- Rate of transmission of the message
- Description of the message
"""

from dataclasses import dataclass
from typing import TextIO, Self
from SIG.topic_generator.data.data_types.variables import Variable
from SIG.topic_generator.data.data_types.variables import VariableTypes
from SIG.utility.exception_handler import print_exception_warning

from SIG.topic_generator.data.data_types.var_bool import VarBool
from SIG.topic_generator.data.data_types.var_int import VarInt
from SIG.topic_generator.data.data_types.var_float import VarFloat
from SIG.topic_generator.data.data_types.var_str import VarStr


@dataclass
class Topic:
    """!
    Defines the allowed parameters for a topic object.

    @param name String defining the name of the topic
    @param lang String specifying the output language(s)
    @param data Defines the set of data types and data structures in the
           topic
    @param queue_size Number of elements that may be buffered (Optional)
    @param rate Rate of published data. (Optional)
    @param description Description of the topic (Optional)
    """

    ####################################################################################################################
    # PUBLIC
    ####################################################################################################################

    # ==================================================================================================================
    # Data
    name: str
    lang: list[str]
    protocol: str
    data: list[dict]
    queue_size: int
    rate: float
    desc: str

    # ==================================================================================================================
    #
    def format_data(yml: TextIO) -> Self:
        """!
        Extracts the data from a YAML file and formats it in a data class.

        @param: yml File handle to the topic YAML file.

        @return
        Data class containing the allowed parameters for topics.
        """

        # Default values
        queue_size = 1
        lang = ["python", "c", "rust"]
        rate = None
        data = []
        protocol = ""
        lang = []
        desc = ""
        name = ""

        # Required fields
        try:
            name = yml["name"]
            protocol = yml["protocol"]
            data = Topic._verify_and_extract_data(yml["data"])
        except Exception:
            raise

        # Optional fields
        if yml.get("queue_size"):
            queue_size = yml["queue_size"]
        if yml.get("rate"):
            rate = yml["rate"]
        if yml.get("desc"):
            desc = yml["desc"]
        if yml.get("lang"):
            lang = list(map(lambda x: x.lower(), yml["lang"]))

        # Create the Topic and return it
        return Topic(name, lang, protocol, data, queue_size, rate, desc)

    ####################################################################################################################
    # PRIVATE
    ####################################################################################################################

    # ==================================================================================================================
    #
    def _verify_and_extract_data(data: list[dict]) -> list[dict]:
        """! @brief Verifies the data field and formats the information into list of dictionaries

        @param data

        @returns
        """

        # Create emtpy dictionaries of found variables
        variables: dict = {}

        # Iterate through each variable type in the topic
        for type, vars in data.items():
            ## Iterate through each variable of the given type
            for v in vars:
                ### Determine the variable type and create the object
                try:
                    #### If the data type exists, add or append to the dictionary of variables
                    # TODO: Need to update each type to Topic._app_or_append(type, Type(v), variables)
                    #       to create a data object of the type `type`.
                    if type == VariableTypes.bool:
                        variables = Topic._add_or_append(type, VarBool(v), variables)
                    elif type == VariableTypes.int:
                        variables = Topic._add_or_append(type, VarInt(v), variables)
                    elif type == VariableTypes.float:
                        variables = Topic._add_or_append(type, VarFloat(v), variables)
                    elif type == VariableTypes.str:
                        variables = Topic._add_or_append(type, VarStr(v), variables)
                    # Otherwise the data type does not exist
                    else:
                        print_exception_warning(
                            "", f"DID NOT FIND THE VARIABLE {type}", None
                        )
                except Exception as e:
                    print_exception_warning(e, f"\nUNABLE TO FORMAT {type}", None)

        return variables

    # ==================================================================================================================
    #
    def _add_or_append(type: VariableTypes, v: dict, d: dict) -> dict:
        """! @brief Either create the entry or append to the list in the dictionary.

        @param type
        @param v
        @param d

        @returns
        """
        # If the key exists in the dictionary
        if type in d:
            d[type].append(v)
        # Otherwise the key does not exist in the dictionary
        else:
            d.update({type: [v]})

        return d
