class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            min_heights = min(heights[left], heights[right])
            width = right - left
            currentArea = min_heights * width
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
            max_area = max(max_area, currentArea)
        return max_area
            

        



    #[1, 7, 2, 5, 4, 7, 3, 6]
    # L                    R


