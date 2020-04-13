from typing import List
from .Node import Node
from enum import Enum
import re

class NodeOperator(Node):
  """
  A Node describing an operator.

  Extended Summary
  ----------------
  Python operators can be found at https://docs.python.org/3/library/operator.html.
  This implimentation may not include all operators listed due to the structure and purpose of our project.

  Parameters
  ----------
  type : OperatorType
    The type of operator this node represents.
  parent : Node, optional
    The parent of this Node.
    Default is None, which implies this to be a root Node.
  children : List[Node], optional
    The children of this Node.
    Default is empty.

  Attributes
  ----------
  type : FlowControllerType
    The type of operator this node represents.
  """

  class OperatorType(Enum):
    """
    A type of operator.

    Attributes
    ----------
    ADDITION: str
      Addition operator (a + b).
    CONTAINMENT: str
      Containment test operator (a in b).
    DIVISION
      Standard division operator (a / b).
    FLOOR_DIVISION
      Flooring (integer) division operator (a // b).
    BITWISE_AND
      Bitwise 'and' operator (a & b).
    BITWISE_XOR
      Bitwise 'exclusive or' operator (a ^ b).
    BITWISE_INVERSION
      Bitwise inversion operator (~ a).
    BITWISE_OR
      Bitwise 'or' operator (a | b).
    EXPONENTIATION
      Exponentiation operator (a ** b).
    IDENTITY_FALSE
      False identity operator (a is not b).
    IDENTITY_TRUE
      True identity operator (a is b).
    LEFT_SHIFT
      Bitwise left shift operator (a << b).
    MODULO
      Modulo operator (a % b).
    MULTIPLICATION
      Multiplication operator (a * b).
    MATRIX_MULTIPLICATION
      Matrix multiplication operator (a @ b).
    ARITHMETIC_NEGATION
      Arithmetic negation operator (- a).
    LOGICAL_NEGATION
      Logical negation operator (not a).
    POSITIVE
      Positive operator (+ a).
    RIGHT_SHIFT
      Bitwise right shift operator (a >> b).
    DELETION
      Deletion operator (del a).
    SLICE
      Slicing operator (a : b)
    SUBTRACTION
      Subtraction operator (a << b).
    LESS_THAN
      Logical less-than operator (a < b).
    LESS_THAN_OR_EQUAL
      Logical less-than-or-equal-to operator (a <= b).
    GREATER_THAN
      Logical greater-than operator (a > b).
    GREATER_THAN_OR_EQUAL
      Logical greater-than-or-equal-to operator (a >= b).
    EQUALITY
      Equality operator (a == b).
    DIFFERENCE
      Difference operator (a != b).
    IN_PLACE_ADDITION
      In-place addition operator (a += b).
    IN_PLACE_BITWISE_AND
      In-place bitwise 'and' operator (a &= b).
    IN_PLACE_BITWISE_FLOOR_DIVISION
      In-place flooring (integer) division operator (a //= b).
    IN_PLACE_LEFT_SHIFT
      In-place bitwise left shift operator (a <<= b).
    IN_PLACE_MODULO_OPERATOR
      In-place modulo operator (a %= b).
    IN_PLACE_MULTIPLICATION
      In-place multiplication operator (a *= b).
    IN_PLACE_MATRIX_MULTIPLICATION
      In-place matrix multiplication operator (a @= b).
    IN_PLACE_BITWISE_OR
      In-place bitwise 'or' operator (a |= b).
    IN_PLACE_EXPONENTIATION
      In-place exponentiation operator (a **= b).
    IN_PLACE_RIGHT_SHIFT
      In-place bitwise right shift operator (a >>= b).
    IN_PLACE_SUBTRACTION
      In-place subtraction operator (a -= b).
    IN_PLACE_DIVISION
      In-place standard division operator (a /= b).
    IN_PLACE_BITWISE_XOR
      In-place bitwise 'xor' operator (a ^= b).
    
    """


  # @classmethod
  # def create_from_char(cls, start_char: str):
  #   """
  #   Create a NodeGroup based on a starting character, e.g. '(', '{', or '['.

  #   Parameters
  #   ----------
  #   start_char : str
  #     The character to base the GroupType on
  #   """

  #   if start_char == '(': return NodeGroup(NodeGroup.GroupType.PAREN)
  #   if start_char == '[': return NodeGroup(NodeGroup.GroupType.BRACKET)
  #   if start_char == '{': return NodeGroup(NodeGroup.GroupType.CURLY)
  #   return None

  
  # def __init__(self, type: GroupType, parent: Node = None, children: List[Node] = None):
  #   super().__init__(parent, children)
  #   self.type = type


  # def __str__(self):
  #   result = "\nNODE GROUP\nType: " + str(self.type) + "\n"
  #   print(self.children)
  #   for child in self.children:
  #     child_str = str(child)
  #     for line in child_str.split('\n'):
  #       result += "\n|   " + line
  #   return result
  