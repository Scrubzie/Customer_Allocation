# Want to take in customers, create and solve distance matrix

def solve_tree(root):
    print("sefd")
    print(post_order_dfs(root))
    print(root)

#######
"""def post_order_dfs(root):
        result = []
        post_order_dfs_helper(root, result)
        return result

def post_order_dfs_helper(node, result):
    for child in node.get_children():
        post_order_dfs_helper(child, result)
    result.append(node.get_id())
"""
#######

# 
def post_order_dfs(root):
    result = []
    post_order_dfs_helper(root, result)
    return root

def post_order_dfs_helper(node, result):
    for child in node.get_children():
        post_order_dfs_helper(child, result)
    result.append(node.get_id())