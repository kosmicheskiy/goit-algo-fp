import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
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
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def depth_first_traversal(node, traversal_order):
    if node:
        traversal_order.append(node)
        node.color = generate_color(len(traversal_order))
        depth_first_traversal(node.left, traversal_order)
        depth_first_traversal(node.right, traversal_order)

def breadth_first_traversal(node, traversal_order):
    queue = [node]
    while queue:
        current_node = queue.pop(0)
        if current_node:
            traversal_order.append(current_node)
            current_node.color = generate_color(len(traversal_order))
            queue.append(current_node.left)
            queue.append(current_node.right)

def generate_color(step):
    # Generate a color based on the step in the traversal
    color_value = 255 - int((step / 10) * 255)
    color_hex = "#{:02X}{:02X}{:02X}".format(color_value, color_value, 255)
    return color_hex

# Create a binary tree
heap_root = Node(0)
heap_root.left = Node(4)
heap_root.right = Node(1)
heap_root.left.left = Node(5)
heap_root.left.right = Node(10)
heap_root.right.left = Node(3)

# Depth-first traversal
depth_first_order = []
depth_first_traversal(heap_root, depth_first_order)

# Visualize depth-first traversal
draw_heap(heap_root)

# Reset colors for breadth-first traversal
for node in depth_first_order:
    node.color = "skyblue"

# Breadth-first traversal
breadth_first_order = []
breadth_first_traversal(heap_root, breadth_first_order)

# Visualize breadth-first traversal
draw_heap(heap_root)
