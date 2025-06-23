class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        INF = 10 ** 7
        last_row = triangle[0]
        row = 1
        while row < len(triangle):
            next_last_row = []
            for i, v in enumerate(triangle[row]):
                next_last_row.append(v + min(last_row[i] if i < len(last_row) else INF, last_row[i - 1] if i > 0 else INF))
            last_row = next_last_row
            row += 1
        return min(last_row)


        
