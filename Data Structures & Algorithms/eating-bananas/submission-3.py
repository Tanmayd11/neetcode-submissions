class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        while l<r:
          k=(l+r)//2
          total=sum((x+k-1)//k for x in piles)
          if total >h:
            l=k+1
          else :
            r=k
        return l