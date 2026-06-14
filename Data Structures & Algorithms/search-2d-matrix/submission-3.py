class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        columns = len(matrix[0])


        top = 0
        bottom = rows - 1

        while top <= bottom:
            middle_row = (top + bottom) // 2
            if target > matrix[middle_row][-1]:
                top = middle_row + 1
            elif target < matrix[middle_row][0]:
                bottom = middle_row - 1
            else:
                break
        
        if not (top <= bottom):
            return False
        
        middle_row = (top + bottom) // 2
        left = 0
        right = columns - 1
        while left <= right:
            middle = (left + right) // 2
            if target > matrix[middle_row][middle]:
                left = middle + 1
            elif target < matrix[middle_row][middle]:
                right = middle - 1
            else:
                return True
        return False
                 