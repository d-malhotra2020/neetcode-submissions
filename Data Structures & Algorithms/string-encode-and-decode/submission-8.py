class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        #""
        for s in strs:
            result += (str(len(s)) + "?" + s)
        #["5Hello?5World"]
        return result

    def decode(self, s: str) -> List[str]:
        results = []
        i = 0
        #[]
        while i < len(s):
            j = i
            while s[j] != "?":
                j += 1
            length = int(s[i:j])
            results.append(s[j+1:j+1+length])
            i = j + 1 + length
        return results