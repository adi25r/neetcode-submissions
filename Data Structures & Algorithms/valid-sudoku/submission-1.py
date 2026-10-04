class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(row: List[str]) -> bool:
            arr = [0] * 10
            for num in row:
                if num != ".":
                    arr[int(num)] += 1
            for i in range(1, 10):
                if arr[i] > 1:
                    return False
            return True

        
        def checkCol(board: List[List[str]], col_index: int) -> bool:
            arr = [0] * 10
            for i in range(9):
                num = board[i][col_index]
                if num != ".":
                    arr[int(num)] += 1

            for i in range(1, 10):
                if arr[i] > 1:
                    return False
            return True

        
        def checkSubBoxes(board: List[List[str]], top_row: int, top_col: int) -> bool:
            arr = [0] * 10
            for i in range(top_row, top_row + 3):
                for j in range(top_col, top_col + 3):
                    num = board[i][j]
                    if num != ".":
                        arr[int(num)] += 1

            for i in range(1, 10):
                if arr[i] > 1:
                    print(arr)
                    return False
            return True
        
        for i in range(9):
            if not checkRow(board[i]):
                print("failed row check")
                return False
            if not checkCol(board, i):
                print("failed col check")
                return False
            if not checkSubBoxes(board, 3* (i // 3), 3 * (i % 3)):
                print("failed subbox check on " + str(i // 3) + " and " + str(i % 3))
                return False
        
        return True

        