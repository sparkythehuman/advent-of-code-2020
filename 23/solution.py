

def part_one(filename, rounds):
    with open(filename) as input:
        cups = [int(i) for i in input]
        max_index = len(cups) - 1
        for i in range(rounds):
            current_index = i % max_index
            current = cups[current_index]
            first_picked_up_idx = current_index + 1 if max_index > current_index else 0
            last_picked_up_idx = current_index + 3 if max_index >= current_index + 3 else current_index + 3 - max_index
            if first_picked_up_idx < last_picked_up_idx:
                picked_up = cups[first_picked_up_idx:last_picked_up_idx + 1]
                left = cups[:first_picked_up_idx] + cups[last_picked_up_idx + 1:]
            else:
                picked_up = cups[first_picked_up_idx:] + cups[:last_picked_up_idx + 1]
                left = cups[last_picked_up_idx + 1: first_picked_up_idx]
            destination = False
            # if the current cup is the smallest, we need the largest cup
            if min(left) == current:
                destination = max(left)
            else:
                # find the next smallest cup
                for j in range(1, max_index):
                    if current - j in left:
                        destination = current - j
                        break
            destination_index = left.index(destination)
            if destination_index + 1 < len(left):
                cups = left[:destination_index + 1] + picked_up + left[destination_index + 1:]
            else:
                cups = left + picked_up
        return cups




def test_part_one():
    assert part_one('./23/example_input.txt', 10) == [5, 8, 3, 7, 4, 1, 9, 2, 6,]


if __name__ == '__main__':
    test_part_one()
