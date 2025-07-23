class Solution:
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        
        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return self.merge(left, right)
    
    def merge(self, left, right):
        merged_list = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged_list.append(left[i])
                i += 1
            else:
                merged_list.append(right[j])
                j += 1
        
        while i < len(left):
            merged_list.append(left[i])
            i += 1
        
        while j < len(right):
            merged_list.append(right[j])
            j += 1
        
        return merged_list

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)