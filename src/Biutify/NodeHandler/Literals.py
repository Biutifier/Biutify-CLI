def visit_Constant(visitor, node, config, indent = '', precedence = -1):
  if isinstance(node.value, str):
    return config['string']['preferred quote'] + str(node.value) + config['string']['preferred quote']
  return str(node.value)

def visit_FormattedValue(visitor, node, config, indent = '', precedence = -1):
  if node.conversion == 115 and config['fstring type'] == 'inline':
    return '{' + visitor.visit(node.value, config) + '}'
  return visitor.visit(node.value, config)

def visit_JoinedStr(visitor, node, config):
  result = ''
  for val in node.values:
    result += visitor.visit(val, config)
  return result

def visit_List(visitor, node, config, indent = '', precedence = -1):
  result = config['list']['begin with']
  separate_char = config['list']['separate with']
  if config['list']['newline after'] != 'never' and len(node.elts) > config['list']['newline after']:
    result += '\n' + indent + config['list']['indent newline with']
    separate_char += '\n' + indent + config['list']['indent newline with']
  for n in range(len(node.elts)):
    result += visitor.visit(node.elts[n], config, indent + config['list']['indent newline with'])
    if n < len(node.elts) - 1:
      result += separate_char
  if config['list']['newline after'] != 'never' and len(node.elts) > config['list']['newline after']:
    return result + '\n' + indent + config['list']['end with']
  else:
    return result + config['list']['end with']

def visit_Tuple(visitor, node, config, indent = '', precedence = -1):
  result = config['tuple']['begin with']
  separate_char = config['tuple']['separate with']
  if config['tuple']['newline after'] != 'never' and len(node.elts) > config['tuple']['newline after']:
    result += '\n' + indent + config['tuple']['indent newline with']
    separate_char += '\n' + indent + config['tuple']['indent newline with']
  for n in range(len(node.elts)):
    result += visitor.visit(node.elts[n], config, indent + config['tuple']['indent newline with'])
    if n < len(node.elts) - 1:
      result += separate_char
  if config['list']['newline after'] != 'never' and len(node.elts) > config['tuple']['newline after']:
    return result + '\n' + indent + config['tuple']['end with']
  else:
    return result + config['tuple']['end with']

def visit_Set(visitor, node, config, indent = '', precedence = -1):
  result = config['set']['begin with']
  separate_char = config['set']['separate with']
  if config['list']['newline after'] != 'never' and len(node.elts) > config['set']['newline after']:
    result += '\n' + indent + config['set']['indent newline with']
    separate_char += '\n ' + indent + config['set']['indent newline with']
  for n in range(len(node.elts)):
    result += visitor.visit(node.elts[n], config, indent + config['set']['indent newline with'])
    if n < len(node.keys) - 1:
      result += separate_char
  if config['set']['newline after'] != 'never' and len(node.elts) > config['set']['newline after']:
    return result + '\n' + indent + config['set']['end with']
  else:
    return result + config['set']['end with']

def visit_Dict(visitor, node, config, indent = '', precedence = -1):
  result = config['dict']['begin with']
  separate_char = config['dict']['separate with']
  if config['list']['newline after'] != 'never' and  len(node.keys) > config['dict']['newline after']:
    result += '\n' + indent + config['dict']['indent newline with']
    separate_char += '\n' + indent + config['dict']['indent newline with']
  for n in range(len(node.keys)):
    keystuff = visitor.visit(node.keys[n], config) + config['dict']['pair with']
    result += keystuff + visitor.visit(node.values[n], config, indent + config['dict']['indent newline with'])
    if n < len(node.keys) - 1:
      result += separate_char
  if config['dict']['newline after'] != 'never' and len(node.keys) > config['dict']['newline after']:
    return result + '\n' + indent + config['dict']['end with']
  else:
    return result + config['dict']['end with']
