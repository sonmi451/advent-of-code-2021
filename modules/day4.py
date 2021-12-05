from read_datafile import read_sequence, read_scoreboards

def get_bingo_numbers():
    filepath = './data/day4_numbers.txt'
    bingo_numbers = read_sequence(filepath)
    return bingo_numbers

def get_scoreboards():
    filepath = './data/day4_scoreboards.txt'
    scoreboards = read_scoreboards(filepath)
    return scoreboards

def bingo_game(bingo_boards, bingo_callouts):
    for num in bingo_callouts:
        for board in range(0, len(bingo_boards)):
            marked_board = [x if x != num else 'x' for x in bingo_boards[board]]
            bingo_boards[board] = marked_board.copy()
            if bingo(marked_board):
                return marked_board, num
    return False, num

def last_available_board(bingo_boards, bingo_callouts):
    num_scoreboards = len(bingo_boards)
    non_bingoed_boards = dict(zip(range(0,num_scoreboards),bingo_boards.copy()))
    for num in bingo_callouts:
        if len(non_bingoed_boards) == 1:
            first = next(iter(non_bingoed_boards))
            return non_bingoed_boards[first]
        for board in range(0, num_scoreboards):
            if bingo_boards[board]:
                marked_board = [x if x != num else 'x' for x in bingo_boards[board]]
                bingo_boards[board] = marked_board
                if bingo(marked_board):
                    bingo_boards[board] = False
                    del non_bingoed_boards[board]
    return False

def bingo(scoreboard):
    regions_of_interest = [scoreboard[:5],
                           scoreboard[5:10],
                           scoreboard[10:15],
                           scoreboard[15:20],
                           scoreboard[20:],
                           scoreboard[::5],
                           scoreboard[1::5],
                           scoreboard[3::5],
                           scoreboard[3::5],
                           scoreboard[4::5] ]
    if ['x','x','x','x','x'] in regions_of_interest:
        return True
    return False

def score_calculator(scoreboard, final_call):
    score = 0
    for num in scoreboard:
        if num != 'x':
            score+= int(num)
    return score * final_call

scoreboards = get_scoreboards()
bingo_callouts = get_bingo_numbers()
winning_board, winning_num = bingo_game(scoreboards, bingo_callouts)
if winning_board:
    score = score_calculator(winning_board, winning_num)

    print(f"> {score}")

else:
    print("No winner found!")

scoreboards = get_scoreboards()
bingo_callouts = get_bingo_numbers()
board = last_available_board(scoreboards, bingo_callouts)
winning_board, winning_num = bingo_game([board], bingo_callouts)

if winning_board:
    score = score_calculator(winning_board, winning_num)

    print(f"> {score}")

else:
    print("No winner found!")
