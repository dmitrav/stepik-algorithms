

def in_order_traversal(node, tree):
    if node[1] > 0:
        in_order_traversal(tree[node[1]], tree)
    print(node[0], end=' ')  # visit
    if node[2] > 0:
        in_order_traversal(tree[node[2]], tree)


def pre_order_traversal(node, tree):
    print(node[0], end=' ')  # visit
    if node[1] > 0:
        pre_order_traversal(tree[node[1]], tree)
    if node[2] > 0:
        pre_order_traversal(tree[node[2]], tree)


def post_order_traversal(node, tree):
    if node[1] > 0:
        post_order_traversal(tree[node[1]], tree)
    if node[2] > 0:
        post_order_traversal(tree[node[2]], tree)
    print(node[0], end=' ')  # visit


if __name__ == '__main__':
    n = int(input())
    tree_nodes = []
    for i in range(n):
        key, left_id, right_id = [x for x in map(int, input().split())]
        tree_nodes.append((key, left_id, right_id))

    in_order_traversal(tree_nodes[0], tree_nodes)
    print()
    pre_order_traversal(tree_nodes[0], tree_nodes)
    print()
    post_order_traversal(tree_nodes[0], tree_nodes)