import re
from math import sqrt


def _parse_tiles(input):
    tiles, tileid = {}, 0
    for group in input.read().split('\n\n'):
        lines = group.splitlines()
        tileid = re.findall(r'(\d+)', lines[0])[0]
        tiles[int(tileid)] = lines[1:]
    return tiles


def _rotate_90_deg_clockwise(tile):
    return list(''.join(x[::-1]) for x in zip(*tile))


def _flip(tile):
    return list(reversed(tile.copy()))


def _build_tile_transformations(tile):
    tile90 = _rotate_90_deg_clockwise(tile)
    tile180 = _rotate_90_deg_clockwise(tile90)
    tile270 = _rotate_90_deg_clockwise(tile180)
    return [tile, tile90, tile180, tile270, _flip(tile), _flip(tile90), _flip(tile180), _flip(tile270)]


def _assemble_image(tile_transformations):
    side_len = int(sqrt(len(tile_transformations)))
    image_matrix = [[(0, 0)] * side_len for _ in range(side_len)]
    remaining_tiles = set(tile_transformations.keys())
    row, column = 0, 0
    while row < side_len and column < side_len:
        for tileid in remaining_tiles:
            for tid, transformation in enumerate(tile_transformations[tileid]):
                up_ok = left_ok = True


def part_two(filename):
    with open(filename) as input:
        tiles = _parse_tiles(input)
        tile_transformations = {tileid: _build_tile_transformations(tile) for tileid, tile in tiles.items()}
        n = 3
        rowcolumn = 6
        r, c = rowcolumn // n, rowcolumn % n
        _assemble_image(tile_transformations)


if __name__ == '__main__':
    # test_part_two_so_far()
    part_two('./20/example_input.txt')