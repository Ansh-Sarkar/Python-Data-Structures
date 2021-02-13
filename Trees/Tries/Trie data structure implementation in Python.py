class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    # inserting nodes (strings) in a trie
    # a. Trie is Blank
    # b. New strings prefix is common to another strings prefix
    # c. New strings prefix is already present as a complete string
    #       eg : API AND APIS
    # d. String to be presented already present in the Trie
    
    # Time Complexity : O(m) , m = Number of chars in word
    # Space Complexity : O(m) , worst case when word not present
    def insertNode(self,word):
        current=self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current=node
        current.endOfString=True
        print("Node inserted")
        
    # Searching in a Trie
    # a. Word does not exist
    # b. Word exists
    # c. prefix of another string is same as word but actual word 
    #       does not exist in the Trie
    def searchString(self,word):
        currentNode=self.root
        for i in word:
            node=currentNode.children.get(i)
            if node == None:
                return False
            currentNode=node
        if currentNode.endOfString==True:
            return True
        else:
            return False   # Prefix of some other string , Case 3
        
# deletion of a string from the Trie outside the class definition
def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False
    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)
        return False
    if index == len(word)-1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True
    if currentNode.endOfString == True:
        deleteString(currentNode, word, index+1)
        return False
    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False
        
# Time Complexity : O(1) , Space Complexity : O(1)
newT = Trie()
newT.insertNode("App")
newT.insertNode("Appl")
deleteString(newT.root, "App", 0)
print(newT.searchString("App"))

# Practical applications of Tries :
# Autocomplete and spelling suggestions
# Spelling Checkers
