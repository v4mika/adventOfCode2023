import re

maxColours = {"red":12, "green": 13, "blue": 14}

def parseLine(line):
    line = re.split('; |:|\n', line)
    game_no = int(line[0].split(" ")[1])
    
    for i in range(1, len(line)):
        set_of_cubes = re.split(",", line[i])
        set_of_cubes = [item.strip() for item in set_of_cubes if item != ""]
        for cube_set in set_of_cubes:
            num_char = cube_set.split(" ")
            if int(num_char[0]) > maxColours[num_char[1]]:
                return 0
    return game_no

def parseLine2(line):
    line = re.split('; |:|\n', line)
    game_no = int(line[0].split(" ")[1])
    colour_dict = {}
    for i in range(1, len(line)):
        set_of_cubes = re.split(",", line[i])
        set_of_cubes = [item.strip() for item in set_of_cubes if item != ""]
        for cube_set in set_of_cubes:
            num_char = cube_set.split(" ")
            if num_char[1] in colour_dict:
                colour_dict[num_char[1]] = max(colour_dict[num_char[1]], int(num_char[0]))
            else:
                colour_dict[num_char[1]] = int(num_char[0])
        
    return colour_dict["red"] * colour_dict["green"] * colour_dict["blue"]
    
        
with open("adventofcode.com_2023_day_2_input.txt", "r") as f:
# with open("example.txt", "r") as f:
    sum = 0
    count = 0
    for line in f:
        sum += parseLine2(line)
print("final answer", sum)
