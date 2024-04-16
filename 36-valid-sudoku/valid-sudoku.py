class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value != '.':
                    res += [(i, value), (value, j), (i//3, j//3, value)]
        
        return len(res) == len(set(res))