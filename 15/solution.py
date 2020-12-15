

def _get_last_number_spoken(starting_numbers, target):
    numbers_map = {}
    for x in range(0, len(starting_numbers)):
        numbers_map[starting_numbers[x]] = { 'first_prev_turn': x+1}

    i = len(starting_numbers) + 1
    last_number_spoken = starting_numbers[ len(starting_numbers) - 1 ] 
    while i <= target:
        if last_number_spoken not in numbers_map.keys():
            last_number_spoken = 0
            numbers_map = { 'first_prev_turn': i }
        if last_number_spoken in numbers_map.keys():
            if numbers_map[last_number_spoken].get('second_prev_turn', False) is False:
                last_number_spoken = 0
                try: 
                    numbers_map[last_number_spoken]['second_prev_turn'] = numbers_map[last_number_spoken]['first_prev_turn']
                    numbers_map[last_number_spoken]['first_prev_turn'] = i
                except KeyError:
                    numbers_map[last_number_spoken] = {'first_prev_turn' : i}
            else:
                last_number_spoken = numbers_map[last_number_spoken]['first_prev_turn'] - numbers_map[last_number_spoken]['second_prev_turn'] 
                try: 
                    numbers_map[last_number_spoken]['second_prev_turn'] = numbers_map[last_number_spoken]['first_prev_turn']
                    numbers_map[last_number_spoken]['first_prev_turn'] = i
                except KeyError:
                    numbers_map[last_number_spoken] = {'first_prev_turn' : i}
        else:
            numbers_map[last_number_spoken] = {'first_prev_turn' : i}
            last_number_spoken = 0
        i += 1
    print(last_number_spoken)


def part_one():
    _get_last_number_spoken([6,4,12,1,20,0,16], 2020)


part_one()


def part_two():
    _get_last_number_spoken([6,4,12,1,20,0,16], 30000000)


part_two()