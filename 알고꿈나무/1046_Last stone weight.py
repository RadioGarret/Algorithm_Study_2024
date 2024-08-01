class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -stone for stone in stones] # max heap
        # We use the negative on the heapq module to simulate the maximum heap
        heapq.heapify(stones)
        while len(stones) > 1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            # repeatedly taking out the maximum 
            if first != second:
                heapq.heappush(stones, -abs(first -second))
   # the difference is pushed back into the heap 
        return -stones[0] if stones else 0