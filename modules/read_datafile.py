

def read_datafile(filepath):
    with open(filepath) as file:
        data = [line.strip() for line in file]
    return data


def read_sequence(filepath):
    with open(filepath) as file:
        data = [line.strip() for line in file]
        seq = data[0].split(',')
    return [int(x) for x in seq]


def read_scoreboards(filepath):
    data = []
    with open(filepath) as file:
        boards = []
        board = []
        for line in file:
            numbers = line.replace('  ', ' ').strip().split(' ')
            if len(numbers) != 1:
                board += [int(x) for x in numbers]
            else:
                boards.append(board)
                board = []

    return boards
