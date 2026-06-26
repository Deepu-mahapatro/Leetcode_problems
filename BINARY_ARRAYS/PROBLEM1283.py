#FIND SMALLEST DIVISOR

#USING BINARY SEARCH METHOD (NO MATH OPERATION)
from typing import List
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        #EDGE CASE
        if not nums:
            return 0
        #SEARCH SPACE FOR DIVISORS
        l=1
        r=max(nums)
        #AS LAST IS VALID DIVISOR ALWAYS
        ans=r
        #BINARY SEARCH
        while l<=r:
            mid=(l+r)//2
            #CALCULATE TOTAL 
            total=0
            for num in nums:
                #USING CEILING METHOD (NO MATH)
                total+=(num+mid-1)//mid
            #IF CURRENT DIVISOR SATISFIES THE THRESHOLD
            if total<=threshold:
                #STORE THE CURRENT DIVISOR
                ans=mid
                #TRY TO FIND SMALLEST DIVISOR AT LEFT SIDE
                r=mid-1
            else:
                #DIVISOR IS TOO SMALL INCREASE IT SEARCH ON RIGHT SIDE
                    l=mid+1
        return ans
obj=Solution()
nums=[1,2,5,9]
threshold=6
print(obj.smallestDivisor(nums,threshold))

#USING BINARY METHOD ( MATH OPERATION)
from typing import List
import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        #EDGE CASE
        if not nums:
            return 0
        #SEARCH SPACE FOR DIVISORS
        l=1
        r=max(nums)
        #AS LAST IS VALID DIVISOR ALWAYS
        ans=r
        #BINARY SEARCH
        while l<=r:
            mid=(l+r)//2
            #CALCULATE TOTAL 
            total=0
            for num in nums:
                #USING CEILING METHOD (NO MATH)
                total+=math.ceil(num/mid)
            #IF CURRENT DIVISOR SATISFIES THE THRESHOLD
            if total<=threshold:
                #STORE THE CURRENT DIVISOR
                ans=mid
                #TRY TO FIND SMALLEST DIVISOR AT LEFT SIDE
                r=mid-1
            else:
                #DIVISOR IS TOO SMALL INCREASE IT SEARCH ON RIGHT SIDE
                    l=mid+1
        return ans
obj=Solution()
nums=[1,2,5,9]
threshold=6
print(obj.smallestDivisor(nums,threshold))