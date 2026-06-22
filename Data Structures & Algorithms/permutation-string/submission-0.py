class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        s1Hashmap = [0] * 26
        s2Hashmap = [0] * 26

        for i in range(len(s1)):
            s1Hashmap[ord(s1[i]) - ord('a')] += 1
            s2Hashmap[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(26):
            matches += (1 if s1Hashmap[i] == s2Hashmap[i] else 0)
        
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[right]) - ord('a')
            s2Hashmap[index] += 1
            if s1Hashmap[index] == s2Hashmap[index]:
                matches += 1
            elif s1Hashmap[index] + 1 == s2Hashmap[index]:
                matches -= 1

            index = ord(s2[left]) - ord('a')
            s2Hashmap[index] -= 1
            if s1Hashmap[index] == s2Hashmap[index]:
                matches += 1
            elif s1Hashmap[index] - 1 == s2Hashmap[index]:
                matches -= 1
            left += 1
        return matches == 26
