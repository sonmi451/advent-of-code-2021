def read_datafile(filepath):
    with open(filepath) as file:
        data = [line.strip() for line in file]
    return data
