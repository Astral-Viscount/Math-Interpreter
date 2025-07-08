from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    NUMBER          = 0
    PLUS            = 1
    MINUS           = 2
    MULTIPLICATION  = 3
    DIVISION        = 4
    L_PAREN         = 5
    R_PAREN         = 6
    POWER           = 7
    SQ_RT           = 8   

@dataclass
class Token:
    type: TokenType
    value: any = None

    # If we print out a token this will print it out in a nice format
    # So this prints out the token value if it has a value
    def __repr__(self):
        return self.type.name + (f": {self.value}" if self.value != None else "")

