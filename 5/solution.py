import math


def _bisect(lower, upper, direction):
    if direction in ['F', 'L']:
        return lower, lower + math.floor((upper-lower)/2)
    elif direction in ['B', 'R']:
        return upper - math.floor((upper-lower)/2), upper


with open('./5/input.txt') as input:
    highest_seat_id = 0
    all_seats = [_ for _ in range(0, 836)]
    for line in input:
        rlower = 0
        rupper = 127
        clower = 0
        cupper = 7
        count = 0
        for i in line.rstrip():
            # first bisect
            if i in ['F', 'B']:
                rlower, rupper = _bisect(rlower, rupper, i)
            if i in ['R', 'L']:
                clower, cupper = _bisect(clower, cupper, i)
            
            # then check set the other val to 0 on the final row/column
            if count == 6 and i == 'F':
                rupper = 0
            elif count == 6 and i == 'B':
                rlower = 0
            elif count == 9 and i == 'L':
                cupper = 0
            elif count == 9 and i == 'R':
                clower = 0

            # on the last letter of the boarding pass, get the seat_id
            if count == 9:
                seat_id = (rlower + rupper) * 8 + (clower + cupper) 
                all_seats.remove(seat_id)
                if seat_id > highest_seat_id:
                    highest_seat_id = seat_id

            count += 1

    # part 1            
    print(highest_seat_id)
    
    # part 2
    print(all_seats)

