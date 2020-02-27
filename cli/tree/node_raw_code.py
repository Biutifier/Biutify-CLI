from typing import List
from node import Node

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


  def __init__(self, code : str, parent: Node = None, children: List[Node] = []):
    super().__init__(parent, children)
    self.code = code