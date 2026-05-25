from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #EDGE CASE: EMPTY ARRAY
        if len(nums)==0:
            return 
        #COUNT VARIABLES
        count0=0
        count1=0
        count2=0
        #COUNT FREQUENCIES
        for num in nums:
            #COUNT 0'S
            if num==0:
                count0+=1
            #COUNT 1'S
            elif num==1:
                count1+=1
            #COUNT 2'S
            else:
                count2+=1
        #REBUILD ARRAY
        index=0
        #PLACE ALL 0'S
        for i in range(count0):
            nums[index]=0
            index+=1
        #PLACE ALL 1'S
        for i in range(count1):
            nums[index]=1
            index+=1
        #PLACE ALL 2'S
        for i in range(count2):
            nums[index]=2
            index+=1
obj=Solution()
nums=[2,0,2,1,1,0]
obj.sortColors(nums)
print(nums)

            