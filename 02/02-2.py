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

max_cubes = {
    "red":0,
    "green":0,
    "blue":0

}

#Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

all_id = []
cubes_power = []
for game in lines:
    game_info,cubes_info = game.split(":")
    game_id = int(game_info.split(" ")[1])
    cubes_sets = cubes_info.split(";")
    flag = False
    for cube_set in cubes_sets:
        cubes_list = cube_set.strip().split(",")
        for cube in cubes_list:
            number_cubes, cube_color = cube.strip().split(" ")
            if(max_cubes[cube_color] < int(number_cubes)):
                max_cubes[cube_color] = int(number_cubes)
    print(max_cubes)
    cubes_power.append(max_cubes["blue"] * max_cubes["green"] * max_cubes["red"])
    max_cubes = {
        "red":0,
        "green":0,
        "blue":0
    }

print(sum(cubes_power))