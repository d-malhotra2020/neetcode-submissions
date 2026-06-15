class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        results = right

        while left <= right:
            k = (left + right) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                results = min(results, k)
                right = k - 1
            else:
                left = k + 1
        return results
                
                
