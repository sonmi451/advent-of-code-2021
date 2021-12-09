from read_datafile import read_datafile

def exponential_fish(lantern_fish, days):

    for day in range(1,days+1):
        print(f'Day {day}')

        lantern_fish = lantern_fish.copy()
        num_starting_fish = len(lantern_fish)

        print(f'> Before Countdown: {lantern_fish}')

        for fish in range(0, num_starting_fish):
            # count fish that reproduce
            if lantern_fish[fish] == 0:
                lantern_fish.append(8)

            # decrement reproduction cycle
            if lantern_fish[fish] > 6:
                lantern_fish[fish] = (lantern_fish[fish] - 1)
            else:
                lantern_fish[fish] = (lantern_fish[fish] - 1) % 7

        print(f'Day {day} fish: {lantern_fish} ')

    total_fish = len(lantern_fish)
    return total_fish
