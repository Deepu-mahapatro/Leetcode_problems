#REARRANGE ELEMENTS BY SIGN

from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        zeros=[]
        for num in nums:
            if num>0:
                pos.append(num)
            elif num<0:
                neg.append(num)
            else:
                zeros.append(num)
        result=[]
        i=0
        j=0
        while i<len(pos) and j<len(neg):
            result.append(pos[i])
            result.append(neg[j])
            i+=1
            j+=1
        while i<len(pos):
            result.append(pos[i])
            i+=1
        while j<len(neg):
            result.append(neg[j])
            j+=1
        result.extend(zeros)
        return result
obj=Solution()
nums=[1,2,3,4,-5,-6,-7,0,0,0,3,-5,0]
print(obj.rearrangeArray(nums))