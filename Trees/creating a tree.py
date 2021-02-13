# creating the tree node class
class TreeNode:
    # every node has its own data along with a list
    # of all its children nodes
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    # this prints the tree in a hierarchial / nested
    # list format
    def __str__(self, level=0):
        ret = " "*level+str(self.data)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    # this method can be used to add a child to
    # any given TreeNode.
    def addChild(self, TreeNode):
        self.children.append(TreeNode)


# create the tree structure
tree = TreeNode('Drinks', [])
cold = TreeNode('cold', [])
hot = TreeNode('hot', [])
tree.addChild(cold)
tree.addChild(hot)
tea = TreeNode('tea', [])
coffee = TreeNode('coffee', [])
hot.addChild(tea)
hot.addChild(coffee)
cola = TreeNode('cola', [])
fanta = TreeNode('fanta', [])
cold.addChild(cola)
cold.addChild(fanta)
print(tree)
