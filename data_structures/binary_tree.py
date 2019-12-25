#HW solve for tower of hanoi
#HW solve for missionary cannibal problem

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, new_value):
        self.value = new_value

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def get_value(self):
        return self.value

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def balanced(self):
        return self.left and self.right


class BinaryTree:
    def __init__(self, root_node=None):
        self.root_node = root_node

    def set_root(self, new_root):
        self.root_node = new_root

    def length(self):
        return self._post_order(self.root_node)

    def add_node(self, item):
        new_node = TreeNode(item)
        if not self.root_node:
            self.root_node = new_node
        else:
            position = self._post_order(self.root_node)

            backtrack = []
            right = 0
            left = 1

            start = self.root_node

            while position > 0:
                if position % 2 == 0:
                    backtrack.insert(0, right)
                else:
                    backtrack.insert(0, left)

                position = int((position -1) / 2)
            
            final = backtrack.pop()
            for command in backtrack:
                if command:
                    start = start.get_left()
                else:
                    start = start.get_right()
            
            if final:
                start = start.set_left(new_node)
            else:
                start = start.set_right(new_node)
        
    def _post_order(self, node):
        if node:
            return 1 + self._post_order(node.get_left()) + self._post_order(node.get_right())
        return 0
        

""" My latest solution
    def _post_order(self, node, layer=-1, deepest_layer=None):

        layer += 1

        if node:
            self._post_order(node.get_left(), layer, deepest_layer)
            self._post_order(node.get_right(), layer, deepest_layer)
            layer -= 1
        else:
            if not deepest_layer:
                deepest_layer = layer
                i_am_where_the_new_node_belongs = node   # Need this ultimately returned, if the "if" below never fires

            if layer < deepest_layer:
                i_am_where_the_new_node_belongs = node
            else:
                layer -= 1

            if i_am_where_the_new_node_belongs:
                return deepest_layer, i_am_where_the_new_node_belongs
"""

""" Failed attempts...
    def drews_attempt(self, current, to_add):  # I'm looking for the first node that is NOT balanced
        if current.balanced:
            if current.get_left().balanced:
                if current.get_right().balanced:
                    drews_attempt(current.get_left(), to_add)
                elif not current.get_right().get_left():
                    current.get_right().set_left(to_add)
                else:
                    current.get_right().set_right(to_add)
            elif not current.get_left().get_left():
                current.get_left.set_left(to_add)
            else:
                current.get_left.set_right(to_add)
        elif not current.get_left():
            current.set_left(to_add)
        else:
            current.set_right(to_add)

    def _check_tree_balance(self, node):
        if node == None:
            return False
        if not node.left and not node.right:
            return True
        elif _check_tree_balance(node.get_left()) and _check_tree_balance(node.get_right()):
            return False

    def _add_node_recursive(self, current, to_add):
        if current.balanced():
            if current.get_left().balanced() and current.get_right.balanced():
                return _add_node_recursive(current.get_left(), to_add)
            elif current.get_left().balanced():
                return _add_node_recursive(current.get_left(), to_add)
            else:
                return _add_node_recursive(current.get_right(), to_add)

        if not current.get_left():
            current.set_left(to_add)
        elif not current.get_right():
            current.set_right(to_add)
"""




""" This was my first, and imcomplete attempt

    def add_node(self, new_node):
        if not self.root_node:
            self.root_node = new_node
        elif not self.root_node.get_left():
            self.root_node.set_left(new_node)
        elif not self.root_node.get_right():
            self.root_node.set_right(new_node)
        elif 
"""

new_tree = BinaryTree()

new_tree.add_node("Finally")
new_tree.add_node("Another")
new_tree.add_node("Answer")
print(new_tree.length())