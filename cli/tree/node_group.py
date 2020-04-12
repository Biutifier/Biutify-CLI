from typing import List
from tree.node import Node
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


  @classmethod
  def create_from_char(cls, start_char: str):
    """
    Create a NodeGroup based on a starting character, e.g. '(', '{', or '['.

    Parameters
    ----------
    start_char : str
      The character to base the GroupType on
    """

    if start_char == '(': return NodeGroup(NodeGroup.GroupType.PAREN)
    if start_char == '[': return NodeGroup(NodeGroup.GroupType.BRACKET)
    if start_char == '{': return NodeGroup(NodeGroup.GroupType.CURLY)
    return None

  
  def __init__(self, type: GroupType, parent: Node = None, children: List[Node] = None):
    super().__init__(parent, children)
    self.type = type


  def __str__(self):
    result = "NODE GROUP\nType: " + str(self.type) + "\n"
    print(self.children)
    for child in self.children:
      child_str = str(child)
      for line in child_str.split('\n'):
        result += "\n    " + line
    return result + '--------------- GROUP ' + str(self.type) + '\n'
  