from read_datafile import read_datafile

def get_course_data():
    filepath = './data/day2.txt'
    course_data = read_datafile(filepath)
    return course_data

def position_product(course_data):
    pitch = 0
    distance = 0
    for datum in course_data:
        vector = datum.split(' ')
        direction = vector[0]
        size = vector[1]

        if direction == 'up':
            pitch -= int(size)
        elif direction == 'down':
            pitch += int(size)
        elif direction == 'forward':
            distance += int(size)

    product = pitch * distance
    return product

data = get_course_data()
product = position_product(data)
print(">", product)
