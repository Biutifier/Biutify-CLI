import ast
from Biutify.NodeListener import Visitor
import Biutify.NodeHandler.Literals as literals
from ruamel.yaml import YAML
import os

yaml = YAML(typ = 'safe')
config = None
with open(os.path.join('config_example.yaml')) as f:
  config = yaml.load(f)


test_str = """if a > b:
  print(a)
else:
  if (b > c):
    print(c)
  else:
    if a: a = [1, 2, 3, 4, 5]"""

print('ORIGINAL:\n' + test_str)
print()
print('REBUILT:\n' + Visitor().rebuild(ast.parse(test_str), config))


