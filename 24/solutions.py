from copy import copy


def _traverse_grid(directions, coordinates=(0,0)):
    if len(directions) == 0:
            return coordinates
    if directions.startswith('nw'):
        new_coordinates = (coordinates[0] - .5, coordinates[1] + 1)
        return _traverse_grid(directions[2:], new_coordinates)
    if directions.startswith('ne'):
        new_coordinates = (coordinates[0] + .5, coordinates[1] + 1)
        return _traverse_grid(directions[2:], new_coordinates)
    if directions.startswith('sw'):
        new_coordinates = (coordinates[0] - .5, coordinates[1] - 1)
        return _traverse_grid(directions[2:], new_coordinates)
    if directions.startswith('se'):
        new_coordinates = (coordinates[0] + .5, coordinates[1] - 1)
        return _traverse_grid(directions[2:], new_coordinates)
    if directions.startswith('e'):
        new_coordinates = (coordinates[0] + 1, coordinates[1])
        return _traverse_grid(directions[1:], new_coordinates)
    if directions.startswith('w'):
        new_coordinates = (coordinates[0] - 1, coordinates[1])
        return _traverse_grid(directions[1:], new_coordinates)


def test_traverse_grid():
    foo = _traverse_grid('nwwswee') 
    assert _traverse_grid('nwwswee') == (0, 0)
    assert _traverse_grid('esew') == (.5, -1)


def part_one(filename):
    with open(filename) as input:
        grid = set()
        for line in input:
            coordinates = _traverse_grid(line.rstrip())
            if coordinates in grid:
                grid.discard(coordinates)
            else:
                grid.add(coordinates)
        return len(grid)


def test_part_one():
    assert part_one('./24/example_input.txt') == 10


def _get_neighbors(coordinates):
    return [
        (coordinates[0] - .5, coordinates[1] + 1),
        (coordinates[0] + .5, coordinates[1] + 1),
        (coordinates[0] - .5, coordinates[1] - 1),
        (coordinates[0] + .5, coordinates[1] - 1),
        (coordinates[0] + 1, coordinates[1]),
        (coordinates[0] - 1, coordinates[1])
    ]


def _get_number_of_black_adjacent(grid, coordinates):
    neighbors = _get_neighbors(coordinates)
    return sum([1 for neighbor in neighbors if neighbor in grid])


def test_get_number_of_black_adjacent():
    grid = {
        (0, 0),
        (.5, 1),
        (-1, 0),
    }
    assert _get_number_of_black_adjacent(grid, (-.5, 1)) == 3
    assert _get_number_of_black_adjacent(grid, (-.5, -1)) == 2
    assert _get_number_of_black_adjacent(grid, (.5, -1)) == 1


def _is_black(grid, coordinates):
    black_neighbors = _get_number_of_black_adjacent(grid, coordinates)
    if coordinates in grid and 0 < black_neighbors <= 2:
        return True
    elif coordinates not in grid and black_neighbors == 2:
        return True
    return False


def test_is_black():
    grid = {
        (0, 0),
        (.5, 1),
        (-1, 0),
    }
    assert _is_black(grid, (0, 0))
    assert _is_black(grid, (-.5, -1))
    assert not _is_black(grid, (1, 1))


def part_two(filename):
    with open(filename) as input:
        grid = set()
        for line in input:
            coordinates = _traverse_grid(line.rstrip())
            if coordinates in grid:
                grid.discard(coordinates)
            else:
                grid.add(coordinates)
        for _ in range(100):
            new_grid = set()
            for tile in grid:
                if _is_black(grid, tile):
                    new_grid.add(tile)
                # ONLY go through neighbors of black tiles, we don't need to traverse the whole grid
                white_neighbors = [neighbor for neighbor in _get_neighbors(tile) if neighbor not in grid]
                for neighbor in white_neighbors:
                    if _is_black(grid, neighbor):
                        new_grid.add(neighbor)
            # grid = copy(new_grid)
            grid = new_grid
    return len(grid)

def test_part_two():
    assert part_two('./24/example_input.txt') == 2208

if __name__ == '__main__':
    test_traverse_grid()
    test_part_one()
    test_get_number_of_black_adjacent()
    test_is_black()
    test_part_two()
    print(f"Part one answer: {part_one('./24/input.txt')}")
    print(f"Part two answer: {part_two('./24/input.txt')}")