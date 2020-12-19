import re
from copy import deepcopy


def _get_valid_numbers(rule, valid_numbers=set()):
    matches = re.finditer(r"(\d*-\d*)",rule)
    for _, match in enumerate(matches, start=1):
        start, end = int(match.group(0).split('-')[0]), int(match.group(0).split('-')[1])+1
        for i in range(start, end):
            valid_numbers.add(i)

    return valid_numbers


def test_get_valid_numbers():
    assert _get_valid_numbers('class: 1-3 or 5-7') == {1,2,3,5,6,7,}


def _build_valid_numbers(rules): 
    valid_numbers = set()
    for rule in rules.splitlines(): 
        valid_numbers = _get_valid_numbers(rule, valid_numbers)

    return valid_numbers


def test_build_valid_numbers():
    assert _build_valid_numbers('class: 1-3 or 5-7\nrow: 6-11 or 33-34') == {1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 33, 34}


def _get_invalid_numbers(ticket, valid_numbers, invalid_numbers):
    for number in ticket.split(','):
        if number.isnumeric() and int(number) not in valid_numbers:
            invalid_numbers.append(int(number))

    return invalid_numbers


def test_get_invalid_numbers():
    assert _get_invalid_numbers(
        ticket='2,4,11,22,33,44',
        valid_numbers={1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 33, 34},
        invalid_numbers=[12]
    ) == [12, 4, 22, 44]


def part_one(filename):
    rules, my_ticket, nearby_tickets = open(filename).read().split('\n\n')

    valid_numbers = _build_valid_numbers(rules)
    invalid_numbers = []
    for ticket in nearby_tickets.split('\n'):
        invalid_numbers = _get_invalid_numbers(ticket, valid_numbers, invalid_numbers) 

    return sum(invalid_numbers)


def test_part_one():
    assert 71 == part_one('./16/example_input.txt')


def _remove_all_invalid_tickets(valid_numbers, tickets):
    valid_tickets = []
    for ticket in tickets.splitlines()[1:]:
        ticket_numbers = [int(x) for x in ticket.split(',')]
        if all(number in valid_numbers for number in ticket_numbers):
            valid_tickets.append(ticket_numbers)

    return valid_tickets


def test_remove_all_invalid_tickets():
    assert _remove_all_invalid_tickets(
        valid_numbers=[1, 2, 3, 4, 5, 6, 7],
        tickets='nearby tickets:\n1,6,3\n7,3,47\n7,5,1'
    ) == [[1, 6, 3], [7, 5, 1]]


def _build_column_graph(tickets):
    graph = {}
    for ticket in tickets:
        for index, value in enumerate(ticket):
            if graph.get(index):
                graph[index].append(value)
            else:
                graph[index] = [value]
    return graph


def test_build_column_graph():
    assert _build_column_graph([[6, 45], [8, 78]]) == {0: [6, 8], 1: [45, 78]}


def _check_if_rule_works(rule, numbers):
    valid_numbers = _get_valid_numbers(rule, set())
    return all(number in valid_numbers for number in numbers)


def test_check_if_rule_works():
    assert _check_if_rule_works('row: 0-5 or 8-19', [3, 15, 5])
    assert not _check_if_rule_works('seat: 0-13 or 16-19', [3, 15, 5])


def _build_valid_rule_columns(rules, colum_graph):
    rule_columns = {}
    for rule_idx, rule in enumerate(rules.splitlines()):
        for column_idx, numbers in colum_graph.items():
            if _check_if_rule_works(rule, numbers):
                if rule_columns.get(rule_idx):
                    rule_columns[rule_idx].append(column_idx)
                else:
                    rule_columns[rule_idx] = [column_idx]

    return rule_columns


def _find_next_number_to_remove(rule_columns, removed_numbers):
    for _, numbers in rule_columns.items():
        if len(numbers) == 1 and numbers[0] not in removed_numbers:
            number_to_remove = numbers[0]
            removed_numbers.append(number_to_remove)
            return False, number_to_remove, removed_numbers

    return True, False, removed_numbers


def _map_valid_positions_to_columns(rules, column_graph):
    done = False 
    removed_numbers = []
    rule_columns = _build_valid_rule_columns(rules, column_graph)
    while not done:
        done, number_to_remove, removed_numbers = _find_next_number_to_remove(rule_columns, removed_numbers)
        if  number_to_remove is not False:
            new_rule_colums = deepcopy(rule_columns)
            for _, numbers in new_rule_colums.items():
                if number_to_remove in numbers and len(numbers) > 1:
                    numbers.remove(number_to_remove)
            rule_columns = new_rule_colums
            
    return rule_columns


def part_two(filename):
    rules, my_ticket, nearby_tickets = open(filename).read().split('\n\n')
    my_ticket = [int(x) for x in my_ticket.splitlines()[1].split(',')]
    valid_numbers = _build_valid_numbers(rules)
    valid_tickets = _remove_all_invalid_tickets(valid_numbers, nearby_tickets)
    column_graph = _build_column_graph(valid_tickets)
    valid_rule_positions = _map_valid_positions_to_columns(rules, column_graph)
    departure_rule_indexes = [i for i, rule in enumerate(rules.splitlines()) if 'departure' in rule]
    total = 1
    for i in departure_rule_indexes:
        total *= my_ticket[valid_rule_positions[i][0]]

    return total



if __name__ == '__main__':
    test_get_valid_numbers()
    test_build_valid_numbers()
    test_get_invalid_numbers()
    test_part_one()
    print("Part one answer: {}".format(part_one('./16/input.txt')))
    test_remove_all_invalid_tickets()
    test_build_column_graph()
    test_check_if_rule_works()
    print("Part two answer: {}".format(part_two('./16/input.txt')))