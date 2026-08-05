import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[stone*-1 for stone in stones]

        heapq.heapify(stones)
        while len(stones)>=2:
            first=abs(heapq.heappop(stones))
            second=abs(heapq.heappop(stones))
            diff=first-second
            if diff==0:
                continue
            heapq.heappush(stones, -1*diff)
        if len(stones)==0:
            return 0
        else:
            return abs(stones[0])



        
       



        