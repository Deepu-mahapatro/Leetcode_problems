#FIND PEAK ELEMENT

#USING BINARY SEARCH METHOD
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            #CHECK LEFT ELEMENT IS MUST SMALLER THAN RIGHT THEN
            if nums[mid]<nums[mid+1]:
                left=mid+1
            #CHECK IF LEFT IS LARGER THEN
            if nums[mid]>nums[mid+1]:
                right=mid
        return left
obj=Solution()
nums=[1,2,3,4,3]
print(obj.findPeakElement(nums))
        