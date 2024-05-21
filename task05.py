import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла
        self.color = "#000000"  # Початковий колір - чорний

def add_edges_dfs(graph, node, pos, x=0, y=0, layer=1, color_step=16):
    if node is not None:
        color = "#{:06x}".format(0x1296F0 - color_step * layer)  # Генерація кольору для вузла
        graph.add_node(node.id, color=color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges_dfs(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1, color_step=color_step)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges_dfs(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1, color_step=color_step)

def add_edges_bfs(graph, root, pos, color_step=16):
    queue = [(root, 0)]
    while queue:
        node, layer = queue.pop(0)
        color = "#{:06x}".format(0x1296F0 - color_step * layer)
        graph.add_node(node.id, color=color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            pos[node.left.id] = (pos[node.id][0] - 1 / 2 ** (layer + 1), pos[node.id][1] - 1)
            queue.append((node.left, layer + 1))
        if node.right:
            graph.add_edge(node.id, node.right.id)
            pos[node.right.id] = (pos[node.id][0] + 1 / 2 ** (layer + 1), pos[node.id][1] - 1)
            queue.append((node.right, layer + 1))

def draw_tree_dfs(tree_root, color_step=16):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges_dfs(tree, tree_root, pos, color_step=color_step)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def draw_tree_bfs(tree_root, color_step=64):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges_bfs(tree, tree_root, pos, color_step=color_step)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева з обходом у глиб
draw_tree_dfs(root)

# Відображення дерева з обходом у ширину
draw_tree_bfs(root)
