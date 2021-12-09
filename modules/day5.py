from read_datafile import read_sequence, read_scoreboards


def graph_lines(input):
    grid = [[0 for x in range (0,9)] for x in range(0,9)]
    # print(grid)
    for line in input:
        x, y = line.split(' -> ')
        x1, y1 = x.split(',')
        x2, y2 = y.split(',')
        print(x1, x2, y1, y2)
        # horizontal
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        if y1 == y2:
            x_diff = x2 - x1
            y_diff = y2 - y1
            grid[x1][x1:x2] = [1 for x in range(x1,x2-1)]
            # print(grid[x1][x1:x2])
            # print([1 for x in range(x1,x2-1)])
        # vertical

    print(grid)
    return grid
