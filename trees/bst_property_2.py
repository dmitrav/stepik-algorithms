
""" More general property: left < node <= right """

INT_MAX = 4294967296
INT_MIN = -4294967296

import sys
sys.setrecursionlimit(50000)


def is_bs_tree(node, tree):
    return check_bs_tree_property(node, tree, INT_MIN, INT_MAX)


def check_bs_tree_property(node, tree, mini, maxi):

    # False if this node violates min/max constraint
    if node[0] < mini or node[0] > maxi:
        return False

    if node[1] < 0 and node[2] > 0:
        # there is only right subtree
        return check_bs_tree_property(tree[node[2]], tree, node[0], maxi)

    elif node[1] > 0 and node[2] < 0:
        # there is only left subtree
        return check_bs_tree_property(tree[node[1]], tree, mini, node[0] - 1)

    elif node[1] < 0 and node[2] < 0:
        # it is a leaf
        return True
    else:
        return check_bs_tree_property(tree[node[1]], tree, mini, node[0] - 1) and check_bs_tree_property(tree[node[2]], tree, node[0], maxi)


if __name__ == "__main__":

    n = int(input())
    tree_nodes = []
    for i in range(n):
        key, left_id, right_id = [x for x in map(int, input().split())]
        tree_nodes.append((key, left_id, right_id))

    if n == 0 or is_bs_tree(tree_nodes[0], tree_nodes):
        print("CORRECT")
    else:
        print("INCORRECT")