#COUNT GOOD NUMBERS
class Solution:
    MOD=10**9+7
    #BINARY EXPONENTIATION RECURSION
    def power(self,base,exp):
        #BASE CASE
        if exp==0:
            return 1
        #HANDLE NEGATIVE NUMBER
        if exp<0:
            return 1/self.power(base,-exp)
        #RECURSIVE CASE
        half=self.power(base,exp//2)
        #EVEN POWER
        if exp%2==0:
            return (half*half)%self.MOD
        #ODD POWER
        else:
            return (base*half*half)%self.MOD
    def countGoodNumbers(self, n: int) -> int:
        #EDGE CASE
        if n<=0:
            return 0
        #COUNT EVEN POSITIONS
        even_count=(n+1)//2
        #COUNT ODD POSITIONS
        odd_count=n//2
        #CALCULATE EVEN POSITIONS
        even_pos=self.power(5,even_count)
        #CALCULATE ODD POSITIONS
        odd_pos=self.power(4,odd_count)
        #TOTAL GOOD NUMBERS
        return (even_pos*odd_pos)%self.MOD
obj=Solution()
print(obj.countGoodNumbers(4))