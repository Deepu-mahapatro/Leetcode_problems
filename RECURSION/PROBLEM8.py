from typing import List
class Solution:
    def myAtoi(self, s: str) -> int:
        #REMOVE SPACES
        s=s.strip()
        #EDGE CASE: EMPTY STRING
        if not s :
            return 0
        #ASSUME POSITIVE NUMBER
        sign=1
        if s[0]=='-':
            sign=-1
            s=s[1:]
        elif s[0]=='+':
            s=s[1:]
        #EDGE CASE "+" OR "-"
        if not s :
            return 0
        INT_MAX=2147483647
        INT_MIN=-2147483648
        def Atoi(index,num):
            #BASE CASE
            if index>=len(s) or not s[index].isdigit():
                return num
            #BUILD NUMBER
            num=num*10+int(s[index])
            #CHECK OVERFLOW
            if sign==1 and num>INT_MAX:
                return INT_MAX
            if sign==-1 and -num<INT_MIN:
                return abs(INT_MIN)
            return Atoi(index+1,num)
        result=sign*Atoi(0,0)
        if result>INT_MAX:
            return INT_MAX
        if result<INT_MIN:
            return INT_MIN
        return result
obj=Solution()
print(obj.myAtoi("123ABC"))