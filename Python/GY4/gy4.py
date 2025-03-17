def is_valid_sudoku(grid):
    if len(grid) != 9 or any(len(row) != 9 for row in grid):
        return False
    
    for row in grid:
        if len(set(row)) != 9 or any(cell < '1' or cell > '9' for cell in row):
            return False
    
    for col in range(9):
        column = [grid[row][col] for row in range(9)]
        if len(set(column)) != 9:
            return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_square = [grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if len(set(sub_square)) != 9:
                return False
    
    return True

grid = [
    "295743861",
    "431865927",
    "876192543",
    "387459216",
    "612387495",
    "549216738",
    "763524189",
    "928671354",
    "154938672"
]

if is_valid_sudoku(grid):
    print("Yes")
else:
    print("No")