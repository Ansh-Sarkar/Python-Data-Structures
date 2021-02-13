import QueueLinkedList as queue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.rightChild = None
        self.leftChild = None

# method for insertion of a new value in a BST
# Time Complexity : O(logN) , Space Complexity : O(n)
def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)   # O(N/2)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)  # O(N/2)
    return "Node Insertion Successful"

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
        q=queue.Queue()
        q.enqueue(rootNode)
        while not q.isEmpty():
            root=q.dequeue()
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
        
# Time Complexity : O(logN) , Space Complexity : O(1)
def minValueNode(bstNode):
    current=bstNode
    while current.leftChild is not None:
        current=current.leftChild
    return current

# Time Complexity : O(logN) , Space Complexity : O(logN) - Selected Stacked Calls
def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)    # O(n/2)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)  # O(n/2)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp

        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = minValueNode(rootNode.rightChild)  # O(logN)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(
            rootNode.rightChild, temp.data)  # O(n/2)
    return rootNode

# Time Complexity : O(1) , Space Complexity : O(1)
def deleteBST(rootNode):
    rootNode.data = None
    rootNode.rightChild = None
    rootNode.leftChild = None
    return "BST Deleted !"
    
# creation of the BST by creating the root node
# Time Complexity : O(1) , space Complexity : O(1)
newBST = BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)
levelorderTraversal(newBST)
print(deleteBST(newBST))
levelorderTraversal(newBST)

