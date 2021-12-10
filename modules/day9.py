from read_datafile import read_datafile

def get_map_data():
    filepath = './data/day9.txt'
    map_data = read_datafile(filepath)
    sensor_map = []
    for row in map_data:
        sensor_map.append([int(x) for x in row])
    return sensor_map

def find_low_points(sensor_map):
    length = len(sensor_map[0])
    height = len(sensor_map)
    outer_coord_x = length-1
    outer_coord_y = height-1

    low_points = []
    for y in range(0,height):
        for x in range(0,length):
            middle = sensor_map[y][x]
            # print(f'coords: {x, y} - value: {middle}')

            # corners
            # top left
            if x == 0 and y == 0:
                # print(f' > top left - {middle}')
                point_a = sensor_map[y+1][x]
                point_b = sensor_map[y][x+1]
                if middle < point_a and middle < point_b:
                    low_points.append(middle)

            # top right
            elif x == outer_coord_x and y == 0:
                # print(f' > top right - {middle}')
                point_a = sensor_map[y+1][x]
                point_b = sensor_map[y][x-1]
                if middle < point_a and middle < point_b:
                    low_points.append(middle)

            # bottom left
            elif x == 0 and y == outer_coord_y:
                # print(f'> bottom left - {middle}')
                point_a = sensor_map[y-1][x]
                point_b = sensor_map[y][x+1]
                if middle < point_a and middle < point_b:
                    low_points.append(middle)

            # bottom right
            elif x == outer_coord_x and y == outer_coord_y:
                # print(f'> bottom right - {middle}')
                point_a = sensor_map[y-1][x]
                point_b = sensor_map[y][x-1]
                if middle < point_a and middle < point_b:
                    low_points.append(middle)

            # top horizontal edge
            elif y == 0:
                # print(f' > top row - {middle}')
                south = sensor_map[y+1][x]
                east = sensor_map[y][x+1]
                west = sensor_map[y][x-1]
                if middle < south and middle < east and middle < west:
                    low_points.append(middle)

            # bottom horizontal edge
            elif y == outer_coord_y:
                # print(f' > bottom row - {middle}')
                north = sensor_map[y-1][x]
                east = sensor_map[y][x+1]
                west = sensor_map[y][x-1]
                if middle < north and middle < east and middle < west:
                    low_points.append(middle)

            # left edge
            elif x == 0:
                # print(f' > left col - {middle}')
                north = sensor_map[y-1][x]
                south = sensor_map[y+1][x]
                east = sensor_map[y][x+1]
                if middle < north and middle < south and middle < east:
                    low_points.append(middle)

            # right edge
            elif x == outer_coord_x:
                # print(f' > right col - {middle}')
                north = sensor_map[y-1][x]
                south = sensor_map[y+1][x]
                west = sensor_map[y][x-1]
                if middle < north and middle < south and middle < west:
                    low_points.append(middle)

            # not edges
            else:
                # print(f' > middle section - {middle}')
                north = sensor_map[y-1][x]
                south = sensor_map[y+1][x]
                east = sensor_map[y][x+1]
                west = sensor_map[y][x-1]
                if middle < north and middle < south and middle < east and middle < west:
                    low_points.append(middle)
    return low_points


def calculate_risk(input):
    risk = 0
    for x in input:
        risk += (1+x)
    return risk

sensor_map = get_map_data()
low_points = find_low_points(sensor_map)
print(low_points)
risk = calculate_risk(low_points)
print(risk)
