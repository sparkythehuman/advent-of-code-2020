

def part_one(input, rounds):
    cups = [int(x) for x in input]
    for i in range(rounds):
        # pick up the three cups and remove them from the circle
        first = cups[1]
        second = cups[2]
        third = cups[3]
        cups.remove(first)
        cups.remove(second)
        cups.remove(third)

        # select destination cup
        for j in range(1, len(cups) + 1):
            if cups[0] - j == 0:
                destination_idx = cups.index(max(cups))
                break
            elif cups[0] - j in cups:
                destination_idx = cups.index(cups[0] - j)
                break

        # place picked up cups immediately clockwise of the destination cup
        cups.insert(destination_idx + 1, first)
        cups.insert(destination_idx + 2, second)
        cups.insert(destination_idx + 3, third)
        # to simplify, we'll set the current cup back to index for the next round
        if i != rounds - 1:
            cups.append(cups[0])
            cups.pop(0)
    
    # get the labels on the cups after cup 1
    cup_one = cups.index(1)
    return ''.join(str(x) for x in cups[cup_one+1:]) 


def test_part_one():
    assert part_one('389125467', 10) == '926'


def part_two(input):
    cups = [int(x) for x in input] + [n for n in range(10, 1000001)]
    # create a linked list: key is cup, value is next cup
    cups_linked_list = {value: cups[idx + 1] if idx < len(cups) - 1 else cups[0] for idx, value in enumerate(cups)}

    current = cups[0]

    for _ in range(10000000):
        # pickup cups
        first = cups_linked_list[current]
        second = cups_linked_list[first]
        third = cups_linked_list[second]
        picked_up = [first, second, third]

        # select the destination cup
        for i in range(1, current + 1):
            if current - i == 0:
                destination = max([cup for cup in cups if cup not in picked_up])
                break
            elif current - i not in picked_up:
                destination = current - i
                break
        
        # update the links
        # the first and second cup links remain the same
        # the current cup should be linked to the cup after the third picked up cup
        cups_linked_list[current] = cups_linked_list[third]
        # the third cup should be linked to the cup after our destination cup
        cups_linked_list[third] = cups_linked_list[destination]
        # the destination cup should be linked to the first cup
        cups_linked_list[destination] = first

        # set our new current cup
        current = cups_linked_list[current]

    # our star cups are two cups that will end up immediately after cup 1
    first_star = cups_linked_list[1]
    second_star = cups_linked_list[first_star]
    return first_star * second_star


def test_part_two():
    assert part_two('389125467') == 149245887792


if __name__ == '__main__':
    test_part_one()
    test_part_two()
    print(f"Part one answer: {part_one('215694783', 100)}")
    print(f"Part two answer: {part_two('215694783')}")
