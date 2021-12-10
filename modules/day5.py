from read_datafile import read_datafile

def get_map_data():
    filepath = './data/day5.txt'
    map_data = read_datafile(filepath)
    return map_data

def graph_lines(input, size, debug=False):
    grid = [[0 for x in range (0,size)] for x in range(0,size)]
    vertical_lines = 0
    horizontal_lines = 0
    diagonal_lines = 0
    for line in input:
        x, y = line.split(' -> ')
        x1, y1 = x.split(',')
        x2, y2 = y.split(',')
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        x_diff = x2 - x1
        y_diff = y2 - y1

        # horizontal
        if y_diff == 0:
            horizontal_lines += 1
            if x1 < x2:
                start_x = x1
                end_x = x2
            else:
                start_x = x2
                end_x = x1

            if debug:
                print(f"## COORDS #################\n{x1, x2, y1, y2}")
                print(f"## ROW: {y1}")
                print(f"## X SPACES: {[x for x in range(start_x, end_x+1)]}\n")

            grid[y1][start_x:end_x+1] = [x+1 for x in grid[y1][start_x:end_x+1]]

        # vertical
        elif x_diff == 0:
            vertical_lines += 1
            if y1 < y2:
                start_y = y1
                end_y = y2
            else:
                start_y = y2
                end_y = y1

            y_items = [x for x in range(start_y, end_y+1)]

            if debug:
                print(f"## COORDS #################\n{x1, x2, y1, y2}")
                print(f"## COL: {x1}")
                print(f"## Y SPACES: {y_items}\n")

            for item in y_items:
                grid[item][x1] = grid[item][x1]+1

        # diagonal
        elif int(x_diff / y_diff) in [1, -1]:
            diagonal_lines += 1

            if x1 < x2:
                x_coords = [x for x in range(x1, x2+1)]
            else:
                x_coords = [x for x in range(x1, x2-1, -1)]

            if y1 < y2:
                y_coords = [y for y in range(y1, y2+1)]
            else:
                y_coords = [y for y in range(y1, y2-1, -1)]

            coords = dict(zip(y_coords, x_coords))

            if debug:
                print(f"## COORDS #################\n{x1, x2, y1, y2}")
                print(f"## GRADIENT: {int(x_diff / y_diff)}")
                print(f"## X SPACES: {x_coords}")
                print(f"## Y SPACES: {y_coords}\n")

            for x, y in coords.items():
                grid[x][y] = grid[x][y]+1

    if debug:
        print(f'Horizontal Lines: {horizontal_lines}')
        print(f'Vertical Lines: {vertical_lines}')
        print(f'Diagonal Lines: {diagonal_lines}')

    flat_grid = []
    for row in grid:
        if debug:
            print(row)
        flat_grid = flat_grid + row
    return flat_grid

def count_peaks(flat_grid):
    peaks = [x for x in flat_grid if x > 1]
    return len(peaks)

input = get_map_data()
flat_output = graph_lines(input, 1000)
num_peaks = count_peaks(flat_output)
print(num_peaks)
