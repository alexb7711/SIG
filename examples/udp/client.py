#!/bin/python

import socket, json
import dataclasses
from dataclasses import dataclass


@dataclass
class Position:
    """Class for keeping track of the (x,y) position of an item."""

    x: float
    y: float


# Transmit Position
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
p = Position(x=0.0, y=1.1)
sock.sendto(json.dumps(dataclasses.asdict(p)).encode("utf-8"), ("192.168.86.35", 1060))
