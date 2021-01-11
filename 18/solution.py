from copy import copy


def _break_into_groups(line):
    line = line.replace(' ', '')
    groups = []
    open_paren = []
    close_paren = []
    for index, char in enumerate(line):
        if char == '(':
            open_paren.append(index)
        elif char == ')':
            close_paren.append(index)
            if len(open_paren) == len(close_paren):
                groups.append(_break_into_groups(line[open_paren[0]+1:index]))
                open_paren = []
                close_paren = []
        elif len(open_paren) == 0:
            groups.append(char)
    return groups


def test_break_into_groups():
    assert ['1', '+', ['2', '*', '3'],  '+', ['4',  '*',  ['5', '+', '6']]] == _break_into_groups(
        '1 + (2 * 3) + (4 * (5 + 6))'
    )


def _get_item(item, method):
    if isinstance(item, list):
        item = method(item)
    return item


def _is_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def _evaluate_left_to_right(line):
    total = _get_item(line[0], _evaluate_left_to_right)  # init to first item
    current_index = 1  # since we have the first item, start at index 1
    while current_index + 1 < len(line):
        item = _get_item(line[current_index], _evaluate_left_to_right)
        if not _is_int(item):  # only do operations if we don't have an int
            next_item = _get_item(line[current_index + 1], _evaluate_left_to_right)
            total = eval(f'{total}{item}{next_item}')
            current_index += 2
        else:
            current_index += 1
    return total


def test__evaluate_left_to_right():
    assert 51 == _evaluate_left_to_right(['1', '+', ['2', '*', '3'],  '+', ['4',  '*',  ['5', '+', '6']]])
    assert 10088 == _evaluate_left_to_right([['3', '*', ['4', '*', '8'], '*', '5', '*', '7', '*', '3'], '+', '8'])


def part_one(filename):
    total = 0
    lines = [line.strip('\n') for line in open(filename)]
    for line in lines:
        total += _evaluate_left_to_right(_break_into_groups(line))
    return total


def test_part_one():
    assert part_one('./18/example_input.txt') == (26+437+12240+13632)


def _evaluate_left_to_right_add_then_multiply(line):
    new_line = copy(line)
    for index, char in enumerate(line):
        if char == '+' or (char == '*' and '+' not in line):
            first = _get_item(line[index - 1], _evaluate_left_to_right_add_then_multiply)
            second = _get_item(line[index + 1], _evaluate_left_to_right_add_then_multiply)
            new_line = line[0:index - 1] + [eval(f'{first}{char}{second}')] + line[index + 2:]
            return _evaluate_left_to_right_add_then_multiply(new_line)
    return int(new_line[0])


def test_evaluate_left_to_right_add_then_multiply():
    assert _evaluate_left_to_right_add_then_multiply(['1', '+', '2', '*', '3']) == 9
    assert _evaluate_left_to_right_add_then_multiply(['1', '+', '2', '*', '3', '*', '3', '+', '1']) == 36
    assert _evaluate_left_to_right_add_then_multiply(['1', '+', ['2', '*', '3'], '*', '3', '+', '1']) == 28


def part_two(filename):
    total = 0
    lines = [line.strip('\n') for line in open(filename)]
    for line in lines:
        total += _evaluate_left_to_right_add_then_multiply(_break_into_groups(line))
    return total


if __name__ == '__main__':
    test_break_into_groups()
    test__evaluate_left_to_right()
    test_part_one()
    test_evaluate_left_to_right_add_then_multiply()
    print(f"Part one answer: {part_one('./18/input.txt')}")
    print(f"Part one answer: {part_two('./18/input.txt')}")