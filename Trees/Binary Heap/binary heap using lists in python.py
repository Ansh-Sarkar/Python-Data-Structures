class Heap:
    def __init__(self, size):
        self.customList = (size+1)*[None]
        self.heapSize = 0
        self.maxSize = size+1

# Time Complexity : O(1) , Space Complexity : O(1)
def peekBH(rootNode):
    if not rootNode:
        return
    return rootNode.customList[1]

# Time Complexity : O(1) , Space Complexity : O(1)
def sizeofBH(rootNode):
    if not rootNode:
        return
    return rootNode.heapSize

# types of traversal : 4
# But we will be mainly using level order traversal here
# you may refer to the other methods from the binary tree section
# Time Complexity : O(n) , Space Complexity : O(1)
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    for i in range(1, rootNode.heapSize+1):
        print(rootNode.customList[i])

# helper function to modify and maintain the binary heap 
# properties and maintain type of Binary Heap
# Time Complexity : O(logN) , Space Complexity : O(logN) - Stack Memory
def heapify(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapify(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapify(rootNode, parentIndex, heapType)
        
# Time Complexity : O(logN) , Space Complexity : O(logN) - Stack Memory
def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize+1 == rootNode.maxSize:
        return "The BH is Full"
    rootNode.customList[rootNode.heapSize+1] = nodeValue
    rootNode.heapSize += 1
    heapify(rootNode, rootNode.heapSize, heapType)
    return "Node Inserted"

# Time Complexity : O(logN) , Space Complexity : O(logN) - Stack Memory
def heapifyExtract(rootNode, index, heapType):
    leftIndex = index*2
    rightIndex = index*2+1
    swapChild = 0
    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
    heapifyExtract(rootNode, swapChild, heapType)
    
# Time Complexity : O(logN) , Space Complexity : O(logN) - Stack Memory
def extractNode(rootNode,heapType):
    if rootNode.heapSize==0:
        return
    extractedNode = rootNode.customList[1]
    rootNode.customList[1]=rootNode.customList[rootNode.heapSize]
    rootNode.customList[rootNode.heapSize]=None
    rootNode.heapSize-=1
    heapifyExtract(rootNode,1,heapType)
    return extractedNode

# Time Complexity : O(1) , Space Complexity : O(1)
def deleteBH(rootNode):
    rootNode.customList = None
    
# main driver code for function testing
# Time Complexity : O(1) , Space Complexity : O(n)
newBH = Heap(5)
insertNode(newBH, 4, "Max")
insertNode(newBH, 5, "Max")
insertNode(newBH, 2, "Max")
insertNode(newBH, 1, "Max")
print(sizeofBH(newBH))
print("-------------")
levelOrderTraversal(newBH)
print("-------------")
print(extractNode(newBH, "Max"))
print("-------------")
levelOrderTraversal(newBH)
print("-------------")
deleteBH(newBH)
print("-------------")
levelOrderTraversal(newBH)


