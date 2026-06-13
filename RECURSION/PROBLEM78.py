#SUBSETS (POWER SET)

from typing import List
class Solution:
    def subsets(self,nums:List[int])->List[List[int]]:
        #EDGE CASE
        if not nums:
            return []
        result=[]
        def backtrack(index,path):
            #BASE CASE
            if index==len(nums):
                result.append(path[:])
                return
            #INCLUDE CURRENT ELEMENT
            path.append(nums[index])
            backtrack(index+1,path)
            #EXCLUDE CURRENT ELEMENT
            path.pop()
            backtrack(index+1,path)
        backtrack(0,[])
        return result
obj=Solution()
nums=[1,2,3]
print(obj.subsets(nums))