# Function to check if triplet exists in a list with the given sum
def isTripletExist(nums, target):
 
    # create an empty dictionary
    d = {}
 
    # insert (element, index) pair into the dictionary for each input element
    for i, e in enumerate(nums):
        d[e] = i
 
    # consider each element except the last element
    for i in range(len(nums) - 1):
 
        # start from the i'th element until the last element
        for j in range(i + 1, len(nums)):
            # remaining sum
            val = target - (nums[i] + nums[j])
 
            # if the remaining sum is found, we have found a triplet
            if val in d:
                # if the triplet doesn't overlap, return true
                if d[val] != i and d[val] != j:
                    return True
 
    # return false if triplet doesn't exist
    return False
 
 
if __name__ == '__main__':
 
    nums = [2, 7, 4, 0, 9, 5, 1, 3]
    target = 6
 
    if isTripletExist(nums, target):
        print('Triplet exists')
    else:
        print('Triplet doesn\'t exist')
 
