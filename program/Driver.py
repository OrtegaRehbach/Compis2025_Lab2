import sys
from antlr4 import *
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from type_check_visitor import TypeCheckVisitor

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = SimpleLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SimpleLangParser(stream)
    tree = parser.prog()

    visitor = TypeCheckVisitor()
    visitor.visit(tree) # Visit the root
    
    if not visitor.errors:
        print("Type checking passed")
        return
    
    for e in visitor.errors:
        print(f"Type checking error: {e}")

if __name__ == '__main__':
    main(sys.argv)
