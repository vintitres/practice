class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connections_dict = {i: [] for i in range(n)}
        for city1, city2 in connections:
            connections_dict[city1].append((city2, 1))
            connections_dict[city2].append((city1, 0))
        seen = set([0])
        q = deque()
        q.append(0)
        rev_used = 0
        while len(q) > 0:
            city = q.popleft()
            for (next_city, direction) in connections_dict[city]:
                if next_city not in seen:
                    seen.add(next_city)
                    q.append(next_city)
                    rev_used += direction
        return rev_used
        
