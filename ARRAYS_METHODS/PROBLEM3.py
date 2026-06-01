#LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #EDGE CASE:EMPTY STRING
        if not s:
            return 0
        left=0
        n=len(s)
        max_length=0
        seen=set()
        for right in range(n):
            #REMOVE DUPLICATES
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            #STORE CURRENT ELEMENT
            seen.add(s[right])
            #UPDATE THE MAX_LENGTH
            max_length=max(max_length,right-left+1)
        return max_length
obj=Solution()
print(obj.lengthOfLongestSubstring("abcabcbb"))