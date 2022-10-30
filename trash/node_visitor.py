import ast


class NodeVisitor(ast.NodeVisitor):
    def __init__(self, SymbolTable):
        self.symtable = SymbolTable
        for child in SymbolTable.get_children():
            self.symtable = child
            print(child.get_symbols())

    def _visit_children(self, node):
        """Determine if the node has children and visit"""
        for _, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        print('  visit item %s' % type(item).__name__)
                        self.visit(item)

            elif isinstance(value, ast.AST):
                print('  visit value %s' % type(value).__name__)
                self.visit(value)

    def generic_visit(self, node):
        # print(type(node).__name__)
        self._visit_children(node)

    def visit_Name(self, node):
        print('  variable %s type %s' % (node.id,
                                         self.symtable.lookup(node.id)))
        # print(dir(self.symtable.lookup(node.id)))
