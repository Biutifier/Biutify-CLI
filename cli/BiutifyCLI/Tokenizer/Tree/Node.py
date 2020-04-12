from typing import List

class Node:
  """
  A node used to build a file tree.

  Parameters
  ----------
  parent : Node, optional
    The parent of this Node.
    Default is None, which implies this to be a root Node.
  children : List[Node], optional
    The children of this Node.
    Default is empty.

  Attributes
  ----------
  parent : Node
    A reference to the parent of this node.
  children : List[Nodes]
    A list of this node's child nodes.

  Methods
  -------
  is_root() -> bool
    Check if instance is a root node.
  create_child(node: Node)
    Create a child to this Node.

  """


  def __init__(self, parent = None, children = None):
    self.parent = parent
    self.children = [] if children is None else children


  def __str__(self):
    result = "\nNODE\n"
    for child in self.children:
      child_str = str(child)
      for line in child_str.split('\n'):
        result += "\n|   " + line
    return result


  def is_root(self) -> bool:
    """
    Check if instance is a root node.

    Returns
    -------
    bool
      Return true if instance is a root node, false otherwise.
    """

    return self.parent is None


  def create_child(self, node):
    """
    Create a child to this Node.

    Parameters
    ----------
    node: Node
      The new child that should be added to this Node.
    """

    self.children.append(node)
    return self.children[-1]