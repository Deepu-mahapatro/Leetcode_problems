#MAXIMUM POINTS YOU CAN OBTAIN FROM CARDS
from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        #TAKE ALL CARDS FORM LEFT INITIALLY
        curr_sum=sum(cardPoints[:k])
        ans=curr_sum
        #MOVE ALONG TEH ELEMENTS TO PROCESS THEM
        for i in range(1,k+1):
            #REMOVE ONE CARD FROM LEFT SIDE
            curr_sum-=cardPoints[k-i]
            #ADD ONE CARD FROM RIGHT SIDE
            curr_sum+=cardPoints[n-i]
            #UPDATE THE MAXIMUM SIZE
            ans=max(ans,curr_sum)
        return ans
obj=Solution()
cardPoints=[1,2,3,4,5,6,1]
k=3
print(obj.maxScore(cardPoints,k))