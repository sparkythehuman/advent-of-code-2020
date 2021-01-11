def _get_loop_size(public_key):
    loop_size = 0
    value = 1 
    subject_number = 7
    while public_key != value:
        value = (value * subject_number) % 20201227
        loop_size += 1
    return loop_size


def test_get_loop_size():
    assert _get_loop_size(17807724) == 11


def _get_encryption_key(loop_size, subject_number):
    value = 1 
    for _ in range(loop_size):
        value = (value * subject_number) % 20201227
    return value
 

def test_get_encryption_key():
    assert _get_encryption_key(8, 17807724) == 14897079
    assert _get_encryption_key(11, 5764801) == 14897079


def part_one(door_pub_key, card_pub_key):
    door_loop_size = _get_loop_size(door_pub_key)
    card_loop_size = _get_loop_size(card_pub_key)

    door_encryption_key = _get_encryption_key(card_loop_size, door_pub_key) 
    card_encryption_key = _get_encryption_key(door_loop_size, card_pub_key)

    return door_encryption_key, card_encryption_key 


if __name__ == '__main__':
    test_get_loop_size()
    test_get_encryption_key()

    door_key, card_key = part_one(335121, 363891) 
    print("Part one answer: {} {}".format(door_key, card_key))