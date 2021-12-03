from read_datafile import read_datafile

def get_course_data():
    filepath = './data/day2.txt'
    course_data = read_datafile(filepath)
    return course_data

def crude_position_product(course_data):
    depth = 0
    horizontal_position = 0
    for datum in course_data:
        vector = datum.split(' ')
        direction = vector[0]
        size = int(vector[1])

        if direction == 'up':
            depth -= size
        elif direction == 'down':
            depth += size
        elif direction == 'forward':
            horizontal_position += size

    product = depth * horizontal_position
    return product


def position_product(course_data):
    depth = 0
    horizontal_position = 0
    aim = 0
    for datum in course_data:
        vector = datum.split(' ')
        direction = vector[0]
        size = int(vector[1])

        if direction == 'up':
            aim -= size
        elif direction == 'down':
            aim += size
        elif direction == 'forward':
            horizontal_position += size
            increase = aim*size
            depth += increase

    product = depth * horizontal_position
    return product

data = get_course_data()
product = position_product(data)
print(">", product)
