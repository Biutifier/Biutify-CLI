from tree.node import Node

class FileTree:

  """
  A tree used to parse and regenerate files.

  Parameters
  ----------
  root : Node
    The node at the root of the tree.

  Attributes
  ----------
  root : Node
    The node at the root of the tree.
    

  Methods
  """

  def __init__(self, root = Node()):
    self.root = root


  def add_node(self, node):
    """
    Add a node to the tree.

    Extended Summary
    ----------------
    Will be added as a new child of the root node.

    Parameters
    ----------
    node : Node
      The node to be added.
    """

    self.root.create_child(node)