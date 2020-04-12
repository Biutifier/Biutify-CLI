from typing import List
from .Node import Node

class NodeRawCode(Node):
  """
  A Node containing raw code.

  Parameters
  ----------
  code : str
    The raw code.
  parent : Node, optional
    The parent of this Node.
    Default is None, which implies this to be a root Node.
  children : List[Node], optional
    The children of this Node.
    Default is empty.

  Attributes
  ----------
  code : str
    The raw code.
  """


  def __init__(self, code : str, parent: Node = None, children: List[Node] = None):
    super().__init__(parent, children)
    self.code = code


  def __str__(self):
    result = "NODE RAW CODE\nCode: " + self.code + "\n----------"
    for child in self.children:
      child_str = str(child)
      for line in child_str.split('\n'):
        result += "\n    " + line
    return result + '--------------- RAW\n'