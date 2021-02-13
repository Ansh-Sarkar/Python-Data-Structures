import QueueLinkedList as queue


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.rightChild = None
        self.leftChild = None
        self.height = 1

# Time Complexity : O(n) , Space Complexity : O(n) - Stack Memory


def preorderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preorderTraversal(rootNode.leftChild)
    preorderTraversal(rootNode.rightChild)

# Time Complexity : O(n) , Space Complexity : O(n) - Stack Memory
# Gives sorted output - In Order Traversal


def inorderTraversal(rootNode):
    if not rootNode:
        return
    inorderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inorderTraversal(rootNode.rightChild)

# Time Complexity : O(n) , Space Complexity : O(n) - Stack Memory


def postorderTraversal(rootNode):
    if not rootNode:
        return
    postorderTraversal(rootNode.leftChild)
    postorderTraversal(rootNode.rightChild)
    print(rootNode.data)

# Time Complexity : O(n) , Space Complexity : O(n)


def levelorderTraversal(rootNode):
    if not rootNode:
        return
    else:
        q = queue.Queue()
        q.enqueue(rootNode)
        while not q.isEmpty():
            root = q.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                q.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                q.enqueue(root.value.rightChild)

# Time Complexity : O(logN) , Space Complexity : O(logN) - Stack Memory (!Imp!)


def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("Node Exists")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("Node Exists")
        else:
            searchNode(rootNode.leftChild, nodeValue)  # O(N/2)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("Node Exists")
        else:
            searchNode(rootNode.rightChild, nodeValue)  # O(N/2)

# Cases in insertion of a node in AVL Tree
# 1. Rotation required
#       Tree remains balanced after insertion
#       Required steps same as Binary Search Tree
# 2. Rotation Not Required
#       a. left left condition - right rotation required
#       b. left right condition - left and then right rotation
#           i.  left rotate - disbalanced nodes left child
#           ii. right rotate after that
#       c. right right condition - left rotation required
#       d. right left condition - right and then left rotation
#           i.  right rotate - disbalanced nodes right child
#           ii. left rotate after that

# Time Complexity : O(1) , Space Complexity : O(1)


def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

# Time Complexity : O(1) , Space Complexity : O(1)


def rightRotation(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    # adding 1 to include the parent node
    disbalancedNode.height = 1 + \
        max(getHeight(disbalancedNode.leftChild),
            getHeight(disbalancedNode.rightChild))
    newRoot.height = 1+max(getHeight(newRoot.leftChild),
                           getHeight(newRoot.rightChild))
    return newRoot

# Time Complexity : O(1) , Space Complexity : O(1)


def leftRotation(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + \
        max(getHeight(disbalancedNode.leftChild),
            getHeight(disbalancedNode.rightChild))
    newRoot.height = 1+max(getHeight(newRoot.leftChild),
                           getHeight(newRoot.rightChild))
    return newRoot

# Time Complexity : O(1) , Space Complexity : O(1)


def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild)-getHeight(rootNode.rightChild)


# Time Complexity : O(logN) , Space Complexity : O(logN) - Stack Memory
def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    rootNode.height = 1+max(getHeight(rootNode.leftChild),
                            getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotation(rootNode)
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotation(rootNode)
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)
    return rootNode

# deletion of a node :
# 1. RootNode does not exist
# 2. Rotation not required
#       i.   LeafNode
#       ii.  Has one ChildNode
#       iii. Has two ChildNodes (Find Successor)
#               Successor = Min elem in right sub-tree
# 3. Rotation is required
#       a. left left condition
#       b. left right condition
#       c. right right condition
#       d. right left condition

# Time Complexity : O(logN) , Space Complexity : O(logN) - Stack Memory


def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)

# Time Complexity : O(logN) , Space Complexity : O(logN) - Stack Memory


def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    # checking for possible unbalanced nodes and balancing
    # using rotations ( left / right or both )
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotation(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotation(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotation(rootNode.leftChild)
        return rightRotation(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rightRotation(rootNode.rightChild)
        return leftRotation(rootNode)
    return rootNode

# Time Complexity : O(1) , Space Complexity : O(1)


def deleteAVLTree(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "AVLTree Deleted !"


# Time Complexity : O(1) , Space Complexity : O(1)
newAVL = AVLNode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
levelorderTraversal(newAVL)
print("----------------")
newAVL = deleteNode(newAVL, 15)
levelorderTraversal(newAVL)
print("----------------")
deleteAVLTree(newAVL)
levelorderTraversal(newAVL)
