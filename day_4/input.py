def main():
    with open("input.txt", "r") as f:
        lines = [l.rstrip() for l in f]
        grid = create_grid(lines)
        return calculate_rolls(grid)



    return grid

def create_grid(lines):
    grid = []

    for l in lines:
        row = [c for c in l]
        grid.append(row)
    
    return grid

def calculate_rolls(grid):
    result = 0
    rows = len(grid)
    cols = len(grid[0])

    while True:
        removed = 0

        for r in range(rows):
            for c in range(cols):
                adj_rolls = 0
                if grid[r][c] == "@":
                    adj_rolls += count_x(grid, cols, r, c)
                    adj_rolls += count_y(grid, rows, r, c)
                    adj_rolls += count_diagonal_main(grid, rows, cols, r, c)
                    adj_rolls += count_diagonal_anti(grid, rows, cols, r, c)
                    if adj_rolls < 4:
                        grid[r][c] = "x"
                        removed += 1
        
        result += removed
        if removed == 0:
            break
    
    return result


def count_x(grid, cols, r, c):
    result = 0

    tc = c - 1
    if tc >= 0 and grid[r][tc] == "@":
        result += 1
    
    tc = c + 1
    if tc < cols and grid[r][tc] == "@":
        result += 1

    return result

def count_y(grid, rows, r, c):
    result = 0

    tr = r - 1
    if tr >= 0 and grid[tr][c] == "@":
        result += 1
    
    tr = r + 1
    if tr < rows and grid[tr][c] == "@":
        result += 1

    return result

def count_diagonal_main(grid, rows, cols, r, c):
    result = 0
    
    tr, tc = r-1, c-1
    if tr >= 0 and tc >= 0 and grid[tr][tc] == "@":
        result += 1
    
    tr, tc = r+1, c+1
    if tr < rows and tc < cols and grid[tr][tc] == "@":
        result += 1
    
    return result

def count_diagonal_anti(grid, rows, cols, r, c):
    result = 0

    tr, tc = r-1, c+1
    if tr >= 0 and tc < cols and grid[tr][tc] == "@":
        result += 1

    tr, tc = r+1, c-1
    if tr < rows and tc >= 0 and grid[tr][tc] == "@":
        result += 1

    return result

if __name__ == "__main__":
    result = main()
    print(result)
