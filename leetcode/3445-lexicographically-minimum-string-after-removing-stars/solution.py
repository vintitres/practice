import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        char_pos = []
        for i, c in enumerate(s):
            if c == '*':
                heapq.heappop(char_pos)
            else:
                heapq.heappush(char_pos, (c,  -i))
        pos_char = []
        while char_pos:
            c, i = heapq.heappop(char_pos)
            pos_char.append((-i, c))
        return ''.join(c for _, c in sorted(pos_char))
    

        
