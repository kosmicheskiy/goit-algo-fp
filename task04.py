import heapq
import networkx as nx
import matplotlib.pyplot as plt

class BinaryHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        heapq.heappush(self.heap, value)
    
    def draw_heap(self):
        heap_tree = nx.DiGraph()
        pos = {}

        for i, value in enumerate(self.heap):
            node_id = str(i)
            heap_tree.add_node(node_id, label=str(value))
            pos[node_id] = (i, 0)

            if i > 0:
                parent_id = str((i - 1) // 2)
                heap_tree.add_edge(parent_id, node_id)

        labels = {node[0]: node[1]['label'] for node in heap_tree.nodes(data=True)}

        plt.figure(figsize=(8, 5))
        nx.draw(heap_tree, pos=pos, labels=labels, arrows=False, node_size=2000, node_color='skyblue')
        plt.show()

# Створення бінарної купи та вставка елементів
heap = BinaryHeap()
heap.insert(10)
heap.insert(5)
heap.insert(7)
heap.insert(3)
heap.insert(1)
heap.insert(8)

# Відображення бінарної купи
heap.draw_heap()
