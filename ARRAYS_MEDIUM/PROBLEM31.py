
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        #EDGE CASE: EMPTY OR SINGLE ELEMENT
        if len(nums) <= 1:
            return

        n = len(nums)

        #STEP 1: FIND PIVOT
        #FIRST INDEX FROM RIGHT WHERE nums[i] < nums[i+1]
        pivot = -1

        for i in range(n - 2, -1, -1):

            if nums[i] < nums[i + 1]:
                pivot = i
                break

        #EDGE CASE:
        #ARRAY IS IN DESCENDING ORDER
        #EXAMPLE: [3,2,1]
        if pivot == -1:
            nums.reverse()
            return

        #STEP 2: FIND NEXT GREATER ELEMENT FROM RIGHT
        for i in range(n - 1, pivot, -1):

            if nums[i] > nums[pivot]:

                #STEP 3: SWAP
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break

        #STEP 4: REVERSE THE SUFFIX
        nums[pivot + 1:] = reversed(nums[pivot + 1:])
obj=Solution()
nums=[1,2,3]
obj.nextPermutation(nums)
print(nums)