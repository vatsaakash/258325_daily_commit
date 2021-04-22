# Write a Python program to find the second smallest number in a list

def second_smallest(numbers):
  if (len(numbers)<2):
    return
  if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
    return
  dup_items = set()
  uniq_items = []
  for x in numbers:
    if x not in dup_items:
      uniq_items.append(x)
      dup_items.add(x)
  uniq_items.sort()
  return  uniq_items[1]

print(second_smallest([1, 8, -8, -78, 10, -27]))
print(second_smallest([41, 11, 90, 0, 12, -72, -24]))
print(second_smallest([1, 1, 3, 0, 0, 0, 2, -2, -3]))
print(second_smallest([4,4]))
print(second_smallest([2]))
