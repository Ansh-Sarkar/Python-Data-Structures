# integer input based hash function
# simple modulus function
def hash1(number, cellNumber):
    return number % cellNumber

# string based hash function
# ASCII Function
def modASCII(string, cellNumber):
    total = 0
    for i in string:
        total += ord(i)
    return total % cellNumber

# Properties of good hash functions
# a. should be able to distribute the hash values uniformly 
#    across the hash tables
# b. It should you use the entire input data in order to 
#    generate the hash values

# Collision resolution techniques
# a. Direct Chaining : Implement buckets as Linked Lists
#                      Store colliding elements in lists
#
# b. Open Addressing : Stored in Vacant Buckets. Probing : 
#       i.   Linear Probing :place new key in the closest 
#               empty cell.
#       ii.  Quadratic Probing : Adding an arbitrary 
#               quadratic polynomial to the index until 
#               an empty cell is found.
#       iii. Double Hashing : Interval between probes is 
#               computed using a second hash function
