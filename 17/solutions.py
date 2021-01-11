import math
from copy import deepcopy


def _count_neighbors(key, graph):
    neighbors = 0
    x, y, z = [int(x) for x in key.split(',')]
    for x_to_check in [x + modifier for modifier in [-1, 0, 1]]:
        for y_to_check in [y + modifier for modifier in [-1, 0, 1]]:
            for z_to_check in [z + modifier for modifier in [-1, 0, 1]]:
                # skip the current key
                if x_to_check == x and y_to_check == y and z_to_check == z:
                    continue
                if graph.get(f'{x_to_check},{y_to_check},{z_to_check}'):
                    neighbors += 1
    return neighbors


def test_check_neighbors():
    graph = {
        '-1,1,0': False,
        '0,1,0': True,
        '1,1,0': False,
        '-1,0,0': False,
        '0,0,0': False,
        '1,0,0': True,
        '-1,-1,0': True,
        '0,-1,0': True,
        '1,-1,0': True,
    }
    assert _count_neighbors('0,0,0', graph) == 5
    assert _count_neighbors('1,1,0', graph) == 2
    assert _count_neighbors('0,-1,0', graph) == 3


def _build_next_iteration(graph, iteration, line_modifier):
    new_graph = deepcopy(graph)
    next_iteration = iteration + line_modifier + 1
    keys_to_check = range(-next_iteration, next_iteration + 1)
    for x in keys_to_check:
        for y in keys_to_check:
            for z in keys_to_check:
                key = f'{x},{y},{z}'
                value = graph.get(key, False)
                neighbors = _count_neighbors(key, graph)
                if value and neighbors not in [2, 3]:
                    new_graph[key] = False
                if not value and neighbors == 3:
                    new_graph[key] = True
    return new_graph


def test_build_next_iteration():
    graph = {
        '-1,1,0': False,
        '0,1,0': True,
        '1,1,0': False,
        '-1,0,0': False,
        '0,0,0': False,
        '1,0,0': True,
        '-1,-1,0': True,
        '0,-1,0': True,
        '1,-1,0': True,
    }
    new_graph = _build_next_iteration(graph, 1, 1)
    assert new_graph['1,-1,-1']


def part_one(filename):
    # coordinates, lines
    graph = {}
    lines = [line.strip('\n') for line in open(filename)]
    line_modifier = 0
    for row_index, line in enumerate(lines):
        line_modifier = math.floor(len(line) / 2)
        for line_index, char in enumerate(line):
            # key = x,y,z
            key = f'{line_index - line_modifier},{-1 * (row_index - line_modifier)},0'
            graph[key] = char == '#'
    for iteration in range(1, 7):
        graph = _build_next_iteration(graph, iteration, line_modifier)
    total = 0
    for value in graph.values():
        if value:
            total += 1
    return total


def test_part_one():
    assert part_one('./17/example_input.txt') == 112


def _count_neighbors_4d(key, graph):
    neighbors = 0
    x, y, z, w = [int(x) for x in key.split(',')]
    for x_to_check in [x + modifier for modifier in [-1, 0, 1]]:
        for y_to_check in [y + modifier for modifier in [-1, 0, 1]]:
            for z_to_check in [z + modifier for modifier in [-1, 0, 1]]:
                for w_to_check in [w + modifier for modifier in [-1, 0, 1]]:
                    # skip the current key
                    if x_to_check == x and y_to_check == y and z_to_check == z and w_to_check == w:
                        continue
                    if graph.get(f'{x_to_check},{y_to_check},{z_to_check},{w_to_check}'):
                        neighbors += 1
    return neighbors


def _build_next_iteration_4d(graph, iteration, line_modifier):
    new_graph = deepcopy(graph)
    next_iteration = iteration + line_modifier + 1
    keys_to_check = range(-next_iteration, next_iteration + 1)
    for x in keys_to_check:
        for y in keys_to_check:
            for z in keys_to_check:
                for w in keys_to_check:
                    key = f'{x},{y},{z},{w}'
                    value = graph.get(key, False)
                    neighbors = _count_neighbors_4d(key, graph)
                    if value and neighbors not in [2, 3]:
                        new_graph[key] = False
                    if not value and neighbors == 3:
                        new_graph[key] = True
    return new_graph


def part_two(filename):
    # coordinates, lines
    graph = {}
    lines = [line.strip('\n') for line in open(filename)]
    line_modifier = 0
    for row_index, line in enumerate(lines):
        line_modifier = math.floor(len(line) / 2)
        for line_index, char in enumerate(line):
            # key = x,y,z
            key = f'{line_index - line_modifier},{-1 * (row_index - line_modifier)},0,0'
            graph[key] = char == '#'
    for iteration in range(1, 7):
        graph = _build_next_iteration_4d(graph, iteration, line_modifier)
    total = 0
    for value in graph.values():
        if value:
            total += 1
    return total


def test_part_two():
    assert part_two('./17/example_input.txt') == 848

if __name__ == '__main__':
    test_check_neighbors()
    test_build_next_iteration()
    test_part_one()
    test_part_two()
    print(f"Part one answer: {part_one('./17/input.txt')}")
    print(f"Part two answer: {part_two('./17/input.txt')}")