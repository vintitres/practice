class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        q = deque([0])
        while len(q) > 0:
            room = q.pop()
            if room in visited:
                continue
            visited.add(room)
            for key in rooms[room]:
                if key in visited:
                    continue
                q.append(key)
        return len(visited) == len(rooms)

        
