#MAJORITY ELEMENT-I

#USING BOYER MOORE VOTING ALGORITHM
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #EDGE CASE
        if not nums:
            return []
        candidate=None
        count=0
        for num in nums:
            #NO ACTIVE CANDIDATE
            if count==0:
                candidate=num
            #SAME AS CANDIDATE
            if num==candidate:
                count+=1
            #DIFFERENT ELEMENT
            else:
                count-=1
        return candidate
obj=Solution()
nums=[3,2,3]
print(obj.majorityElement(nums))

#USING HASH MAP METHOD
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #EDGE CASE
        if not nums:
            return []
        freq={}
        n=len(nums)
        #BUILD FREQUENCY
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        #FIND MAJORITY ELEMENT
        for num,count in freq.items():
            if count>n//2:
                return num
obj=Solution()
nums=[3,2,3]
print(obj.majorityElement(nums))