def _parse_decks(file):
    decks = []
    groups = file.read().split('\n\n')
    for group in groups:
        lines = group.splitlines()
        decks.append([int(x) for x in lines[1:]])
    return decks[0], decks[1]


def _play_game(player1, player2):
    while len(player1) != 0 and len(player2) != 0:
        if player1[0] > player2[0]:
            player1.append(player1[0])
            player1.append(player2[0])
        else:
            player2.append(player2[0])
            player2.append(player1[0])
        player1.pop(0)
        player2.pop(0)
    return player1, player2


def part_one(filename):
    with open(filename, 'r') as file:
        player1, player2 = _parse_decks(file)
        player1, player2 = _play_game(player1, player2)
        score = 0
        winner = player1 if len(player1) > len(player2) else player2
        for index, card in enumerate(winner):
            modifier = len(winner) - index
            score += card * modifier
    return score


def test_part_one():
    assert part_one('./22/example_input.txt') == 306


def _play_game_recursive(player1, player2):
    previous_rounds = []
    while len(player1) != 0 and len(player2) != 0:
        if [player1, player2] in previous_rounds:
            previous_rounds.append([player1, player2])
            # player one wins the game
            return [[1], []]
        else:
            previous_rounds.append([player1.copy(), player2.copy()])
            # look for subgames
            if player1[0] < len(player1) and player2[0] < len(player2):
                new_player1, new_player2 = _play_game_recursive(player1[1:(player1[0] + 1)], player2[1:(player2[0] + 1)])
                if len(new_player1) > len(new_player2):
                    # player one wins
                    player1.append(player1[0])
                    player1.append(player2[0])
                else:
                    # player two wins
                    player2.append(player2[0])
                    player2.append(player1[0])
            elif player1[0] > player2[0]:
                player1.append(player1[0])
                player1.append(player2[0])
            else:
                player2.append(player2[0])
                player2.append(player1[0])
        player1.pop(0)
        player2.pop(0)
    return player1, player2


def test_part_two():
    assert part_two('./22/example_input.txt') == 291


def part_two(filename):
    with open(filename, 'r') as file:
        player1, player2 = _parse_decks(file)
        player1, player2 = _play_game_recursive(player1, player2)
        score = 0
        winner = player1 if len(player1) > len(player2) else player2
        for index, card in enumerate(winner):
            modifier = len(winner) - index
            score += card * modifier
    return score



if __name__ == '__main__':
    test_part_one()
    test_part_two()
    print(f"Part one answer: {part_one('./22/input.txt')}")
    print(f"Part two answer: {part_two('./22/input.txt')}")