import os


def numCells(grid):
    res = 0
    for i in range(len(grid)):
        for k in range(len(grid[0])):
            val = grid[i][k]
            flag = 1
            for ii in range(max(0, i - 1), min(len(grid), i + 2)):
                for kk in range(max(0, k - 1), min(len(grid[0]), k + 2)):
                    if (ii, kk) != (i, k) and val <= grid[ii][kk]:
                        flag = 0
                        break
                if flag == 0:
                    break
            else:
                res += 1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
