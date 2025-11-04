# Time complexity is O(m*n) as doing a BFS and traversing through each row and col
# Space is also O(m*n) using queue data structure

# The intuition is to do a BFS from the clicked row and col and then check the neighbors, if they don't have a mine we can process them and update
# the cell to "B". Otherwise we don't process them.

class Solution:
    def updateBoardBFS(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        dirs = [(0,1), (1,0), (-1,0), (0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]
        queue = deque()
        queue.append((click[0], click[1]))
        board[click[0]][click[1]] = "B"
        while queue:
            r, c = queue.popleft()
            minesCnt = self.getMinesCount(board, r, c, dirs)
            if minesCnt == 0:
                for dx, dy in dirs:
                    nr = r + dx
                    nc = c + dy
                    if nr < 0 or nc < 0 or nr == m or nc == n or board[nr][nc] != 'E':
                        continue
                    board[nr][nc] = "B"
                    queue.append((nr,nc))
            else:
                board[r][c] = str(minesCnt)
        return board

    def getMinesCount(self, board, r, c, dirs):
        cnt = 0
        for dx, dy in dirs:
            nr = r + dx
            nc = c + dy
            if nr >= 0 and nc >= 0 and nr < len(board) and nc < len(board[0]) and board[nr][nc] == 'M':
                cnt += 1
        return cnt


    # The same can be solved using DFS as well as they are connected components. The time and space complexity remains the same as above.
    def updateBoardDFS(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        self.dfs(board, click[0], click[1], dirs)
        return board

    def dfs(self, board, r, c, dirs):
        # Base case
        if r < 0 or c < 0 or r == len(board) or c == len(board[0]) or board[r][c] != "E":
            return
        # Logic
        board[r][c] = "B"
        cnt = self.getMinesCount(board, r, c, dirs)
        if cnt == 0:
            for dx, dy in dirs:
                nr = r + dx
                nc = c + dy
                self.dfs(board, nr, nc, dirs)
        else:
            board[r][c] = str(cnt)

    def getMinesCount(self, board, r, c, dirs):
        cnt = 0
        for dx, dy in dirs:
            nr = r + dx
            nc = c + dy
            if nr >= 0 and nc >= 0 and nr < len(board) and nc < len(board[0]) and board[nr][nc] == 'M':
                cnt += 1
        return cnt