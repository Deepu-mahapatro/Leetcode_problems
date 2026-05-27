from typing import List
class Solution:
    def subSum(self, nums: List[int], k: int) -> int:
        #EDGE CASE: EMPTY ARRAY
        if nums==[]:
            return 0
        #PREFIX SUM-> FREQUENCY
        prefix_count={}
        #PREFIX SUM 0 EXISTS ONCE INITILALY
        prefix_count[0]=1
        #STRORE RUNNING PREFIX SUM
        current_sum=0
        #STORE FINAL ANSWER
        count=0
        #TRAVERSE THE ARRAY
        for num in nums:
            #UPDATE RUNNING SUM
            current_sum+=num
            #FIND REQUIRED PREFIX SUM
            needed_sum=current_sum-k
            #IF PREFIX SUM EXISTS
            #ADD ITS FREQUENCY
            if needed_sum in prefix_count:
                count+=prefix_count[needed_sum]
            #STORE CURRENT PREFIX SUM
            if current_sum in prefix_count:
                prefix_count[current_sum]+=1
            else:
                prefix_count[current_sum]=1
        return count
obj=Solution()
print(obj.subSum([1,2,1],2))