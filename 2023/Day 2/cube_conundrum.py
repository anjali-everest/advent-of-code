def read_data() -> list:
    with open("input.txt") as f:
        return f.read().splitlines()

def get_formatted_data(data):
    games_info_map={}
    for index in range(len(data)):
        trials = data[index].split(':')[1].strip().split(';')
        game_map={}
        for trial in trials:
            for cube in trial.split(','):
                cubes_per_color = cube.split()
                if((cubes_per_color[1] in game_map.keys() and int(game_map.__getitem__(cubes_per_color[1])) < int(cubes_per_color[0])) or (cubes_per_color[1] not in game_map.keys()) ):
                    game_map[cubes_per_color[1]]= int(cubes_per_color[0])
        games_info_map.__setitem__(index, game_map)
    print(games_info_map)
    return games_info_map

def sum_of_valid_games():
    data = read_data()
    input = {'red': 12, 'green': 13, 'blue': 14}
    games_info = get_formatted_data(data)
    games_sum = 0
    for game in games_info.keys():
        if(not any(games_info[game][cube] > input[cube] for cube in input.keys())):
            games_sum+= game+1
    print(games_sum)

def sunm_of_min_set_of_cubes():
    data = read_data()
    games_info = get_formatted_data(data)
    games_sum = 0
    for game in games_info.keys():
        cubes_power = 1
        for cube in games_info[game].keys():
            cubes_power*= games_info[game][cube]
        games_sum+= cubes_power
    print(games_sum)


# sum_of_valid_games() # Part 1
sunm_of_min_set_of_cubes() # Part 2
