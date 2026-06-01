class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        hashmap = {}

        for word in strs:
            freq = [0] * 26
            for character in word:
                freq[ord(character) - ord('a')] += 1
            key = tuple(freq)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)
        for word in hashmap.values():
            result.append(word)
        return result
        

                