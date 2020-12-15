

adjacent = [
    [-1, -1], [-1, 0], [-1, 1], 
    [0, -1], [0, 1],
    [1, -1], [1, 0], [1, 1]
]


def _get_state_part_one(column, row_idx, column_idx, layout):
    if column == '.':
        return '.'
    elif column == 'L':
        for row_delta, column_delta in adjacent:
            try:
                if row_idx+row_delta >= 0 and column_idx+column_delta >= 0: 
                    if layout[row_idx+row_delta][column_idx+column_delta] == '#':
                        return 'L'
            except IndexError:
                continue
        return '#'
    elif column == '#':
        count = 0
        for row_delta, column_delta in adjacent:
            try:
                if row_idx+row_delta >= 0 and column_idx+column_delta >= 0: 
                    if layout[row_idx+row_delta][column_idx+column_delta] == '#':
                        count += 1
            except IndexError:
                continue
        return 'L' if count >= 4 else '#'


def _get_state_part_two(column, row_idx, column_idx, layout):
    if column == '.':
        return '.'
    elif column == 'L':
        for row_delta, column_delta in adjacent:
            row_check = row_idx+row_delta 
            column_check = column_idx+column_delta 
            seat_found = False
            while (row_check >= 0 and column_check >= 0) and not seat_found:
                try:
                    if layout[row_check][column_check] == '#':
                        seat_found = True
                        return 'L'
                    elif layout[row_check][column_check] == 'L':
                        seat_found = True
                except IndexError:
                    break
                row_check += row_delta
                column_check += column_delta
        return '#'
    elif column == '#':
        count = 0
        for row_delta, column_delta in adjacent:
            row_check = row_idx+row_delta 
            column_check = column_idx+column_delta 
            seat_found = False
            while (row_check >= 0 and column_check >= 0) and not seat_found:
                try:
                    if layout[row_check][column_check] == '#':
                        count += 1
                        seat_found = True
                    elif layout[row_check][column_check] == 'L':
                        seat_found = True
                except IndexError:
                    break
                row_check += row_delta
                column_check += column_delta
        return 'L' if count >= 5 else '#'


def _get_new_layout(layout, puzzle_part):
    _operations = {
        'part_one' : _get_state_part_one,
        'part_two' : _get_state_part_two
    }
    new_layout = []
    row_idx = 0
    for row in layout:
        new_row = []
        column_idx = 0
        for column in row:
            new_row.append(_operations[puzzle_part](column, row_idx, column_idx, layout))
            column_idx += 1
        row_idx += 1
        new_layout.append(new_row)
    return new_layout


def _find_final_seat_count(prev_layout, new_layout, puzzle_part):
    if prev_layout == new_layout:
        occupied_seat_count = 0
        for row in new_layout:
            for column in row:
                if column == '#':
                    occupied_seat_count += 1
        print(occupied_seat_count)
    else:
        _find_final_seat_count(new_layout, _get_new_layout(new_layout, puzzle_part), puzzle_part)


def part_one():
    with open('./11/input.txt') as input:
        layout = [ list(row) for row in input.read().split('\n')]
        _find_final_seat_count([], layout, 'part_one')


part_one()


def part_two():
    with open('./11/input.txt') as input:
        layout = [ list(row) for row in input.read().split('\n')]
        _find_final_seat_count([], layout, 'part_two')


part_two()