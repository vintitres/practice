class Solution:
    def hIndex(self, citations: List[int]) -> int:
        begin = 0
        end = len(citations)
        while begin < end:
            mid = int((begin + end + 1) / 2)
            if len(list(filter(lambda x: x >= mid, citations))) < mid:
                end = mid - 1
            else:
                begin = mid
        return begin

        
