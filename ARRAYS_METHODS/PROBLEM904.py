#FRUITS INTO BASKETS
from typing import List
class Solution:
    def totalFruit(self,fruits:List[int])->int:
        #EDGE CASE
        if not fruits:
            return 0
        left=0
        answer=0
        count={}
        n=len(fruits)
        for right in range(n):
            fruit=fruits[right]
            count[fruit]=count.get(fruit,0)+1
            while len(count)>2:
                left_fruit=fruits[left]
                count[left_fruit]-=1
                if count[left_fruit]==0:
                    del count[left_fruit]
                left+=1
            answer=max(answer,right-left+1)
        return answer
obj=Solution()
fruits=[1,2,1,2,3]
print(obj.totalFruit(fruits))