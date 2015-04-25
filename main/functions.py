# -*- coding: utf-8 -*-
from pyflakes import checker
import _ast
import sys

def checkCode(codeString):
    filename = "code.py"
    
    warning = []
    try:
        tree = compile(codeString, filename, "exec", _ast.PyCF_ONLY_AST)
    except SyntaxError:
        value = sys.exc_info()[1]
        msg = value.args[0]

        (lineno, offset, text) = value.lineno, value.offset, value.text

        
        if text is None:            
            error = "unexpectedError: Problema de decodificación de la fuente";            
        else:
            error = "Code.py: "+str(lineno)+": " +msg + " -> " + text;            
        return True,False, error.capitalize()
    except Exception:
        #reporter.unexpectedError(filename, 'problem decoding source')
        error = "unexpectedError: Problema de decodificación de la fuente";        return False, error
    # Okay, it's syntactically valid.  Now check it.
    w = checker.Checker(tree, filename)
    w.messages.sort(key=lambda m: m.lineno)
    warns = False
    for war in w.messages:
        warns = True
        warning.append(str(war).capitalize())
    return False, warns ,warning
