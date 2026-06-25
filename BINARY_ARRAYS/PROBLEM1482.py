#MINIMUM DAYS TO MAKE M BOUQUETS

#USING BINARY SEARCH METHOD
from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        #EDGE CASE:
        #IF TOTAL FLOWERS NEEDED IS MORE THAN AVAILABLE FLOWERS(IMPOSSIBLE)
        if m*k>len(bloomDay):
            return -1
        #BINARY SEARCH RANGE
        left=min(bloomDay)
        right=max(bloomDay)
        answer=-1
        while left<=right:
            mid=(left+right)//2
            #CHECK IF MID DAY IS POSSIBLE
            bouquets=0
            flowers=0
            for bloom in bloomDay:
                #FLOWER HAS BLOOMED
                if bloom<=mid:
                    flowers+=1
                    #ENOUGH ADJACENT FLOWERS
                    if flowers==k:
                        bouquets+=1
                        #FLOWERS ARE USED
                        flowers=0
                else:
                    #ADJACENT BREAKS
                    flowers=0
            #BINARY SEARCH DECISION
            if bouquets>=m:
                #STORE POSSIBLE ANSWER
                answer=mid
                #SEARCH FOR A SMALLER DAY
                right=mid-1
            else:
                #NEED TO AIT LONGER
                left=mid+1
        return answer
obj=Solution()
bloomDay=[1,10,3,10,2]
m=3
k=1
print(obj.minDays(bloomDay,m,k))