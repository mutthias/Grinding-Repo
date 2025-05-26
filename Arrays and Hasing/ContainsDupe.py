class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        for i in nums:
            if i in hashmap:
                return True
            hashmap.add(i)
        
        return False
    
    """
    To check if we have a duplicate in an array, we can sort the array and then see if a subsequent
    number is the same as the former. This would be O(nlogn), because we need to sort the array (O(nlogn))
    and then traverse the entire array (O(n)). To make this O(n), we use a set instead to keep track of 
    numbers we've discovered. If we encounter a number in the set, then we have a duplicate and can return true.
    """