def gridChallenge(grid):
    for i in range(0,len(grid)-1):
        for j in range(len(grid[i])):
            if sorted(grid[i])[j]>sorted(grid[i+1])[j]:
                return 'NO'
    return 'YES'