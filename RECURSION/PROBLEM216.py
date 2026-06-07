from typing import List
from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        def backtrack(start,path,current_sum):
            #VALID COMBINATION FOUND
            if len(path)==k and current_sum==n:
                result.append(path[:])
                return
            #INVALID STATE
            if len(path)>k or current_sum>n:
                return
            #TRY EVERY POSSIBLE NUMBER
            for num in range(start,10):
                #CHOOSE
                path.append(num)
                #EXPLORE
                backtrack(num+1,path,current_sum+num)
                #UNDO CHOICE
                path.pop()
        backtrack(1,[],0)
        return result
obj=Solution()
print(obj.combinationSum3(3,7))