#leetcode question link: https://leetcode.com/problems/next-greater-element-i/description/

def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nums1Idx = { n:i for i , n in enumerate(nums1)}
    result = [-1] * len(nums1)
    s = [] #stack
    for i in range(len(nums2)):
        current = nums2[i]
        while s and current > s[-1]:
            val = s.pop()
            idx = nums1Idx[val]
            result[idx] = current
        if current in nums1Idx:
            s.append(current)
    return result

