import ast


class Lister(ast.NodeVisitor):
    def generic_visit(self, node):
        # print(type(node).__name__)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_FunctionDef(self, node):
        print(f'Function Def: {node.name}')
        self.generic_visit(node)

    def visit_Name(self, node):
        print('Name :', node.id)

    def visit_Num(self, node):
        print('Num :', node.__dict__['value'])

    def visit_Str(self, node):
        print("Str :", node.s)

    def visit_Print(self, node):
        print("print(:")
        self.generic_visit(node)

    def visit_Assign(self, node):
        print("Assign :")
        self.generic_visit(node)

    def visit_Expr(self, node):
        print("Expr :")
        self.generic_visit(node)
