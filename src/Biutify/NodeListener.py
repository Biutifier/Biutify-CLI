import ast
import Biutify.NodeHandler as Handler


class Visitor(ast.NodeVisitor):

  def visit(self, node, config, indent = '', precedence = -1):
        """Visit a node."""
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(Handler, method, self.generic_visit)
        # print('VISIT TYPE: ' + visitor.__name__)
        return visitor(self, node, config, indent, precedence)

  def generic_visit(self, visitor, node, config, indent = '', precedence = -1):
    result = ''
    for _, value in ast.iter_fields(node):
      if isinstance(value, list):
        for item in value:
          if isinstance(item, ast.AST):
            result += visitor.visit(item, config, indent, precedence) + '\n'
      if isinstance(value, ast.AST):
        result += visitor.visit(value, config, indent, precedence)

    return result

  def rebuild(self, tree, config):
    return self.generic_visit(self, tree, config, '')
