from read_datafile import read_sequence, read_scoreboards

def get_bingo_numbers():
    filepath = './data/day4_numbers.txt'
    bingo_numbers = read_sequence(filepath)
    return bingo_numbers

def get_scoreboards():
    filepath = './data/day4_scoreboards.txt'
    scoreboards = read_scoreboards(filepath)
    return scoreboards

def board_marker(scoreboards, bingo_callouts):
    for num in bingo_callouts:
        for scoreboard in range(0, len(scoreboards)):
            new_scoreboard = [x if x != num else 'x' for x in scoreboards[scoreboard]]
            scoreboards[scoreboard] = new_scoreboard.copy()
            if bingo(new_scoreboard):
                return new_scoreboard, num
    return False, num

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
winning_board, winning_num = board_marker(scoreboards, bingo_callouts)
if winning_board:
    score = score_calculator(winning_board, winning_num)

    print(f"> {score}")

else:
    print("No winner found!")
