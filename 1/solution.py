with open('./1/input.txt') as input:
  data = [ int(x.strip()) for x in input ]

  # part 1
  for i in data:
    for j in data:
      if 2020 == i + j:
        print(i*j)
  
  # part 2
  for i in data:
    for j in data:
      for k in data:
        if 2020 == i + j + k:
          print(i*j*k)