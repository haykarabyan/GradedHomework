# PROBLEM 3#########


class Node(object):

    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def get_prev(self):
        return self.prev

    def set_next(self, new_next):
        self.next_node = new_next

    def set_prev(self, new_prev):
        self.prev_node = new_prev


class LinkedList():
    def __init__(self):
        self.header = Node(None, None, None)
        self.trailer = Node(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def addFirst(self, data):
        new_node = Node(data)
        new_node.set_next(self.header)
        self.header = new_node
        self.size += 1

    def len(self):
        return self.size

    def isempty(self):
        return self.size == 0

    def addLast(self, e):
        new_node = Node(e)
        if self.header is None:
            self.addFirst(e)
            return
        new_node.set_prev(self.trailer)
        self.trailer = new_node



    def insert_between(self, e, predecessor, successor):
        newest = Node(e, predecessor, successor)  # linked to neighbors
        predecessor.next = newest
        successor.prev = newest
        self.size += 1
        return newest

    def delete_node(self, node):
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        element = node.element  # record deleted element
        node.prev = node.next = node.element = None  # deprecate node
        return element

x = LinkedList()

for i in range(10):
  x.addLast(i)


def get_evens_and_odds_from_linked_lists(linked_list):
    i = linked_list.header
    while i.data is not None:
        evens = []
        odds = []
        if i.data%2==0:
            evens.append(i.data)
        else:
            odds.append(i.data)
        i = i.get_next()


# PROBLEM 1 ###

class Deque:
    def __init__(self):
        d = []
        self.size = 0

    def addFirst(self, key):
        self.d.insert(0, key)
        self.size += 1

    def addLast(self, key):
        self.d.append(key)
        self.size += 1

    def removeFirst(self):
        self.d.pop(0)
        self.size -= 1

    def removeLast(self):
        self.d.pop(self.size - 1)
        self.size -= 1

    def first(self):
        if self.d[0]:
            return self.d[0]

    def last(self):
        if self.d[self.size - 1]:
            return self.d[self.size - 1]
