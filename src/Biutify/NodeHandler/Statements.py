def visit_Assign(visitor, node, config, indent = '', precedence = -1):
  result = ''
  for t in range(len(node.targets)):
    result += visitor.visit(node.targets[t], config, indent, precedence)
    if t < len(node.targets) - 1:
      result += config['assign']['separate with']
  result += config['assign']['assign with']
  result += visitor.visit(node.value, config, indent, precedence)
  return result