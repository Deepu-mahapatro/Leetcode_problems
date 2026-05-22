from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #EDGE CASE IF ARR IS EMPTY
        if not  nums:
            return -1
        result=0
        for num in nums:
            #LOGIC OF XOR:A^A=0 AND A^0=A
            result^=num
        return result
obj=Solution()
answer=obj.singleNumber([1,2,3,3,2])
print(answer)