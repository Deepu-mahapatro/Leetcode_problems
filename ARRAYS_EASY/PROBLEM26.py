from typing import List

class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:

        # Edge case
        if len(nums) == 0:
            return 0

        # First element is always unique
        k = 1

        # Traverse array from second element
        for i in range(1, len(nums)):

            # If current element is different from previous
            if nums[i] != nums[i - 1]:

                # Store unique element
                nums[k] = nums[i]

                # Move unique position
                k += 1

        return k


# Input array
nums = [0,0,1,1,1,2,2,3,3,4]

# Create object
obj = Solution()

# Call function
k = obj.removeDuplicates(nums)

# Print result
print("Number of unique elements:", k)

print("Array after removing duplicates:")

for i in range(k):
    print(nums[i], end=" ")