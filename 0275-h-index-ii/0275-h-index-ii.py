class Solution(object):
    def hIndex(self, citations):
        lo,hi = 0,len(citations)-1
        n=len(citations)
        if n == 0:
            return 0
        while lo <= hi :
            mid = lo +(hi-lo)//2
            if citations[mid] == n-mid :
                return citations[mid]
            elif citations[mid] > n-mid :
                hi = mid -1 
            else:
                lo=mid+1

        return n - lo


        """
        :type citations: List[int]
        :rtype: int
        """
        