class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freqMap = {}
        for s in magazine:
            freqMap[s] = freqMap.get(s, 0) + 1
        
        for s in ransomNote:
            if s not in magazine or freqMap[s] <= 0:
                return False
            freqMap[s] -= 1
        return True

        