from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        row_zero = [False] * rows
        col_zero = [False] * cols

        # FIND ALL ORIGINAL ZEROS
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_zero[i] = True
                    col_zero[j] = True

        # UPDATE MATRIX
        for i in range(rows):
            for j in range(cols):
                if row_zero[i] or col_zero[j]:
                    matrix[i][j] = 0
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
obj = Solution()
obj.setZeroes(matrix)
print(matrix)