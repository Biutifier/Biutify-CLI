from cli.tree.file_tree import FileTree
from cli.tree.node import Node
from cli.tree.node_group import NodeGroup
from cli.tree.node_raw_code import NodeRawCode

grouping_chars = [
  ('(', ')'),
  ('[', ']'),
  ('{', '}')
]

def create_groups(raw_code: str, root_node: Node = Node(), exit_char: str = None) -> Node:
  """
  Take raw code and extract groups.

  Extended Summary
  ----------------
  Will convert all non-group code to NodeRawCode objects.
  NodeGroups and NodeRawCodes will be added as children to root_node

  Parameters
  ----------
  raw_code : str
    The code to be grouped.
  root_node : Node, optional
    The node that will parent the generated NodeGroups and NodeRawCodes.
  exit_char : str, optional
    The character that will end the group.

  Returns
  -------
  Node
    A reference to the node that parents the generated NodeGroups and NodeRawCodes.
  int
    The length of raw_code that was used (either len(raw_code), or shorter because it found exit_char)
  """

  current_raw_code = ''
  index = 0

  while index < len(raw_code):

    # check for end of group
    if raw_code[index] == exit_char:
      return root_node, index

    # check for grouping character
    for e_grouping_char in grouping_chars:
      if raw_code[index] == e_grouping_char[0]:

        # commit current code and create group
        root_node.create_child(NodeRawCode(current_raw_code))
        group_node = root_node.create_child(NodeGroup.create_from_char(e_grouping_char[0]))
        group, group_index = tokenize(raw_code[index + 1:], group_node, e_grouping_char[1])
        index += group_index + 1
        break

    else:
      current_raw_code += raw_code[index]

      index += 1

    return root_node, index





def tokenize(raw_text: str, exit_char: str = None) -> int:

  result = []
  index = 0

  while index < len(raw_text):

    if raw_text[index] == exit_char:
      return result, index

    # check for grouping character
    print(raw_text[index])
    for e_grouping_char in grouping_chars:
      # print(raw_text[index])
      if raw_text[index] == e_grouping_char[0]:
        group = tokenize(raw_text[index + 1:], e_grouping_char[1])
        result.append(group[0])
        index += group[1] + 1
        break
    else:
      result.append(raw_text[index])

    index += 1

  return result, index



with open('cli/test.txt', 'r') as f:
  print(tokenize(f.read()))