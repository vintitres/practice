class Solution:
    def hIndex(self, citations: List[int]) -> int:
        begin = 0
        citations.sort()
        end = len(citations)
        while begin < end:
            mid = int((begin + end + 1) / 2)
            if len(citations) - bisect_left(citations, mid) < mid:
                end = mid - 1
            else:
                begin = mid
        return begin

        
