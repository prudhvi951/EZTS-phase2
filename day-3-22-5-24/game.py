def numIslands(grid):
    if not grid:
        return 0

    def dfs(grid, i, j):
        # Check boundaries and if the cell is water ('0')
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        
        # Mark the cell as visited by setting it to '0'
        grid[i][j] = '0'
        
        # Visit all neighboring cells (up, down, left, right)
        dfs(grid, i + 1, j)
        dfs(grid, i - 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                dfs(grid, i, j)
    
    return count

# Define the grid
grid = [
    ['1', '1', '0', '1'],
    ['0', '0', '0', '1'],
    ['1', '0', '0', '1'],
    ['0', '1', '0', '1']
]

# Call the function and print the result
print(numIslands(grid))  # Output: 4
