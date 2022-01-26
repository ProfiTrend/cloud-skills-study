# CS - Data Structure - Tree(Binary Tree)
# Jennas Lee

class Node:
    num = None
    left = None
    right = None

    def __init__(self, num):
        self.num = num


class Tree:
    root = None

    # 전위 순회
    def preOrder(self, node):
        print(node.num, end=' ')

        if node.left:
            self.preOrder(node.left)
        else:
            pass

        if node.right:
            self.preOrder(node.right)
        else:
            pass

    # 중위 순회
    def inOrder(self, node):
        if node.left:
            self.preOrder(node.left)
        else:
            pass

        print(node.num, end=' ')

        if node.right:
            self.preOrder(node.right)
        else:
            pass

    # 후위 순회
    def postOrder(self, node):
        if node.left:
            self.preOrder(node.left)
        else:
            pass

        if node.right:
            self.preOrder(node.right)
        else:
            pass

        print(node.num, end=' ')

    # make tree
    def make(self, node, left, right):
        if self.root is None:
            self.root = node
        else:
            pass

        node.left = left
        node.right = right


def main():
    print("BINARY TREE")
    # queue data structure
    tree = Tree()

    node_list = [Node(i) for i in range(1, 8)]

    # make tree using 1 to 7
    for i in range(int(len(node_list) / 2)):
        tree.make(node_list[i], node_list[i * 2 + 1], node_list[i * 2 + 2])
    #      1
    #   2     3
    # 4  5   6  7

    print('PRE ORDER')
    tree.preOrder(tree.root)
    print()

    print('IN ORDER')
    tree.inOrder(tree.root)
    print()

    print('POST ORDER')
    tree.postOrder(tree.root)
    print()


if __name__ == '__main__':
    main()
