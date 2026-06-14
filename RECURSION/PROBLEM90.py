#SUBSETS II (CONTAIN DUPLICATES) 

from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #SORT ARRAY SO THAT DUPLICATES BECOME ADJACENT
        nums.sort()
        #STORE ALL UNIQUE SUBSETS
        result=[]
        #BACKTRACK FUNCTION
        def backtrack(start,subset):
            #EVERY SUBSET FORMET SO FAS IS VALID
            result.append(subset[:])
            #TRY EVEVRY POSSIBLE ELEMENT FROM CURRNET POSITION
            for i in range(start,len(nums)):
                #SKIP DUPLICATES
                if i>start and nums[i]==nums[i-1]:
                    continue
                    #CHOOSE CURRENT ELEMENT
                subset.append(nums[i])
                #EXPLORE FURTHER
                backtrack(i+1,subset)
                # UNDO CHOICE (BACKTRACK)
                subset.pop()
        backtrack(0,[])
        return result
obj=Solution()
nums=[1,2,2]
print(obj.subsetsWithDup(nums))