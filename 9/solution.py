

def _is_in_preamble(item, preamble):
    for p in preamble:
        if int(item) - int(p) in preamble and int(item) - int(p) != int(p):
            return True


def _build_data(preamble_len):
    with open('./9/input.txt') as input:
        ciphertext = [int(i) for i in input.read().split('\n')]
        preamble = [int(ciphertext[j]) for j in range(0, preamble_len) ]
        return preamble, ciphertext


def _find_target(target, index, ciphertext):
    sum = 0
    contiguous_set = []
    for x in range(index, len(ciphertext)):
        sum += ciphertext[x]
        contiguous_set.append(ciphertext[x])
        if sum == target:
            return True, contiguous_set
        elif sum > target:
            return False, None


def part_one(preamble_len):
    preamble, ciphertext = _build_data(preamble_len)
    for k in range(preamble_len, len(ciphertext)):
        if not _is_in_preamble(ciphertext[k], preamble):
            print(ciphertext[k])
            return
        preamble.pop(0)
        preamble.append(ciphertext[k])


part_one(25)


def part_two(preamble_len):
    target = part_one(preamble_len) 
    preamble, ciphertext = _build_data(preamble_len)
    for k in range(0, len(ciphertext)):
        success, contiguous_set = _find_target(target, k, ciphertext)
        if success:
            print(max(contiguous_set) + min(contiguous_set))
            return


part_two(25)
