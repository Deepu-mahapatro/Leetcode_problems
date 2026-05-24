from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        #EDGE CASE 1: LESS THAN 2 ELEMENTS
        if n<2:
            return []
        #CHECK EVERY POSSIBLE PAIR
        for i in range(n):
            for j in range(i+1,n):
                #PAIR FOUND
                if nums[i]+nums[j]==target:
                    return [i,j]
        #EDGE CASE 2: NO PAIR FOUND
        return []
onj=Solution()
print(onj.twoSum([1,2,3,4,5],7))