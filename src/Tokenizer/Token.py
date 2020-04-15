from enum import Enum

class TokenType:

  class Operator:
    class Parse(Enum):
      BEFORE = 0
      AFTER = 1
      BEFORE_AND_AFTER = 2
      STATEMENT = 3

    def __init__(self, symbol, priority, parse = Parse.BEFORE_AND_AFTER):
      self.symbol = symbol
      self.priority = priority
      self.parse = parse

  class AmbiguousOperator:
    def __init__(self, symbol):
      self.symbol = symbol

  operators = [
    [
      Operator('=', 0),
      Operator(':=', 0)
    ],
    [
      Operator('or', 3)
    ],
    [
      Operator('and', 4)
    ],
    [
      Operator('not', 5)
    ],
    [
      Operator('in', 6),
      Operator('not  in', 6),
      Operator('is not', 6),
      Operator('is', 6),
      Operator('<', 6),
      Operator('<=', 6),
      Operator('>', 6),
      Operator('>=', 6),
      Operator('!=', 6),
      Operator('==', 6)
    ],
    [
      Operator('|', 7)
    ],
    [
      Operator('^', 8)
    ],
    [
      Operator('&', 9)
    ],
    [
      Operator('<<', 10),
      Operator('>>', 10)
    ],
    [
      Operator('+', 11),
      Operator('-', 11)
    ],
    [
      Operator('*', 12),
      Operator('@', 12),
      Operator('//', 12),
      Operator('/', 12),
      Operator('%', 12)
    ],
    [
      Operator('+', 13, Operator.Parse.AFTER),
      Operator('-', 13, Operator.Parse.AFTER),
      Operator('~', 13, Operator.Parse.AFTER)
    ],
    [
      Operator('**', 14)
    ],
    [
      Operator('await', 14, Operator.Parse.AFTER)
    ]
  ]

class Token:


  def __init__(self, token_type, raw_text):
    self.type = token_type
    self.raw_text = raw_text