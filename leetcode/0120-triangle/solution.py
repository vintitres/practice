class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        INF = 10 ** 7
        last_row_min = triangle[0]
        for row in triangle[1:]:
            next_last_row_min = []
            for i, v in enumerate(row):
                next_last_row_min.append(v + min(last_row_min[i] if i < len(last_row_min) else INF, last_row_min[i - 1] if i > 0 else INF))
            last_row_min = next_last_row_min
        return min(last_row_min)


        
