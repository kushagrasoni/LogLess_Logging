import ast


class Lister(ast.NodeVisitor):
    def generic_visit(self, node):

        for field, value in ast.iter_fields(node):
        # for field, value in ast.iter_child_nodes(node):
            print(field, value)
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        self.visit(item)
            elif isinstance(value, ast.AST):
                self.visit(value)
        # ast.NodeVisitor.generic_visit(self, node)

    def visit_Print(self, node):
        self.generic_visit(node)
        print(type(node).__name__, node)

    def visit_Expr(self, node):
        self.generic_visit(node)
        print(type(node).__name__, node)

    def visit_Assign(self, node):
        """ visit a Assign node and visits it recursively"""
        self.generic_visit(node)
        print(type(node).__name__, node.value)

    def visit_BinOp(self, node):
        """ visit a BinOp node and visits it recursively"""
        self.generic_visit(node)
        print(type(node).__name__)

    def visit_Call(self, node):
        """ visit a Call node and visits it recursively"""
        self.generic_visit(node)
        print(type(node).__name__)

    def visit_Lambda(self, node):
        """ visit a Function node """
        self.generic_visit(node)
        print(type(node).__name__)

    def visit_FunctionDef(self, node):
        """ visit a Function node and visits it recursively"""
        self.generic_visit(node)
        print(type(node).__name__)

    def visit_Module(self, node):
        """ visit a Module node and the visits recursively"""
        self.generic_visit(node)

    def visit_arguments(self, node):
        """ visit a Arguments node and visits it recursively"""
        self.generic_visit(node)
        print(type(node).__name__)

    def visit_arg(self, node):
        """ visit a Arg node and visits it recursively"""
        self.generic_visit(node)
        print(type(node).__name__, node.__dict__['arg'])

    def visit_Num(self, node):
        """ visit a Num node and visits it recursively"""
        self.generic_visit(node)
        print(type(node).__name__, node.__dict__['value'])

    def visit_Str(self, node):
        """ visit a Str node and visits it recursively"""
        self.generic_visit(node)
        print(type(node).__name__, node.s)

    def visit_Constant(self, node):
        """ visit a Str node and visits it recursively"""
        self.generic_visit(node)
        print(type(node).__name__, node.value)

    def visit_Name(self, node):
        """ visit a Str node and visits it recursively"""
        self.generic_visit(node)
        print(type(node).__name__, node.id)
