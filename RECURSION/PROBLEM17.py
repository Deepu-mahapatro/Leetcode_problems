#LETTER COMBINATIONS OF PHONE NUMBERS
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #EDGE CASE
        if not digits:
            return []
        phone={
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
        }
        result=[]
        def backtrack(index,current):
            #BASE CASE
            #COMBINATION FOUND 
            if index==len(digits):
                result.append(current)
                return
            #GET LETTERS OF CURRENT DIGITS
            letters=phone[digits[index]]
            #TRY EVERY LETTER
            for ch in letters:
                #ADD LETTER
                backtrack(index+1,current+ch)
        backtrack(0,"")
        return result
obj=Solution()
digits="23"
print(obj.letterCombinations(digits))
        