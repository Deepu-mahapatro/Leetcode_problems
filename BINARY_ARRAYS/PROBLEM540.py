#SINGLE ELEMENT IN SORTED ARRAY

from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            #CHECK MID IS ODD OR EVEN
            if mid%2==1:
                mid-=1
            #CHECK THE PAIR (IF PAIR MOVE LEFT)
            if nums[mid]==nums[mid+1]:
                left=mid+2
            #IF NOT PAIR (SINGLE ELEMENT)
            else:
                right=mid
        return nums[right]
obj=Solution()
nums=[1,1,2,2,3,4,4]
print(obj.singleNonDuplicate(nums))