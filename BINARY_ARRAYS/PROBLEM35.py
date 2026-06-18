#SEARCH INSERT POSITION
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return left
obj=Solution()
nums=[1,3,4,5]
target=2
print(obj.searchInsert(nums,target))