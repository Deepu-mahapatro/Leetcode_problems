#KTH MISSING POSITIVE NUMBER

from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        #BINARY SEARCH ON THE ARRAY
        left=0
        right=len(arr)-1
        while left<=right:
            mid=(left+right)//2
            #NUMBER OF MISSING POSITIVE INTEGERS BEFORE ARR[MID]
            #FORMULA:
            #MISSING=ACTUAL VALUE-EXPECTED VALUE
            #EXPECTED VALUE AT INDEX MID=MID+1
            missing=arr[mid]-(mid+1)
            if missing<k:
                #NOT ENOUGH MISSING NUMBERS YET
                #THE KTH MISSING NUMBER IS ON THE RIGHT
                left=mid+1
            else:
                #WE HAVE ALREADY FOUND K OR MORE MISSING NUMBERS
                #SEARCH ON THE LEFT TO FIND THE FIRST SUCH POSITION 
                right=mid-1
        #AFTER BINARY SEARCH :
        #LEFT=NUMBER OF ARRAY ELEMENTS BEFORE THE K TH MISSING NUMBER
        #THEREFORE,ANSWER=K+LEFT
        return left+k
obj=Solution()
arr=[2,3,4,7,11]
k=5
print(obj.findKthPositive(arr,k))