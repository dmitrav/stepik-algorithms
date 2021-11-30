

def in_order_traversal(root, tree):
    if root[1] > 0:
        in_order_traversal(tree[root[1]], tree)
    print(root[0], end=' ')
    if root[2] > 0:
        in_order_traversal(tree[root[2]], tree)


def pre_order_traversal(root, tree):
    print(root[0], end=' ')
    if root[1] > 0:
        pre_order_traversal(tree[root[1]], tree)
    if root[2] > 0:
        pre_order_traversal(tree[root[2]], tree)


def post_order_traversal(root, tree):
    if root[1] > 0:
        post_order_traversal(tree[root[1]], tree)
    if root[2] > 0:
        post_order_traversal(tree[root[2]], tree)
    print(root[0], end=' ')


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