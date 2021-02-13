class BinaryTree:
    def __init__(self, size):
        self.customList = size*[None]
        self.lastUsedIndex = 0
        self.maxSize = size

    # preorder traversal in a list based implementation
    # of a binary tree
    # in case of list based , we start from index = 1
    # Time Complexity : O(n) , Space Complexity : O(n) - Stack Memory
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal((2*index+1))

    # inorder traversal in a list based implementation
    # of a binary tree
    # in case of list based , we start from index = 1
    # Time Complexity : O(n) , Space Complexity : O(n) - Stack Memory
    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal((index*2+1))

    # postorder traversal in a list based implementation
    # of a binary tree
    # in case of list based , we start from index = 1
    # Time Complexity : O(n) , Space Complexity : O(n) - Stack Memory
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(2*index)
        self.postOrderTraversal(2*index+1)
        print(self.customList[index])

    # levelorder traversal in a list based implementation
    # of a binary tree
    # in case of list based , we start from index = 1
    # Time Complexity : O(n) , Space Complexity : O(1)
    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])

    # Time Complexity : O(1) , Space Complexity : O(1)
    def insertNode(self, value):
        if self.lastUsedIndex+1 == self.maxSize:
            return "BT is Full"
        else:
            self.customList[self.lastUsedIndex+1] = value
            self.lastUsedIndex += 1
            return "The value has been inserted"

    # Time Complexity : O(n) , Space Complexity : O(1)
    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Node Exists"
        return "Node DNE"

    # Time Complexity : O(n) , Space Complexity : O(1)
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "BT DNE"
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "Node Deleted"

    # function to delete the entire binary tree
    # Time Complexity : O(1) , Space Complexity : O(1)
    def deleteBinaryTree(self):
        self.customList = None
        return "BT Deleted"


tree = BinaryTree(8)
print(tree.insertNode("Drinks"))
print(tree.insertNode("Hot"))
print(tree.insertNode("Cold"))
print(tree.insertNode("Tea"))
print(tree.insertNode("Coffee"))
tree.levelOrderTraversal(1)
print(tree.deleteBinaryTree())
tree.levelOrderTraversal(1)
