

def _create_row(row):
    output = []
    for x in range(99):
        output.append(row.strip())
    output = ''.join(output)
    return list(output)


with open('./3/input.txt') as input:
    map_data = [ _create_row(x) for x in input ]

    slopes = {
        'right_1_down_1': {'right': 1, 'down': 1, 'trees': 0},
        'right_3_down_1': {'right': 3, 'down': 1, 'trees': 0},
        'right_5_down_1': {'right': 5, 'down': 1, 'trees': 0},
        'right_7_down_1': {'right': 7, 'down': 1, 'trees': 0},
        'right_1_down_2': {'right': 1, 'down': 2, 'trees': 0},
    }

    for key in slopes:
        right_index = 0 
        down_index = 0 
        for i in range(len(map_data)):
            right_index += slopes[key]['right']
            down_index += slopes[key]['down'] 
            try: 
                if map_data[down_index][right_index] == '#':
                    slopes[key]['trees'] += 1
            except IndexError:
                break

    print(slopes)
