#BINARY SUB ARRAY WITH SUM
from typing import List
class Solution:
    def numSub_arraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_count={0:1}
        curr_sum=0
        count=0
        for num in nums:
            curr_sum+=num
            required_prefix=curr_sum-goal
            if required_prefix in prefix_count:
                count+=prefix_count[required_prefix]
            prefix_count[curr_sum]=prefix_count.get(curr_sum,0)+1
        return count
obj=Solution()
nums=[1,1,0]
goal=2
print(obj.numSub_arraysWithSum(nums, goal))