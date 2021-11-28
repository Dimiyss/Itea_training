from enum import Enum
from typing import TypedDict, Any

MAX_ATTEMPT = 3
DEFAULT_HEADER_SIZE = 10
DEFAULT_PACK_SIZE = 5
DEFAULT_ENCODING = '866'
IP = 'localhost'
PORT = 1234
MAX_QUEUE = 1


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
