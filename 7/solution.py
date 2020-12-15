import re


def _can_hold(rule, bag):
    regex = f"[0-9] {bag} bag"
    bag_contains = rule.split('contain')[1]
    if re.search(regex, bag_contains):
        return True
    return False


def _count_bags(bags):
    count = 0
    for bag in bags.split(', '):
        try:
            count += int(re.findall('\d', bag)[0])
        except: 
            return None
    return count


def _get_children_bags(bags):
    children_bags = {}
    for bag in bags.split(', '):
        try:
            count = int(re.findall('\d', bag)[0])
            bag = re.split('\d', bag)[1].strip().rstrip('.').rstrip('s') 
            children_bags[bag] = count
        except:
            None
    return children_bags
    

def _build_rules_graph():
    with open('./7/input.txt') as input:
        rules = input.read().split('\n') 
        bag_graph = {}
        for rule in rules:
            parent_bag, children_bags = rule.split('s contain ')
            bag_graph[parent_bag] = {'count': None, 'children': None}
            bag_graph[parent_bag]['count'] = _count_bags(children_bags)
            bag_graph[parent_bag]['children'] = _get_children_bags(children_bags)
        return bag_graph


def _recursively_find_bag(can_hold_shiny_gold_bag, bag_type):
    with open('./7/input.txt') as input:
        rules = input.read().split('\n') 
        for rule in rules:
            if _can_hold(rule, bag_type):
                parent_bag = rule.split('bags')[0].strip() 
                can_hold_shiny_gold_bag.add(parent_bag)
                can_hold_shiny_gold_bag = _recursively_find_bag(can_hold_shiny_gold_bag, parent_bag)
        return can_hold_shiny_gold_bag


def _recursively_count_bags(count, rules_graph, target_bag, prev_parent_bag, multiplier):
    for parent_bag in rules_graph:
        if parent_bag == target_bag:
            if rules_graph[parent_bag]['children']: 
                if target_bag in rules_graph[prev_parent_bag]['children']: 
                    multiplier = multiplier * rules_graph[prev_parent_bag]['children'][target_bag] 
                count += rules_graph[parent_bag]['count'] * multiplier
                for child_bag in rules_graph[parent_bag]['children']:
                    count = _recursively_count_bags(count, rules_graph, child_bag, parent_bag, multiplier)
    return count


def part_one():
    can_hold_shiny_gold_bag = set()
    _recursively_find_bag(can_hold_shiny_gold_bag, 'shiny gold')
    print(len(can_hold_shiny_gold_bag))


part_one()


def part_two():
    rules_graph = _build_rules_graph()
    count = _recursively_count_bags(0, rules_graph, 'shiny gold bag', 'shiny gold bag', 1)
    print(count)


part_two()