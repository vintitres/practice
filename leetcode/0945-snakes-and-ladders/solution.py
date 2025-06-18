from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        flat_board = [-1]
        flip = False
        for row in reversed(board):
            if not flip:
                flat_board += row
            else:
                flat_board += reversed(row)
            flip = not flip
        board = flat_board
        print(board)
        n = len(board)
        seen = [False] * n
        queue = deque()
        queue.append((1, 0))
        while queue:
            curr, rolls = queue.popleft()
            print(curr, n)
            for next_pos in range(curr + 1, min(curr + 6, n - 1) + 1):
                print(next_pos)
                next_pos = board[next_pos] if board[next_pos] != -1 else next_pos
                if next_pos == n - 1:
                    return rolls + 1
                if not seen[next_pos]:
                    seen[next_pos] = True
                    queue.append((next_pos, rolls + 1))
        return -1
        
        
