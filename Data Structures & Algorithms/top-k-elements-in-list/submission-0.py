class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [5,5,5, 4,4, 3]
        c = Counter(nums)
        h = []
        for item in c.items():
            heapq.heappush(h, ((item[1], item[0])))
            if len(h) > k:
                heapq.heappop(h)
        return [a[1] for a in h]    


    # # [1,3,2,3,5,6,6,7,7,7,7]

    # {1:1, 2:2, 3:3}
    # k=1 -> [3]
    # k = 2 -> [2,3]
    # k = 0 > []