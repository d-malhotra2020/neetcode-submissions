class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0
        while left < right:
            width = right - left
            h = min(heights[left], heights[right])
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            currentArea = width * h
            maxArea = max(maxArea, currentArea)
        return maxArea