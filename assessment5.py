import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="#b0c4de"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, pause=0.8):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show(block=False)
    plt.pause(pause)
    plt.close()

def heap_to_tree(heap):
    if not heap:
        return None
    nodes = [Node(val) for val in heap]
    n = len(heap)
    for i in range(n):
        left_i = 2 * i + 1
        right_i = 2 * i + 2
        if left_i < n:
            nodes[i].left = nodes[left_i]
        if right_i < n:
            nodes[i].right = nodes[right_i]
    return nodes[0]

def gradient_colors(n, start="#1a237e", end="#bbdefb"):
    def hex_to_rgb(h):
        h = h.lstrip('#')
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    def rgb_to_hex(rgb):
        return '#%02x%02x%02x' % rgb
    start_rgb = hex_to_rgb(start)
    end_rgb = hex_to_rgb(end)
    colors = []
    for i in range(n):
        rgb = tuple(
            int(start_rgb[j] + (end_rgb[j] - start_rgb[j]) * i / (n-1)) for j in range(3)
        )
        colors.append(rgb_to_hex(rgb))
    return colors

def dfs_visualize(root):
    stack = []
    order = []
    if root:
        stack.append(root)
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    colors = gradient_colors(len(order))
    for idx, node in enumerate(order):
        node.color = colors[idx]
        draw_tree(root)
    for node in order:
        node.color = "#b0c4de"

def bfs_visualize(root):
    queue = deque()
    order = []
    if root:
        queue.append(root)
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    colors = gradient_colors(len(order))
    for idx, node in enumerate(order):
        node.color = colors[idx]
        draw_tree(root)
    for node in order:
        node.color = "#b0c4de"


def main():
    heap = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    tree_root = heap_to_tree(heap)
    print("DFS traversal visualization:")
    dfs_visualize(tree_root)
    print("BFS traversal visualization:")
    bfs_visualize(tree_root)


if __name__ == "__main__":
    main()
