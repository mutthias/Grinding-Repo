class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        
        nums_set = set(nums)
        nums_list = list(nums_set)
        nums_list.sort()
        res = 0
        cur_len = 0
        # 1 2 3 4 100 200
        for i in range(1, len(nums_list)):
            if nums_list[i] - 1 == nums_list[i - 1]:
                cur_len += 1
            else:
                res = max(cur_len, res)
                cur_len = 0
        
        return max(res, cur_len) + 1
            


        