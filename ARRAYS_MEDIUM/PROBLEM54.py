#SPIRAL MANNER MATRIX

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        result=[]
        top=0
        bottom=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        while top<=bottom and left<=right:
            #TRAVERSE TOP ROW
            for col in range(left,right+1):
                result.append(matrix[top][col])
            top+=1
            #TRAVERSE RIGHT COLUMN
            for row in range(top,bottom+1):
                result.append(matrix[row][right])
            right-=1
            #TRAVERSE BOTTOM ROW
            if top<=bottom:
                for col in range(right,left-1,-1):
                    result.append(matrix[bottom][col])
            bottom-=1
            #TRAVERSE LEFT COLUMN
            if left<=right:
                for row in range(bottom,top-1,-1):
                    result.append(matrix[row][left])
                left+=1
        return result
obj=Solution()
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(obj.spiralOrder(matrix))