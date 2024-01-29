from enum import Enum
from .base import HexMemoryAddress


class GameStateAddress(Enum):
    BATTLE_TYPE = HexMemoryAddress(0xD057, 1)