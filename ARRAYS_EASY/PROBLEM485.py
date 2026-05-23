from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #CURRENT STREAK OF ONES
        curr_count=0
        #MAX STREAK OF ONES
        max_count=0
        #TRAVERSE EACH ELEMENT
        for i in nums:
            #IF CURRENT ELEMENT IS 1
            if i==1:
                #CONTINUE THE STREAK
                curr_count+=1
                #UPDATE MAX STREAK
                if curr_count>max_count:
                    max_count=curr_count
            #IF CURRENT ELEMENT IS 0
            else:
                #RESET THE CURRENT STREAK
                curr_count=0
        return max_count
nums=[1,1,1,1,0,1,1,1]
obj=Solution()
print(obj.findMaxConsecutiveOnes(nums))