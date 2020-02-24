# import cli.file_tree
# import cli.node

grouping_chars = [
  ('(', ')'),
  ('[', ']'),
  ('{', '}')
]

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