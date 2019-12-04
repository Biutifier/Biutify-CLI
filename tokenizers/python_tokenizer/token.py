from enum import Enum

class TokenType(Enum):

    NONE = 0
    NEWLINE = 1
    INDENT = 2
    DEDENT = 3
    IDENTIFIER = 4
    KEYWORD = 5
    LITERAL = 6
    OPERATOR = 7
    DELIMITER = 8


class Token:

    token_type = TokenType.NONE


# https://docs.python.org/3/reference/lexical_analysis.html


'''

ORDER

find literals (strings mostly)

find groups

find operators

find variables


'''