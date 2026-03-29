class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # for storing the rows
        cols = defaultdict(set) # for storing the cols
        subMatrix = defaultdict(set) # for sub 3x3 squares

        for r in range(9):
            for c in range(9):
                # check if the cell is empty:
                if board[r][c] == ".": continue

                # check if the number is already present in the map
                if (board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (board[r][c] in subMatrix[(r // 3, c // 3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                subMatrix[(r // 3, c // 3)].add(board[r][c])
        return True
                