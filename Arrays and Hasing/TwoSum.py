class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[val] = i
        
        return [0, 0]

"""
We don't want the obvious O(n^2) solution of scanning the entire array per element.
We create a hashmap that will hold a (value, index) pair. We find a difference by 
subtracting the target - current value. If the difference is in the hashmap, return
the current index i that we are at, as well as the value at hashmap[val]. If not,
add this val to the hashmap, with the index as its key --> hashmap[val] = i. 
"""