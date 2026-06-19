#FIND FIRST AND LAST POSITION OF ELEMENT IN SORTED ARRAY

from typing import List
class Solution:
    def first_occurence(self,nums,target):
        left=0
        right=len(nums)-1
        ans=-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                ans=mid
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return ans
    def last_occurence(self,nums,target):
        left=0
        right=len(nums)-1
        ans=-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                ans=mid
                left=mid+1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return ans
    def searchRange(self,nums,target):
        if not nums:
            return [-1,-1]
        first=self.first_occurence(nums,target)
        last=self.last_occurence(nums,target)
        return [first,last]
obj=Solution()
nums=[1,2,2,2,3,4]
target=2
print(obj.searchRange(nums,target))