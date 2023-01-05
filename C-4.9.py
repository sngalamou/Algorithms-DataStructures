def max_min(numbers):
  x = numbers[0]
  y = numbers[0]
  for num in data:
    if num> x:
      x = num
    elif num< y:
        y = num
  return x, y

print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))
print(max_min([1,2,3,4,5,6,7,8,9,10]))
print(max_min([1, 2, 3, 4, 5, 6]))
