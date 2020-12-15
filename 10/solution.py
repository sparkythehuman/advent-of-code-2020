

def part_one():
    with open('./10/input.txt') as input:
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
        print(f'{diff_one} differences of 1 jolt')
        print(f'{diff_three} differences of 3 jolts')
        print(f'Puzzle solution is { diff_one * diff_three }')


part_one()

