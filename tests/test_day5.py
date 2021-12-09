from modules.day5 import graph_lines, count_peaks


def test_graph_lines():
    input = [
    	'0,9 -> 5,9',
        '8,0 -> 0,8',
        '9,4 -> 3,4',
        '2,2 -> 2,1',
        '7,0 -> 7,4',
        '6,4 -> 2,0',
        '0,9 -> 2,9',
        '3,4 -> 1,4',
        '0,0 -> 8,8',
        '5,5 -> 8,2'
    ]
    test_output = [int(x) for x in '0000000100001000010000100001000000000100011211121100000000000000000000000000000000000000002221110000']
    output = graph_lines(input, 10)
    assert output == test_output

def test_count_peaks():
    test_input = [int(x) for x in '0000000100001000010000100001000000000100011211121100000000000000000000000000000000000000002221110000']
    assert count_peaks(test_input) == 5
