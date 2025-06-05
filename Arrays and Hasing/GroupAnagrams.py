class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in range(0, len(strs)):
            s = "".join(sorted(strs[i]))
            hashmap[s].append(strs[i])

        return list(hashmap.values())
    
    """
    We can brute force by starting at each string, and then for each string, sort it,
    then traverse the entire array and see if there are any other matching sorted strings.
    This becomes super expensive, as sorting strings are an O(nlogn) operation, and having
    to loop through the entire list for each element makes the entire operation O(n^2logn).
    We can make this only O(nlogn) by using a hashmap. We iterate through every element in
    the array, but instead of having to iterate for every element, we can simply check if our
    element is in the hashmap. If it is, add it to the hash, and if not create a new key with
    the sorted string and the unsorted string as a value. Return a list of the hashmap values.
    """