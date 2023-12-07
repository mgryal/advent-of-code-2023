lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break


cubes = {
    "red":12,
    "green":13,
    "blue":14
}

#Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

all_id = []
for game in lines:
    game_info,cubes_info = game.split(":")
    game_id = int(game_info.split(" ")[1])
    cubes_sets = cubes_info.split(";")
    flag = False
    for cube_set in cubes_sets:
        cubes_list = cube_set.strip().split(",")
        for cube in cubes_list:
            number_cubes, cube_color = cube.strip().split(" ")
            if cubes[cube_color] < int(number_cubes):
                flag = True
    if flag:
        continue
    all_id.append(game_id)

print(sum(all_id))
