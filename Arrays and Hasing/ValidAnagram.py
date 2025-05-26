class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash = defaultdict(int)
        t_hash = defaultdict(int)
        
        for i in s:
            s_hash[i] += 1
        
        for i in t:
            t_hash[i] += 1
        
        return s_hash == t_hash

"""
To check if this is an anagram, we do the hashmap method, where each character maps to a
count. If the strings aren't equal length, we can return false promptly. Otherwise, we loop
through each string and create hashmaps for both. If the hashmaps are equal, then return true,
otherwise false. This will be O(2n) --> O(n).
"""