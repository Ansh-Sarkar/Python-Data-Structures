import QueueLinkedList as queue


class TreeNode:
    # Time Complexity : O(1) , Space Complexity : O(1)
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    # 3 Types of depth first traversal :
    # 1. preorder 2. inorder 3. postorder

    # preorder traversal :
    # root node -> Left Subtree (Full Left Subtree) -> Right Subtree (Full Right Subtree)
    # right subtrees rightmost leaf will be reached at last

    # inorder traversal :
    # left subtree (leftmost) -> root node -> right subtree (rightmost)
    # right most trees , rightmost leaf is visited last

    # postorder traversal :
    # left subtree (leftmost) -> right subtree (rightmost) -> root node
    # in this case , the last visited root is the root node

    # 1 Type of breadth first traversal : Level Order Traversal
    # Print the values of all nodes in a given level first and then
    # go to the next level


tree = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
tree.leftChild = leftChild
tree.rightChild = rightChild
left = TreeNode("Tea")
right = TreeNode("Coffee")
leftChild.leftChild = left
leftChild.rightChild = right

# Time Complexity : O(n) , Space Complexity : O(n) -> Stack Calls


def preorderTraversal(rootNode):
    if not rootNode:
        return
    else:
        print(rootNode.data)
    preorderTraversal(rootNode.leftChild)   # O(n/2) recursive
    preorderTraversal(rootNode.rightChild)  # O(n/2) recursive

# Time Complexity : O(n) , Space Complexity : O(n)


def inorderTraversal(rootNode):
    if not rootNode:
        return
    inorderTraversal((rootNode.leftChild))  # O(n/2) recursive
    print(rootNode.data)
    inorderTraversal(rootNode.rightChild)   # O(n/2) recursive

# Time Complexity : O(n) , Space Complexity : O(n)


def postorderTraversal(rootNode):
    if not rootNode:
        return
    postorderTraversal(rootNode.leftChild)  # O(n/2) recursive
    postorderTraversal(rootNode.rightChild)  # O(n/2) recursive
    print(rootNode.data)

# level order traversal implementation using Queue
# Time Complexity : O(n) , Space Complexity : O(n) (due to queue creation)


def levelorderTraversal(rootNode):
    if not rootNode:
        return
    else:
        q = queue.Queue()
        q.enqueue(rootNode)
        while not (q.isEmpty()):
            root = q.dequeue()
            # The value parameter is a part of the Node class
            print(root.value.data)
            if root.value.leftChild is not None:
                q.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                q.enqueue(root.value.rightChild)

# Time Complexity : O(n) , Space Complexity : O(n)
# normal level order traversal of a binary tree


def searchTree(rootNode, nodeValue):
    if not rootNode:
        return "BT DNE"
    else:
        q = queue.Queue()
        q.enqueue(rootNode)
        while not q.isEmpty():
            root = q.dequeue()
            if root.value.data == nodeValue:
                return "Node Exists"
            if root.value.leftChild is not None:
                q.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                q.enqueue(root.value.rightChild)
        return "Node DNE"

# Time Complexity : O(n) , Space Complexity : O(n)
# Inserts the new node in the first empty position found


def insertNode(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        q = queue.Queue()
        q.enqueue(rootNode)
        while not q.isEmpty():
            root = q.dequeue()
            if root.value.leftChild is not None:
                q.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Node Inserted"
            if root.value.rightChild is not None:
                q.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Node Inserted"

# Deletion of a Node in a Binary Tree
# Time Complexity : O(n) , Space Complexity : O(n)
# deepest node = last node visited during level order traversal
# replace value of node to be deleted to the deepest node
# and then delete the deepest node

# Time Complexity : O(n) , Space Complexity : O(n)
# function to get the deepest node of the tree
# helper function for main deletion function


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        q = queue.Queue()
        q.enqueue(rootNode)
        while not q.isEmpty():
            root = q.dequeue()
            if root.value.leftChild is not None:
                q.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                q.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode

# function to delete the deepest node from the tree
# helper function for main deletion function


def deleteDeepestNode(rootNode, deepestNode):
    if not rootNode:
        return
    else:
        q = queue.Queue()
        q.enqueue(rootNode)
        while not q.isEmpty():
            root = q.dequeue()
            if root.value is deepestNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is deepestNode:
                    root.value.rightChild = None
                    return
                else:
                    q.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is deepestNode:
                    root.value.leftChild = None
                    return
                else:
                    q.enqueue(root.value.leftChild)

# Time Complexity : O(n) , Space Complexity : O(n)
# main deletion function for removing a node from tree


def deleteNode(rootNode, node):
    if not rootNode:
        return "BT DNE"
    else:
        q = queue.Queue()
        q.enqueue(rootNode)
        while not q.isEmpty():
            root = q.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "Node Deleted"
            if root.value.leftChild is not None:
                q.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                q.enqueue(root.value.rightChild)
        return "Deletion Failed"

# function for deletion of the entire Binary Tree
# Time Complexity : O(1) , Space Complexity : O(1)


def deleteBinaryTree(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "BT Deleted"


deleteBinaryTree(tree)
levelorderTraversal(tree)
