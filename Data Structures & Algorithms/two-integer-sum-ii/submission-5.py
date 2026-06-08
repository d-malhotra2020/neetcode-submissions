class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            sumNum = numbers[left] + numbers[right]
            if sumNum < target and numbers[left] != numbers[right]:
                left += 1
            elif sumNum > target and numbers[left] != numbers[right]:
                right -=1
            else:
                return [left + 1, right + 1]
        