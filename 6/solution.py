
# part 1
with open('./6/input.txt') as input:
    total = 0 
    prev_group_count = 0
    no_answers = [ chr(i) for i in range(ord('a'), ord('z')+1)]
    for line in input: 
        for i in line.split(' '):
            if i == '\n':
                no_answers = [ chr(i) for i in range(ord('a'), ord('z')+1)]
                continue
            for j in i:
                try: 
                    no_answers.remove(j)
                except ValueError:
                    continue

        if 26-len(no_answers) == 0:
            total += prev_group_count
        prev_group_count = 26-len(no_answers) 
    print(total)


# part 2
with open('./6/input.txt') as input_2:
    total_2 = 0 
    for line in input_2.read().split('\n\n'):
        group = line.split('\n')
        if len(group) == 1:
            total_2 += len(group[0])
        else:
            seen = {}
            all_yeses = set()
            for member in group:
                for answer in member:
                    if answer not in seen:
                        seen[answer] = 1
                    else:
                        seen[answer] += 1
                        foo = len(group)
                        if seen[answer] == len(group):
                            all_yeses.add(answer)
            total_2 += len(all_yeses)
    print(total_2)


    