class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        res = [[] for i in range(len(nums) + 1)]
        topK = []
        
        for i in nums:
            freq_map[i] = 1 + freq_map.get(i, 0)
        
        for n, c in freq_map.items():
            res[c].append(n)

        for i in range(len(res) - 1, 0, -1):
            for j in res[i]:
                topK.append(j)
                if len(topK) == k:
                    return topK
  
        return res

        