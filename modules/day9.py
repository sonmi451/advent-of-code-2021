from read_datafile import read_sequence

def find_low_points(sensor_map):
    length = len(sensor_map[0])
    height = len(sensor_map)
    last_horizontal = length-2
    last_vertical = height-2

    print('## GRID')
    for y in sensor_map:
        print(y)
    print('#######')


    for y in range(0,height):

        for x in range(0,length):
            # print(f'Coords: {x, y}')
            # print(f'Value: {sensor_map[y][x]}')

            # Horizontal
            if x >= last_horizontal:
                continue
            else:
                point_a, point_b, point_c = int(sensor_map[y][x]),  int(sensor_map[y][x+1]), int(sensor_map[y][x+2])
                if point_b < point_a and point_b < point_c:
                    sensor_map[y][x] = 9
                    sensor_map[y][x+2] = 9

            # Vertical
            if y >= last_vertical:
                continue
            else:
                col_a, col_b, col_c = int(sensor_map[y][x]),  int(sensor_map[y+1][x]), int(sensor_map[y+2][x])
                if col_b < col_a and col_b < col_c:
                    sensor_map[y][x] = 9
                    sensor_map[y+2][x] = 9


    print('## NEW GRID')
    flat_grid = []
    for row in sensor_map:
        print(row)
        flat_grid = flat_grid + row
    print('## OUTPUT')
    output = [x for x in flat_grid if x != 9]
    print(output)
    print('###########')
    return output


def calculate_risk(input):
    risk = 0
    for x in input:
        risk += 1+x
    return risk
