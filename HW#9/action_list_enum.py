from enum import Enum
from typing import TypedDict, Any


class ActionList(Enum):
    CREATE_BOOK = 1
    CREATE_READER = 2
    GIVE_BOOK = 3
    RETURN_BOOK = 4
    PRINT_ALL_BOOK = 5
    PRINT_AVAILABLE_BOOK = 6
    PRINT_BUSY_BOOK = 7
    SORTED_BOOK = 8
    END = 9
    OK = 10


class NetworkMessage(TypedDict):
    action: ActionList
    data: Any
