from .Tokenizer.Tokenizer import create_groups
import os

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.txt'), 'r') as f:
  print(str(create_groups(f.read())[0]))
  # create_groups(f.read())