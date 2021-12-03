from read_datafile import read_datafile

def get_power_data():
    filepath = './data/day3.txt'
    diagnostic_report = read_datafile(filepath)
    return diagnostic_report

def power_consumption(diagnostic_report):
    half_report_length = int(len(diagnostic_report)/2)
    count_bit_1, count_bit_2, count_bit_3, count_bit_4, count_bit_5, count_bit_6, count_bit_7, count_bit_8, count_bit_9, count_bit_10, count_bit_11, count_bit_12 = 0,0,0,0,0,0,0,0,0,0,0,0

    gamma_bit1, gamma_bit2, gamma_bit3, gamma_bit4, gamma_bit5, gamma_bit6, gamma_bit7, gamma_bit8, gamma_bit9, gamma_bit10, gamma_bit11, gamma_bit12 = 0,0,0,0,0,0,0,0,0,0,0,0
    epsilon_bit1, epsilon_bit2, epsilon_bit3, epsilon_bit4, epsilon_bit5, epsilon_bit6, epsilon_bit7, epsilon_bit8, epsilon_bit9, epsilon_bit10, epsilon_bit11, epsilon_bit12 = 1,1,1,1,1,1,1,1,1,1,1,1

    for line in diagnostic_report:
        data = [x for x in line.strip()]
        if data[0] == '1':
            count_bit_1 += 1
        if data[1] == '1':
            count_bit_2 += 1
        if data[2] == '1':
            count_bit_3 += 1
        if data[3] == '1':
            count_bit_4 += 1
        if data[4] == '1':
            count_bit_5 += 1
        if data[5] == '1':
            count_bit_6 += 1
        if data[6] == '1':
            count_bit_7 += 1
        if data[7] == '1':
            count_bit_8 += 1
        if data[8] == '1':
            count_bit_9 += 1
        if data[9] == '1':
            count_bit_10 += 1
        if data[10] == '1':
            count_bit_11 += 1
        if data[11] == '1':
            count_bit_12 += 1

    if count_bit_1 > half_report_length:
        gamma_bit1 = 1
        epsilon_bit1 = 0

    if count_bit_2 > half_report_length:
        gamma_bit2 = 1
        epsilon_bit2 = 0

    if count_bit_3 > half_report_length:
        gamma_bit3 = 1
        epsilon_bit3 = 0

    if count_bit_4 > half_report_length:
        gamma_bit4 = 1
        epsilon_bit4 = 0

    if count_bit_5 > half_report_length:
        gamma_bit5 = 1
        epsilon_bit5 = 0

    if count_bit_6 > half_report_length:
        gamma_bit6 = 1
        epsilon_bit6 = 0

    if count_bit_7 > half_report_length:
        gamma_bit7 = 1
        epsilon_bit7 = 0

    if count_bit_8 > half_report_length:
        gamma_bit8 = 1
        epsilon_bit8 = 0

    if count_bit_9 > half_report_length:
        gamma_bit9 = 1
        epsilon_bit9 = 0

    if count_bit_10 > half_report_length:
        gamma_bit10 = 1
        epsilon_bit10 = 0

    if count_bit_11 > half_report_length:
        gamma_bit11 = 1
        epsilon_bit11 = 0

    if count_bit_12 > half_report_length:
        gamma_bit12 = 1
        epsilon_bit12 = 0

    gamma_bits = ''.join([str(gamma_bit1), str(gamma_bit2), str(gamma_bit3), str(gamma_bit4), str(gamma_bit5), str(gamma_bit6), str(gamma_bit7),str(gamma_bit8),str(gamma_bit9), str(gamma_bit10), str(gamma_bit11), str(gamma_bit12)])
    epsilon_bits = ''.join([str(epsilon_bit1), str(epsilon_bit2), str(epsilon_bit3), str(epsilon_bit4), str(epsilon_bit5), str(epsilon_bit6), str(epsilon_bit7),str(epsilon_bit8),str(epsilon_bit9), str(epsilon_bit10), str(epsilon_bit11), str(epsilon_bit12)])
    gamma_rate = int(gamma_bits,2)
    epsilon_rate = int(epsilon_bits,2)
    power_consumption = gamma_rate * epsilon_rate
    return power_consumption

data = get_power_data()
product = power_consumption(data)
print(">", product)
