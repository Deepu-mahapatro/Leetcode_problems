#KADANES ALGORITHM ( MAXIMUM SUB ARRAY)

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #EDGE CASE
        if not nums:
            return 0
        current_sum=nums[0]
        max_sum=nums[0]
        for num in nums[1:]:
            #EITHER CONTINUE WITH OLD SUB ARRAY OR START FRESH
            current_sum=max(num,current_sum+num)
            #UPDATE THE ANSWER
            max_sum=max(max_sum,current_sum)
        return max_sum
obj=Solution()
nums=[-2,1,-3,4]
print(obj.maxSubArray(nums))