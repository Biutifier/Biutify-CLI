from typing import List

class Node:
  """
  A node used to build a file tree.

  Attributes
  ----------
  children : List[Nodes]
    A list of this node's child nodes.
  parent : Node
    A reference to the parent of this node.

  Methods
  -------
  is_root() -> bool
    Check if instance is a root node.

  """

  children: List[Node] = []
  parent: Node = None


  def is_root(self) -> bool:
    """
    Check if instance is a root node.

    Returns
    -------
    bool
      Return true if instance is a root node, false otherwise.
    """

    return self.parent is None