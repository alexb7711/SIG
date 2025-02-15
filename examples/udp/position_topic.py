#!/bin/python

import socket, json, sys

from dataclasses import dataclass

BUFSIZE = 65535
interface = "0.0.0.0"
port = 1060


@dataclass
class Position:
    """Class for keeping track of the (x,y) position of an item."""

    x: float
    y: float

    @classmethod
    def from_dict(cls, data):
        return cls(x=data.get("x"), y=data.get("y"))


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((interface, port))

print("Listening for datagrams at {}".format(sock.getsockname()))

while True:
    data, address = sock.recvfrom(sys.getsizeof(Position))
    print(type(data))
    json_data = json.loads(data.decode("utf-8"))
    p = Position.from_dict(json_data)

    print(f"The client at {address} transmitted the position {p}")
    # print("The client at {} says: {!r}".format(address, text))
