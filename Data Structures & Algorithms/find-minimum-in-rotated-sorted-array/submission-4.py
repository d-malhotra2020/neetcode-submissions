class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        results = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                results = min(results, nums[left])
                break
        
            mid = (left + right) // 2
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
            results = min(results, nums[mid])
        return results



        #[3, 4, 5, 6, 1, 2]

