from read_datafile import read_datafile

def get_input_data():
    filepath = './data/day8.txt'
    data = read_datafile(filepath)
    return data

def find_digit_patterns(input):
    decoded = []

    for line in input:
        zero = []
        one = []
        two = []
        three = []
        four = []
        five = []
        six = []
        seven = []
        eight = []
        nine = []
        crib = {}
        split = line.split(' | ')
        signal_patterns = [''.join(sorted(x)) for x in split[0].split(' ')]
        output_values = [''.join(sorted(x)) for x in split[1].split(' ')]


        # decode based on string length
        for pattern in signal_patterns:
            crib[pattern] = 0
            if len(pattern) == 2:
                crib[pattern] = 1
                one = [x for x in pattern]

            elif len(pattern) == 3:
                crib[pattern] = 7
                seven = [x for x in pattern]

            elif len(pattern) == 4:
                crib[pattern] = 4
                four = [x for x in pattern]

            elif len(pattern) == 7:
                crib[pattern] = 8
                eight = [x for x in pattern]

        # # decode 0 6 9 based on string config
        # for pattern in signal_patterns:
        #     if len(pattern) == 6: # test for 0, 6 or 9
        #         # print(pattern)
        #         if all(item in pattern for item in four):
        #             crib[pattern] = 9
        #             print('> nine')
        #             nine = [x for x in pattern]
        #         elif all(item in pattern for item in four) and all(item in pattern for item in seven):
        #             crib[pattern] = 6
        #             print('> six')
        #         else:
        #             crib[pattern] = 0
        #             print('> zero')

        # decode 0 6 9 based on string config
        for pattern in signal_patterns:
            if len(pattern) == 6: # test for 0, 6 or 9
                crib[pattern] = 6
                if all(item in pattern for item in seven):
                    crib[pattern] = 0
                    if all(item in pattern for item in four):
                        crib[pattern] = 9
                        nine = [x for x in pattern]
                        print('nine')


        # decode 2 3 5 based on string config
        for pattern in signal_patterns:
            if len(pattern) == 5:
                crib[pattern] = 2
                if all(item in pattern for item in one):
                    crib[pattern] = 3
                    print('three')
                if all(item in pattern for item in seven):
                    crib[pattern] = 5
                    print('five')

        print(crib)

        # decode output
        crib['output'] = int(''.join([str(crib[output_value]) for output_value in output_values]))
        decoded.append(crib)
    return decoded

def sum_all_outputs(decoded_numbers):
    outputs = [crib['output'] for crib in decoded_numbers]
    return sum(outputs)

def count_digits(decoded, numbers_of_interest):
    instances = 0
    for crib in decoded:
        for number in crib['output']:
            if number in [1, 4, 7, 8]:
                instances += 1
    return instances

# input = get_input_data()
# decoded_numbers = find_digit_patterns(input)
# num_digits = count_digits(decoded_numbers, [1, 4, 7, 8])
# print(num_digits)
