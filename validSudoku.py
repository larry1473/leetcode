from collections import defaultdict
def isValidSudoku(board):
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                if(board[r][c] == "."):
                    continue
                if (board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r//3,c//3)]):
                    return False
                else:
                    col[c].add(board[r][c]) 
                    row[r].add(board[r][c])
                    square[(r//3,c//3)].add(board[r][c])
        return True