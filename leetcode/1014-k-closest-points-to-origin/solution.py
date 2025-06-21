import heapq
def dist(point: List[int]) -> float:
    x = point[0]
    y = point[1]
    return sqrt(x * x + y * y)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_points = []
        for point in points:
            d = dist(point)
            if len(closest_points) < k:
                heapq.heappush(closest_points, (-d, point))
            else:
                max_dist = -closest_points[0][0]
                if d < max_dist:
                    heapq.heappushpop(closest_points, (-d, point))
        return [point for _, point in closest_points]

        
