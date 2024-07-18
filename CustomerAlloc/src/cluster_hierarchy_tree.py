from cluster_tree_solver import *

class TreeNode:
    def __init__(self, cluster_id, customers=None, route=None):
        self.id = cluster_id
        self.customers = []
        self.route = route
        self.children = []
        self.cost = None

    # Getters
    def get_id(self):
        return self.id

    def get_customers(self):
        return self.customers
    
    def get_route(self):
        return self.route
    
    def get_children(self):
        return self.children
    
    def get_cost(self):
        return self.cost

    # Setters (Only using add_child and add_customer currently, 17/07/2024)
    def add_child(self, child_node):
        if not isinstance(child_node, TreeNode):
            raise TypeError("child_node must be a TreeNode")
        self.children.append(child_node)


    def add_customer(self, customer):
        self.customers.append(customer)

    def set_customers(self, customers):
        self.customers = customers

    def post_order_dfs(self):
        result = []
        self._post_order_dfs_helper(self, result)
        return result

    def _post_order_dfs_helper(self, node, result):
        for child in node.children:
            self._post_order_dfs_helper(child, result)
        result.append(node.id)

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.id) + ": " + repr(self.customers) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret
    
    def find_node_by_id(self, target_id):
        result = []
        self._find_node_by_id_helper(self, target_id, result)
        if result:
            return result[0]
        else:
            return None

    def _find_node_by_id_helper(self, node, target_id, result):
        if node.id == target_id:
            result.append(node)
        for child in node.children:
            self._find_node_by_id_helper(child, target_id, result)

    def solve_tree(self):
        solve_tree(self)

    
    # Setters and getters
    # CRUD (Find is part of Read)

"""root = TreeNode("root", 0)
child1 = TreeNode("child1", 1)
child2 = TreeNode("child2", 2)
child3 = TreeNode("child3", 3)
child4 = TreeNode("child4", 4)

root.add_child(child1)
root.add_child(child2)
child1.add_child(child3)
child1.add_child(child4)

print(root)

post_order_result = root.post_order_dfs()
print(f"Post-order DFS: {post_order_result}")"""