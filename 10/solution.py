

def part_one(filename):
    with open(filename) as input:
        adapters = [int(x) for x in input.read().split('\n')]
        adapters.sort()
        device_joltage = adapters[len(adapters) - 1] + 3
        adapters.append(device_joltage)
        current_rating, diff_one, diff_three = 0, 0, 0
        for adapter in adapters:
            if adapter - current_rating == 1:
                diff_one += 1
                current_rating = adapter
            elif adapter - current_rating == 2:
                current_rating = adapter
            elif adapter - current_rating == 3:
                diff_three += 1
                current_rating = adapter
        return diff_one * diff_three


def _build_graph(adapters):
    # get a list of all potential children adapters (+1, +2 or +3)
    return {adapter: [adapter + x for x in [1,2,3] if adapter + x in adapters] for adapter in adapters}


def test_build_graph():
    assert _build_graph([0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]) == {
        0: [1],
        1: [4],
        4: [5, 6, 7],
        5: [6, 7],
        6: [7],
        7: [10],
        10: [11, 12],
        11: [12],
        12: [15],
        15: [16],
        16: [19],
        19: [22],
        22: []
    }


def _count_paths(graph):
    paths = {0:1}
    for parent, children in graph.items():
        for child in children:
            paths[child] = sum([paths.get(child, 0), paths[parent]])
    return paths


def test_count_paths():
    graph = {
        0: [1],
        1: [4],
        4: [5, 6, 7],
        5: [6, 7],
        6: [7],
        7: [10],
        10: [11, 12],
        11: [12],
        12: [15],
        15: [16],
        16: [19],
        19: [22],
        22: []
    }

    assert _count_paths(graph) == {
        0: 1,
        1: 1,
        4: 1,
        5: 1,
        6: 2,   # 6 can be reached from 5 (+1) or 4 (+1)
        7: 4,   # 7 can be reached from 6 (+2), 5 (+1) or 4 (+1)
        10: 4,
        11: 4,
        12: 8,  # 12 can be reached from 11 (+4) or 10 (+4)
        15: 8,
        16: 8,
        19: 8,
        22: 8
    }


def part_two(filename):
    with open(filename) as input:
        lines = [int(x) for x in input.read().split('\n')]
        lines.sort()
        device_joltage = max(lines) + 3
        adapters = [0] + lines + [device_joltage]
        graph = _build_graph(adapters)
        return _count_paths(graph)[device_joltage]
    

def test_part_two():
    assert part_two('./10/example_input.txt') == 8


if __name__ == '__main__':
    print(f'Part one solution is: {part_one("./10/input.txt")}')
    test_build_graph()
    test_count_paths()
    test_part_two()
    print(f'Part two solution is: {part_two("./10/input.txt")}')