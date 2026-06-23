class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        left = 0
        for i in range(len(nums)):
            if len(nums) > 1 and nums[left] == nums[left - 1]:
                return True
            left += 1
        return False