import ast

def visit_UnaryOp(visitor, node, config, indent = '', precedence = -1):
  operators = {
    ast.Invert: (config['operator']['invert'], 13),
    ast.Not: (config['operator']['not'], 5),
    ast.UAdd: (config['operator']['uadd'], 13),
    ast.USub: (config['operator']['usub'], 13)
  }
  for key in operators.keys():
    if isinstance(node.op, key):
      result = ''
      if operators[key][1] < precedence: result += '('
      result += operators[key][0]
      result += visitor.visit(node.operand, config, indent, operators[key][1])
      if operators[key][1] < precedence: result += ')'
      return result
  return ''

def visit_BinOp(visitor, node, config, indent = '', precedence = -1):
  operators = {
    ast.Add: (config['operator']['add'], 11),
    ast.Sub: (config['operator']['sub'], 11),
    ast.Mult: (config['operator']['mult'], 12),
    ast.Div: (config['operator']['div'], 12),
    ast.FloorDiv: (config['operator']['floordiv'], 12),
    ast.Mod: (config['operator']['mod'], 12),
    ast.Pow: (config['operator']['pow'], 14),
    ast.LShift: (config['operator']['lshift'], 10),
    ast.RShift: (config['operator']['rshift'], 10),
    ast.BitOr: (config['operator']['bitor'], 7),
    ast.BitXor: (config['operator']['bitxor'], 8),
    ast.BitAnd: (config['operator']['bitand'], 9),
    ast.MatMult: (config['operator']['matmult'], 12)
  }
  for key in operators.keys():
    if isinstance(node.op, key):
      result = ''
      if operators[key][1] < precedence: result += '('
      result += visitor.visit(node.left, config, indent, operators[key][1])
      result += operators[key][0]
      result += visitor.visit(node.right, config, indent, operators[key][1])
      if operators[key][1] < precedence: result += ')'
      return result
  return ''

def visit_BoolOp(visitor, node, config, indent = '', precedence = -1):
  operators = {
    ast.And: (config['operator']['and'], 4),
    ast.Or: (config['operator']['or'], 3),
  }
  result = ''
  for key in operators.keys():
    if isinstance(node.op, key):
      if operators[key][1] < precedence: result += '('
      for val in range(len(node.values)):
        result += visitor.visit(node.values[val], config, indent, operators[key][1])
        if val < len(node.values) - 1: result += operators[key][0]
      if operators[key][1] < precedence: result += ')'
  return result

def visit_Compare(visitor, node, config, indent = '', precedence = -1):
  operators = {
    ast.Eq: (config['operator']['eq'], 6),
    ast.NotEq: (config['operator']['noteq'], 6),
    ast.Lt: (config['operator']['lt'], 6),
    ast.LtE: (config['operator']['lte'], 6),
    ast.Gt: (config['operator']['gt'], 6),
    ast.GtE: (config['operator']['gte'], 6),
    ast.Is: (config['operator']['is'], 6),
    ast.IsNot: (config['operator']['isnot'], 6),
    ast.In: (config['operator']['in'], 6),
    ast.NotIn: (config['operator']['notin'], 6),
  }
  result = ''
  if 6 < precedence: result += '('
  result += visitor.visit(node.left, config, indent, 6)
  for opid in range(len(node.ops)):
    for key in operators.keys():
      if isinstance(node.ops[opid], key):
        result += operators[key][0]
        result += visitor.visit(node.comparators[opid], config, indent, 6)
  if 6 < precedence: result += ')'
  return result

def visit_Call(visitor, node, config, indent = '', precedence = -1):
  result = visitor.visit(node.func, config, indent, precedence) + config['function call']['start args with']
  for arg in range(len(node.args)):
    result += visitor.visit(node.args[arg], config, indent, precedence)
    if arg < len(node.args) - 1 or len(node.keywords) > 0:
      result += config['function call']['separate args with']
  for kwd in range(len(node.keywords)):
    result += visitor.visit(node.keywords[kwd], config, indent, precedence)
    if kwd < len(node.keywords) - 1:
      result += config['function call']['separate args with']
  return result + config['function call']['end args with']

def visit_keyword(visitor, node, config, indent = '', precedence = -1):
  return node.arg + config['keyword']['assign with'] + visitor.visit(node.value, config, indent, precedence)

def visit_IfExp(visitor, node, config, indent = '', precedence = -1):
  result = visitor.visit(node.body, config, indent, precedence)
  result += config['if expression']['if']
  result += visitor.visit(node.test, config, indent, precedence)
  result += config['if expression']['else']
  result += visitor.visit(node.orelse, config, indent, precedence)
  return result

def visit_Attribute(visitor, node, config, indent = '', precedence = -1):
  return visitor.visit(node.value, config, indent, precedence) + config['attribute']['access with'] + visitor.visit(node.attr, config, indent, precedence)
