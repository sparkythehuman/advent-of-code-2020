import re

with open('./2/input.txt') as input:
    counter_one = 0
    counter_two = 0
    for line in input:
        data = line.strip().split(' ')
        character_positions = [m.start() for m in re.finditer(data[1].strip(':'), data[2])] 

        # part 1
        character_count = int(len(character_positions))
        lower = int(data[0].split('-')[0])
        upper = int(data[0].split('-')[1])
        if lower <= character_count <= upper:
            counter_one += 1

        # part 2
        character_positions = [i+1 for i in character_positions]
        first = int(data[0].split('-')[0])
        second = int(data[0].split('-')[1])
        if first in character_positions and second not in character_positions:
            counter_two += 1
        elif first not in character_positions and second in character_positions:
            counter_two += 1 

    print(counter_one)
    print(counter_two)