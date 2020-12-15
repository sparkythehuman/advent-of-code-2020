

def _test_instructions(instructions_dict):
    operations_run = []
    accumulator = 0
    i = 0 
    while i <= len(instructions_dict):
        if i in operations_run:
            return False, accumulator
            break;
        if i == len(instructions_dict): 
            return True, accumulator
            break
        operations_run.append(i)

        if instructions_dict[i]['operator'] == 'acc':
            if '+' in instructions_dict[i]['argument']:
                accumulator += int(instructions_dict[i]['argument'].lstrip('+'))
            elif '-' in instructions_dict[i]['argument']:
                accumulator -= int(instructions_dict[i]['argument'].lstrip('-'))
            i += 1
        elif instructions_dict[i]['operator'] == 'jmp':
            if '+' in instructions_dict[i]['argument']:
                i += int(instructions_dict[i]['argument'].lstrip('+'))
            elif '-' in instructions_dict[i]['argument']:
                i -= int(instructions_dict[i]['argument'].lstrip('-'))
        elif instructions_dict[i]['operator'] == 'nop':
            i += 1
    return False, accumulator


def _build_instruction_dict():
    with open('./8/input.txt') as input:
        instructions = input.read().split('\n')
        instructions_dict = { 
            index : { 
                'operator' : instruction.split(' ')[0],
                'argument': instruction.split(' ')[1]
                } for index, instruction in enumerate(instructions) } 
    return instructions_dict


def part_one():
    instructions_dict = _build_instruction_dict()
    success, accumulator = _test_instructions(instructions_dict)
    print(accumulator)


part_one()


def part_two():
    instructions_dict = _build_instruction_dict()
    for i in range(0, len(instructions_dict)): 
        if instructions_dict[i]['operator'] == 'jmp':
            instructions_dict[i]['operator'] = 'nop'
        elif instructions_dict[i]['operator'] == 'nop':
            instructions_dict[i]['operator'] = 'jmp'
        success, accumulator = _test_instructions(instructions_dict)
        if success:
            print(accumulator)
            break;
        else:
            instructions_dict = _build_instruction_dict()


part_two()