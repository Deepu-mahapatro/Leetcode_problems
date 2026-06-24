#KOKO EATING BANANAS

#USING BINARY SEARCH METHOD
from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return 0
        #MINIMUM POSSIBLE SPEED
        left=1
        #MAXIMUM POSSIBLE SPEED
        right=max(piles)
        #CONDITION TO END LOOP
        while left<=right:
            #GUESS A SPEED
            mid =(left+right)//2
            #CALCULATE TOTAL HOURS NEEDED
            hours=0
            for pile in piles:
                #CEIL DIVISION
                hours+=math.ceil(pile/mid)
            #IF KOKO CAN FINISH WITHIN 1 HOUR
            if hours<=h:
                #MINIMUM SPEED MAY BE ON LEFT SIDE SO MOVE RIGHT
                right=mid-1
            else:
                #MID IS TOO LOW SEARCH ON RIGHT SIDE SO MOVE LEFT
                left=mid+1
        return left
obj=Solution()
piles=[3,6,7,11]
h=8
print(obj.minEatingSpeed(piles,h))