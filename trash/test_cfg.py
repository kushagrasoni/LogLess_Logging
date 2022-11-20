from scalpel.cfg import CFGBuilder

from Scalpel.scalpel.import_graph.import_graph import ImportGraph, Tree

cfg = CFGBuilder().build_from_file('test_cfg_func.py', './test_cfg_func.py')


# cfg.build_visual('pdf')

for block in cfg:
    # print(dir(block))
    # print(block.get_source())
    print(block.statements)
    calls = block.get_calls()
    # print(dir(calls))
    print(calls)

# dot = cfg.build_visual('png')
# dot.render("cfg_diagram", view=False)


for (block_id, fun_name), fun_cfg in cfg.functioncfgs.items():
    print(block_id, fun_name)


# root_node = Tree("test_cfg_func.py")
# import_graph = ImportGraph()
# import_graph.build_dir_tree()
# module_dict = import_graph.parse_import(root_node)
# leaf_nodes = import_graph.get_leaf_nodes()
# print(len(leaf_nodes))

