class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left <= right:
            if len(nums) > 1 and nums[left - 1] == nums[left]:
                return True
            left += 1
        return False