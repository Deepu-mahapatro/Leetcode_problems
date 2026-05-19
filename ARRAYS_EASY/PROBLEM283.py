#MOVE ALL ZEROS TO END 

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index=0
        #MOVE NON ZERO FORWARD
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[index]=nums[i]
                index+=1
        while index<len(nums):
            nums[index]=0
            index+=1
nums=[1,2,3,4,0,3,0]
obj=Solution()
obj.moveZeroes(nums)
print(nums)