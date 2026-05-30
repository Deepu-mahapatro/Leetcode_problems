from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #EDGE CASE
        if not nums:
            return 0
        num_set=set(nums)
        longest=0
        for num in num_set:
            #CHECK IF CURRENT IS THE START OF A SEQUENCE
            if num-1 not in num_set:
                current=num
                length=1
                #EXPAND TEH SEQUENCE
                while current+1 in num_set:
                    current+=1
                    length+=1
                longest=max(longest,length)
        return longest
obj=Solution()
nums=[1,200,45,3,23,2,5,56,4]
print(obj.longestConsecutive(nums))