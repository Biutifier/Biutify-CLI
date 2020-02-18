# import cli.file_tree
# import cli.node

def tokenize(file_path: str):

  with open(file_path, 'r') as file:
    raw_text = file.read()
    for index in range(len(raw_text)):

      # check for grouping character
      pass


tokenize('/home/zachchampion/Documents/work.txt')