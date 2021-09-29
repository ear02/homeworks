from dataclasses import dataclass
"""
create dataclass `Engine`
"""


@dataclass
class Engine:
    def __init__(self, volume, pistons):
        self.volume = volume
        self.pistons = pistons
