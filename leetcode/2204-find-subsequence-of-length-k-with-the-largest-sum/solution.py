class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return 0
        heap = []
        for i, num in enumerate(nums):
            if len(heap) < k:
                heapq.heappush(heap, (num, i))
            elif heap[0][0] < num:
                heapq.heappushpop(heap, (num, i))
        return [n for n, _ in sorted(heap, key=lambda tup: tup[1])]
            

        
