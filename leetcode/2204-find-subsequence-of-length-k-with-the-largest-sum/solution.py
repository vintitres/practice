class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return 0
        heap = []
        for i, num in enumerate(nums):
            if len(heap) < k:
                heapq.heappush(heap, (num, i))
            elif heap[0][0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, (num, i))
        return [nums[i] for i in sorted(i for _, i in heap)]
            

        
