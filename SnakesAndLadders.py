# Time is O(n^2)  as going through each and every cell in the snakes and ladders board
# The space is also same as using newBoard which is the size O(n^2)

# The intuition here is to flatten the array and then do a BFS on it and for every size, we update the move.
# If we are able to reach the index which is n^2 we can return the moves result otherwise return -1

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        newBoard = [-1] * (n * n)
        r = n - 1
        c = 0
        newBoard[0] = -1
        flag = True
        for i in range(1, n * n):
            if flag:
                c += 1
                if c >= n:
                    r -= 1
                    c -= 1
                    flag = False
            else:
                c -= 1
                if c < 0:
                    r -= 1
                    c += 1
                    flag = True
            if board[r][c] == -1:
                newBoard[i] = -1
            else:
                newBoard[i] = board[r][c] - 1
        queue = deque()
        queue.append(0)
        newBoard[0] = -2
        moves = 0
        while queue:
            size = len(queue)
            for i in range(size):
                idx = queue.popleft()
                for k in range(1, 7):  # for dice roll
                    newIdx = idx + k
                    if newBoard[newIdx] == n * n - 1 or newIdx == n * n - 1:
                        return moves + 1
                    if newBoard[newIdx] != -2:
                        if newBoard[newIdx] == -1:
                            queue.append(newIdx)
                        else:
                            queue.append(newBoard[newIdx])
                        newBoard[newIdx] = -2
            moves += 1

        return -1