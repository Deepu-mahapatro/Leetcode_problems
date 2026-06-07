#COUNT NICE SUB ARRAYS
from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #STORE FREQUENCT OF ADD-PREFIX COUNTS
        freq={0:1}
        prefix=0
        answer=0
        for num in nums:
            #ODD NUMBER FOUND
            if num%2==1:
                prefix+=1
            #COUNT VALID PREVIOUS PREFIXES
            answer+=freq.get(prefix-k,0)
            #STORE CURRENT PREFIX
            freq[prefix]=freq.get(prefix,0)+1
        return answer
obj=Solution()
nums=[1,2,1]
k=2
print(obj.numberOfSubarrays(nums,k))