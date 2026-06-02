#POWER(X,N) POWER FUNCTION
from typing import List
class Solution:
    def myPow(self, x: float, n: int) -> float:
        #BASE CASE
        if n==0:
            return 1
        #HANDLE NEGATIVE NUMBER
        if n<0:
            return 1/self.myPow(x,-n)
        #HALF THE SOLUTION
        half=self.myPow(x,n//2)
        #EVEN POWER
        if n%2==0:
            return half*half
        #ODD POWER
        else:
            return x*half*half
obj=Solution()
print(obj.myPow(2,3))