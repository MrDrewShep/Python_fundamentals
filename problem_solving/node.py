
"""
THE FOLLOWING FILE IS JUST AN UNDER-THE-HOOD WAY OF LOOKING AT THE SAME COLLECTIONS WE ALREADY KNOW

Nodes as loops in a chain-link. Each node only knows 2 things: it's data, and next. So the list only knows the head-node. To find a node deep within, each node will have to look ahead to its next.
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.data} -> {self.next}'

    def get_data(self):
        return self.data

    def edit_data(self, new_value):
        self.data = new_value

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node