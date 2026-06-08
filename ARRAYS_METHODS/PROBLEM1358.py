#NUMBER OF SUBSTRINGS CONTAINING ALL THREE (A,B,C) CHARACTERS
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left=0
        n=len(s)
        count=0
        #FREQUENCY INTIALLY 
        freq={'a':0,'b':0,'c':0}
        #EXPAND WINDOW USING RIGHT POINTER
        for right in range(n):
            #ADD CURRENT CHARACTER TO WINDOW
            freq[s[right]]+=1
            #WINDOW CONTAIN ALL THREE CHARACTERS
            while freq['a']>0 and freq['b']>0 and freq['c']>0:
                #COUNT ALL VALID EXTENSIONS
                count+=n-right
                #SHRINK TEH WINDOW FROM LEFT
                freq[s[left]]-=1
                left+=1
        return count
obj=Solution()
s="abcabcabc"
print(obj.numberOfSubstrings(s))