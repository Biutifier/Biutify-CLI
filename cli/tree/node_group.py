from typing import List
from node import Node
from enum import Enum

class NodeGroup(Node):
  """
  A Node containing a group.

  Extended Summary
  ----------------
  A group includes anything between parenthesis, brackets, or curly braces.

  Parameters
  ----------
  type : GroupType
    The type of group that this represents (paren, list, or curly).
  parent : Node, optional
    The parent of this Node.
    Default is None, which implies this to be a root Node.
  children : List[Node], optional
    The children of this Node.
    Default is empty.

  Attributes
  ----------
  type : GroupType
    The type of group that this represents (paren, list, or curly).
  """

  class GroupType(Enum):
    """
    A type of group.

    Attributes
    ----------
    PAREN : Dictionary
      A group of parenthesis.
    BRACKET : Dictionary
      A group of brackets.
    CURLY : Dictionary
      A group of curly braces.
    """

    PAREN = {
      'name'      : 'parenthesis',
      'start_char': '(',
      'end_char'  : ')'
    }
    BRACKET = {
      'name'      : 'brackets',
      'start_char': '[',
      'end_char'  : ']'
    }
    CURLY = {
      'name'      : 'curly',
      'start_char': '{',
      'end_char'  : '}'
    }

  
  def __init__(self, type: GroupType, parent: Node = None, children: List[Node] = []):
    super().__init__(parent, children)
    self.type = type
  