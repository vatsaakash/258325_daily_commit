# Write a Python program to convert a list into a nested dictionary of keys
list = [1, 5, 8, 9]
dict = current = {'a': 2, 'b': 75}
for name in list:
    current[name] = {}
    current = current[name]
print(dict)