def visit_Name(visitor, node, config, indent = '', precedence = -1):
  return node.id

def visit_Starred(visitor, node, config, indent = '', precedence = -1):
  return config['variable']['star with'] + visitor.visit(node.id)