#GENERATE PARENTHESIS
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #EDGE CASE
        if n<=0:
            return []
        result=[]
        def backtrack(curr,open,close):
            #VALID LENGTH
            if len(curr)==n*2:
                result.append(curr)
                return
            #TO ADD "(" 
            if open<n:
                backtrack(curr+"(",open+1,close)
            #TO ADD ")"
            if close<open:
                backtrack(curr+")",open,close+1)
        #SET VALID INPUTS
        backtrack("",0,0)
        return result
obj=Solution()
print(obj.generateParenthesis(3))