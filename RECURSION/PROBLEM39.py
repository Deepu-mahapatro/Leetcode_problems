#COMBINATION SUM

from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #STORE ALL VALID COMBINATIONS
        result=[]
        def backtrack(start,target,path):
            #BASE CASE
            #IF TARGET BECOMES 0, WE FOUND VALID COMBINATION
            if target==0:
                result.append(path[:])
                return
            #IF TARGET BECOMES NEGATIVE THSI IS INVALID
            if target <0:
                return
            #TRY EVERY CANDIDATE STARTING FROM "START"
            for i in range(start,len(candidates)):
                #CHOOSE CURRENT NUMBER
                path.append(candidates[i])
                #REDUCE TARGET 
                backtrack(i,target-candidates[i],path)
                #REMOVE LAST NUMBER
                path.pop()
        #START RECURSION FROM INDEX 0
        backtrack(0,target,[])
        #RETURN ALL VALID COMBINATION
        return result
obj=Solution()
candidates=[2,3]
target=6
print(obj.combinationSum(candidates,target))  