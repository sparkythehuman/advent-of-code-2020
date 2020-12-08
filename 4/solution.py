import re 


required_fields = {
    'byr': '19[2-9][0-9]|200[0-2]',
    'iyr': '20[1-2][0-9]',
    'eyr': '20[2-3][0-9]',
    'hgt': '1[5-8][0-9]cm|19[0-3]cm|[5-6][0-9]in|7[0-3]in',
    'hcl': '#[0-9|a-f]{6}',
    'ecl': 'amb|blu|brn|gry|grn|hzl|oth',
    'pid': '^[0-9]{9}$',
}


with open('./4/input.txt') as input:
    passports = []
    passport = {}
    for line in input: 
        for i in line.split(' '):
            j = i.split(':')
            try: 
                key, value = j[0], j[1].strip()
                passport[key] = value
            except IndexError:
                passports.append(passport)
                passport = {}
                continue

    valid_passports = 0
    valid_passports_2 = 0
    for i in passports: 
        meets_requirements = True
        valid = True
        for field in required_fields:
            if field not in i.keys():
                meets_requirements = False
            if not re.search(required_fields[field], i.get(field, '')):
                valid = False

        if meets_requirements:
            valid_passports += 1
        if valid:
            valid_passports_2 += 1
    
    print(valid_passports)
    print(valid_passports_2)

            



