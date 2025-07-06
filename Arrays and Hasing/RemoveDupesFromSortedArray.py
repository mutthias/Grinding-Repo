class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        l = 1
        r = len(nums)

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            
            else:
                count = 1
            
            if count <= 2:
                nums[l] = nums[i]
                l += 1
        
        return l
