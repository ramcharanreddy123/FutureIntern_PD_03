grid = [[' ' for _ in range(3)] for _ in range(3)]

def draw_grid(grid):
    for row in grid:
        print(' | '.join(row))
        print('---------')

def check_win(grid):
    for row in grid:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True
    for col in range(len(grid)):
        check = []
        for row in grid:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != ' ':
            return True
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != ' ':
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != ' ':
        return True
    return False

def check_draw(grid):
    for row in grid:
        if ' ' in row:
            return False
    return True

current_player = 'X'
while True:
    draw_grid(grid)
    print(f"Player {current_player}'s turn")
    move = input("Enter your move (1-9): ")
    move = int(move) - 1
    row = move // 3
    col = move % 3
    if grid[row][col] != ' ':
        print("Invalid move, try again.")
        continue
    grid[row][col] = current_player
    if check_win(grid):
        draw_grid(grid)
        print(f"Player {current_player} wins!")
        break
    if check_draw(grid):
        draw_grid(grid)
        print("It's a draw!")
        break
    current_player = 'O' if current_player == 'X' else 'X'