#LONGEST REPEATING CHARACTER REPLACEMENT
class Solution:
    def characterReplacement(self,s:str,k:int)->int:
        #EDGE CASE
        if not s:
            return ""
        #SET VALID INPUTS
        left=0
        n=len(s)
        max_freq=0
        freq={}
        result=0
        #EXPAND THE WINDOW USING RIGHT POINTER
        for right in range(n):
            #CURRENT CHARACTER
            char=s[right]
            #COUNT THE FREQUENCY OF THE CHARACTER
            freq[char]=freq.get(char,0)+1
            #UPDATE THE AMX_FREQUENCY
            max_freq=max(max_freq,freq[char])
            #CURRENT WINDOW LENGTH
            window_size=right-left+1
            #CONDITION APPLIED HERE
            while window_size-max_freq>k:
                #REMOVE THE FREQUENCY OF LEFT CHARACTER
                freq[s[left]]-=1
                #MOVE THE LEFT POINTER FORWARD
                left+=1
                #UPDATE THE CURRENT WINDOW SIZE
                window_size=right-left+1
            #UPDATE THE THE RESULT
            result=max(result,window_size)
        return result
obj=Solution()
s="AAABC"
k=2
print(obj.characterReplacement(s,k))