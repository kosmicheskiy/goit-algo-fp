class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def insert_after(self, prev_node: Node, data):
    if prev_node is None:
      print("Попереднього вузла не існує.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key: int):
    cur = self.head
    if cur and cur.data == key:
      self.head = cur.next
      cur = None
      return
    prev = None
    while cur and cur.data != key:
      prev = cur
      cur = cur.next
    if cur is None:
      return
    prev.next = cur.next
    cur = None

  def search_element(self, data: int) -> Node | None:
    cur = self.head
    while cur:
      if cur.data == data:
        return cur
      cur = cur.next
    return None

  def print_list(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next

  def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

  def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        new_head = Node()
        current = self.head

        while current:
            next_node = current.next
            prev = new_head

            while prev.next and prev.next.data < current.data:
                prev = prev.next

            current.next = prev.next
            prev.next = current
            current = next_node

        self.head = new_head.next  

  def merge_sorted_lists(self, llist2):
    merged_list = LinkedList()
    current1 = self.head
    current2 = llist2.head

    while current1 is not None and current2 is not None:
        if current1.data < current2.data:
            merged_list.insert_at_end(current1.data)
            current1 = current1.next
        else:
            merged_list.insert_at_end(current2.data)
            current2 = current2.next

    while current1 is not None:
        merged_list.insert_at_end(current1.data)
        current1 = current1.next

    while current2 is not None:
        merged_list.insert_at_end(current2.data)
        current2 = current2.next

    return merged_list

llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

llist.reverse_list()

print("\nРеверсований список:")
llist.print_list()

llist.insertion_sort()

print("Відсортований список:")
llist.print_list()

# Створення другого відсортованого списку
llist2 = LinkedList()
llist2.insert_at_end(8)
llist2.insert_at_end(12)
llist2.insert_at_end(18)

# Об'єднання двох відсортованих списків
merged_list = llist.merge_sorted_lists(llist2)

# Друк об'єднаного відсортованого списку
print("Об'єднаний відсортований список:")
merged_list.print_list()
