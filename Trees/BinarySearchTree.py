class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return '('+str(self.left)+':L ' + "V:" + str(self.value) + " R:" + str(self.right)+')'


class BinarySearchTree(object):
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        new_node = Node(value)
        current_node = self.root
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    return self
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return self
                else:
                    current_node = current_node.right

    def look_up(self, value):
        current_node = self.root
        counter = 0
        while current_node:
            if value < current_node.value:

                current_node = current_node.left
                counter += 1
                if current_node.value == value:
                    return str(current_node.value) + ' is in leaf ' + str(counter)
            else:

                current_node = current_node.right
                counter += 1
                if current_node.value == value:
                    return str(current_node.value) + ' is in leaf ' + str(counter)

    def remove(self, value):
        currentNode = self.root
        parentNode = None
        while currentNode:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            elif value == currentNode.value:
                # option 1: No right child
                if currentNode.right is None:
                    if parentNode is None:
                        self.root = currentNode.left
                        return self
                    else:
                        # if parent > current value, make current left child a child of parent
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.left
                            return self
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.left
                            return self
                # Option 2: Right child which doesnt have a left child
                elif currentNode.right.left is None:
                    currentNode.right.left = currentNode.left
                    if parentNode == Node:
                        self.root = currentNode.right
                        return self
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.right
                            return self
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.right
                            return self
                # Option 3: Right child that has a left child
                else:
                    # find the Right child's left most child
                    leftmost = currentNode.right.left
                    leftmostParent = currentNode.right
                    while leftmost.left is not None:
                        leftmostParent = leftmost
                        leftmost = leftmost.left
                    # Parent's left subtree is now leftmost's right subtree
                    leftmostParent.left = leftmost.right
                    leftmost.left = currentNode.left
                    leftmost.right = currentNode.right

                    if parentNode is None:
                        self.root = leftmost
                        return self
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = leftmost
                            return self
                        elif currentNode.value > parentNode.value:
                            parentNode.right = leftmost
                            return self
        return True

    def traverse(self, node):
        tree = {'value': node.value, 'left': None if node.left is None else self.traverse(node.left),
                'right': None if node.right is None else self.traverse(node.right)}
        return tree


