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

data = get_power_data()
product = power_consumption(data)
print(">", product)
