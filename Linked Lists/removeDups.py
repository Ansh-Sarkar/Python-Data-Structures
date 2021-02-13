# function to remove the duplicate numbers in a linkedlist
# Time Complexity : O(n) , Space Complexity : O(n)
# space complexity because of the linked list made
from LinkedList import LinkedList

# function which uses a temporary buffer


def removeDups1(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        visited = set([currentNode.value])
        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next = currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
        return ll

# function without using a temporary buffer
# Time Complexity : O(n^2) , Space Complexity : O(1)
def removeDups2(ll):
    if ll.head is None:
        return
    currentNode = ll.head
    while currentNode:
        runner = currentNode
        while runner.next:
            if runner.next.value == currentNode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        currentNode = currentNode.next
    return ll.head


# driver code for testing functions and classes
ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
removeDups2(ll)
print(ll)
