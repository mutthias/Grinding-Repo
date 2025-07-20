class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_total = defaultdict(int)
        res = 0
        hash_total[0] = 1
        cur_sum = 0

        for num in nums:
            cur_sum += num
            if cur_sum - k in hash_total:
                res += hash_total[cur_sum - k]
            hash_total[cur_sum] += 1
        
        return res
