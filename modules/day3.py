from read_datafile import read_datafile

def get_power_data():
    filepath = './data/day3.txt'
    diagnostic_report = read_datafile(filepath)
    return diagnostic_report

def power_consumption(diagnostic_report):
    data_length = len(diagnostic_report[0])
    half_report_length = int(len(diagnostic_report)/2)

    # Count the bitrate
    counts = [0 for x in range(0, data_length)]
    for line in diagnostic_report:
        data = [x for x in line]

        for bit in range(0, data_length):
            if data[bit] == '1':
                counts[bit] += 1

    # Find gamma and epsilon bits
    gamma_counts = [0 for x in range(0, data_length)]
    epsilon_counts = [1 for x in range(0, data_length)]

    for count in range(0, data_length):

        if counts[count] > half_report_length:
            gamma_counts[count] = 1
            epsilon_counts[count] = 0

    gamma_bits = ''.join([str(bit) for bit in gamma_counts])
    epsilon_bits = ''.join([str(bit) for bit in epsilon_counts])
    gamma_rate = int(gamma_bits,2)
    epsilon_rate = int(epsilon_bits,2)
    power_consumption = gamma_rate * epsilon_rate
    return power_consumption

def count_bits(report, bit_position):
    zeros, ones = 0, 0
    for line in report:
        if line[bit_position] == '1':
            ones += 1
        else:
            zeros += 1
    return zeros, ones

def most_common_value(report, bit_position):
    zeros, ones = count_bits(report, bit_position)

    new_report = []
    if ones < zeros:
        for line in report:
            if line[bit_position] == '0':
                new_report.append(line)

    else:
        for line in report:
            if line[bit_position] == '1':
                new_report.append(line)
    return new_report

def least_common_value(report, bit_position):
    zeros, ones = count_bits(report, bit_position)

    new_report = []
    if ones < zeros:
        for line in report:
            if line[bit_position] == '1':
                new_report.append(line)

    else:
        for line in report:
            if line[bit_position] == '0':
                new_report.append(line)
    return new_report

def get_rating(diagnostic_report, type="oxygen"):
    report = diagnostic_report
    data_length = len(diagnostic_report[0])
    for bit in range(0, data_length):
        if type == "oxygen":
            report = most_common_value(report, bit)
        elif type == "carbondioxide":
            report = least_common_value(report, bit)
        if len(report) == 1:
            return int(report[0],2)


def life_support_rating(diagnostic_report):
    oxygen_rating = get_rating(diagnostic_report, "oxygen")
    co2_scrubber_rating = get_rating(diagnostic_report, "carbondioxide")
    return oxygen_rating * co2_scrubber_rating

data = get_power_data()
power = power_consumption(data)
life_support = life_support_rating(data)
print(">", power)
print(">", life_support)
