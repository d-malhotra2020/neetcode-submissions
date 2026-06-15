class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        columns = len(matrix[0])

        top = 0
        bottom = rows - 1

        while top <= bottom:
            middle_row = (top + bottom) // 2
            if matrix[middle_row][-1] < target:
                top = middle_row + 1
            elif matrix[middle_row][0] > target:
                bottom = middle_row - 1
            else:
                break
            
        
        middle_row = (top + bottom) // 2
        left = 0
        right = columns - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[middle_row][mid] < target:
                left = mid + 1
            elif matrix[middle_row][mid] > target:
                right = mid - 1
            else:
                return True
        return False
