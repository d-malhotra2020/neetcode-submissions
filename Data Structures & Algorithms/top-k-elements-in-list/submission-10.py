class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # count = {1:1, 2:2, 3:3}

        for n, c in count.items():
            frequency[c].append(n)

        #frequency = [0], [1], [2], [3]
        #             0,   1,   2,   3

        result = []
        for i in range(len(frequency) -1, 0, -1):
            for n in frequency[i]:
                result.append(n)
                # result = [3, 2, 1, 0]
                while len(result) == k:
                    return result
                        #result = [3, 2]
        

        