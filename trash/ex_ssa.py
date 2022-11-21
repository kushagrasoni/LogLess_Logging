import os
import sys
import ast
import astor
import unittest
from scalpel.core.mnode import MNode
from scalpel.SSA.const import SSA

code_str = """
def foo():
    arg1 = 1
    arg2 = 2
    if arg1 > arg2:
        a = arg1 - arg2
    else:
        a = arg2 - arg1
    var = 5
    b = a * var
    return a + b
print(f'Output: {foo()}')
"""
def main():

    mnode = MNode("local")
    mnode.source = code_str
    mnode.gen_ast()
    cfg = mnode.gen_cfg()
    m_ssa = SSA()
    ssa_results, const_dict = m_ssa.compute_SSA(cfg)
    for block_id, stmt_res in ssa_results.items():
        print("These are the results for block ".format(block_id))
        print(stmt_res)
    for name, value in const_dict.items():
        print(name, value)
    print(ssa_results)

if __name__ == '__main__':
    main()