def find_digit_patterns(input):
    decoded = []
    for line in input:
        crib = {}
        split = line.split(' | ')
        signal_patterns = [''.join(sorted(x)) for x in split[0].split(' ')]
        output_values = [''.join(sorted(x)) for x in split[1].split(' ')]

        print(signal_patterns)
        print(output_values)

        # decode based on string length
        for pattern in signal_patterns:
            pattern_found = False
            crib[pattern] = '.'
            if len(pattern) == 2:
                crib[pattern] = 1
                pattern_found = True
            elif len(pattern) == 3:
                crib[pattern] = 7
                pattern_found = True
            elif len(pattern) == 4:
                crib[pattern] = 4
                pattern_found = True
            elif len(pattern) == 7:
                crib[pattern] = 8
                pattern_found = True

        # decode output
        crib['output'] = [crib[output_value] for output_value in output_values]
        decoded.append(crib)
    return decoded


def count_digits(decoded, numbers_of_interest):
    instances = 0
    for crib in decoded:
        for number in crib['output']:
            if number in [1, 4, 7, 8]:
                instances += 1
    return instances
