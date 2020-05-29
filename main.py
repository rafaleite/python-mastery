def custom_range(num):
  count = 0
  while count < num:
    yield count
    count+=1

for x in range(10):
  print(x)