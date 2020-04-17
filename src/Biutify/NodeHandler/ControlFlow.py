import ast

def visit_If(visitor, node, config, indent = '', precedence = -1):
  result = 'if ' + visitor.visit(node.test, config, config['if']['indent'], precedence) + config['if']['colon']
  if len(node.body) == 1 and not config['if']['separate single line']:
    result += visitor.visit(node.body[0], config, indent, precedence)
  else:
    for line in node.body:
      for sub_line in visitor.visit(line, config, '', precedence).split('\n'):
        result += '\n' + config['if']['indent'] + sub_line
  if len(node.orelse) == 0: return result
  if len(node.orelse) == 1 and isinstance(node.orelse[0], ast.If):
    result += '\nel' + visitor.visit(node.orelse[0], config, '', precedence)
  elif len(node.orelse) == 1 and not config['if']['separate single line']:
    result += '\nelse' + config['if']['colon'] + visitor.visit(node.orelse[0], config, indent, precedence)
  else:
    result += '\nelse' + config['if']['colon']
    for line in node.orelse:
      for sub_line in visitor.visit(line, config, indent, precedence).split('\n'):
        result += '\n' + config['if']['indent'] + sub_line
  return result