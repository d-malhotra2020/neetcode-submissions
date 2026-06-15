class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        results = right

        while left <= right:
            k = (left + right) //2
            min_hours = 0
            for p in piles:
                min_hours += math.ceil(p / k)
            if min_hours <= h:
                right = k - 1
                results = min(results, k)
            else:
                left = k + 1
        return results


        #[1, 4, 3, 2] h = 9
