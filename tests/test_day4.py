from modules.day4 import bingo_game, last_available_board, score_calculator


def test_bingo_game():
    boards = [
    [22, 13, 17, 11,  0,
     8,  2, 23,  4, 24,
    21,  9, 14, 16,  7,
     6, 10,  3, 18,  5,
     1, 12, 20, 15, 19],

     [3, 15,  0,  2, 22,
     9, 18, 13, 17,  5,
    19,  8,  7, 25, 23,
    20, 11, 10, 24,  4,
    14, 21, 16, 12,  6],

    [14, 21, 17, 24,  4,
    10, 16, 15,  9, 19,
    18,  8, 23, 26, 20,
    22, 11, 13,  6,  5,
     2,  0, 12,  3,  7]
    ]
    sequence = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    winning_board_state, winning_num = bingo_game(boards, sequence)
    assert winning_num == 24
    assert winning_board_state == ['x', 'x','x', 'x', 'x', 10, 16, 15, 'x', 19, 18,  8, 'x', 26, 20, 22, 'x', 13,  6,  'x', 'x',  'x', 12,  3,  'x']


def test_last_available_board():
    boards = [
    [22, 13, 17, 11,  0,
     8,  2, 23,  4, 24,
    21,  9, 14, 16,  7,
     6, 10,  3, 18,  5,
     1, 12, 20, 15, 19],

     [3, 15,  0,  2, 22,
     9, 18, 13, 17,  5,
    19,  8,  7, 25, 23,
    20, 11, 10, 24,  4,
    14, 21, 16, 12,  6],

    [14, 21, 17, 24,  4,
    10, 16, 15,  9, 19,
    18,  8, 23, 26, 20,
    22, 11, 13,  6,  5,
     2,  0, 12,  3,  7]
    ]
    sequence = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    last_winning_board = last_available_board(boards, sequence)
    assert last_winning_board == [3, 15, 0,  2, 22, 9, 18, 13, 17,  5, 19,  8,  7, 25, 23, 20, 11, 10, 24, 4, 14, 21, 16, 12,  6]


def test_first_winner_score_calculator():
    board = [ 'x', 'x',  'x', 'x',  'x',
        10, 16, 15,   'x', 19,
        18,  8, 'x', 26, 20,
        22, 'x', 13,  6, 'x',
         'x',  'x', 12,  3,  'x',  'x']
    assert score_calculator(board, 24) == 4512


def test_last_winner_score_calculator():
    board = [3, 15, 'x', 'x', 22, 'x', 18, 'x', 'x', 'x', 19,  8, 'x', 25, 'x',  20, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 12, 6]
    assert score_calculator(board, 13) == 1924
