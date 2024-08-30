"""!@file publisher.py"""

from dataclasses import dataclass
from typing import TextIO, Self


@dataclass
class Publisher:
    """!
    Defines the allowed parameters for a publisher object.

    @param name String defining the name of the publisher
    @param lang String specifying the output language(s)
    @param data Defines the set of data types and data structures in the
           publisher
    @param queue_size Number of elements that may be buffered (Optional)
    @param rate Rate of published data. (Optional)
    @param description Description of the publisher (Optional)
    """

    # ==========================================================================
    # Data
    name: str
    lang: str
    publish: dict
    queue_size: int
    rate: float
    desc: str

    # ==========================================================================
    # Helper methods
    def format_data(yml: TextIO) -> Self:
        """!
        Extracts the data from a YAML file and formats it in a data class.

        @param: yml File handle to the publisher YAML file.

        @return
        Data class containing the allowed parameters for publishers.
        """

        # Extract the data

        # Default values
        Publisher.queue_size = 1
        Publisher.lang = "python"

        # Required fields
        Publisher.name = yml["name"]
        Publisher.publish = yml["publish"]

        # Optional field
        if yml.get("queue_size"):
            Publisher.rate = yml["queue_size"]
        if yml.get("rate"):
            Publisher.rate = yml["rate"]
        if yml.get("desc"):
            Publisher.desc = yml["desc"]

        return Publisher
