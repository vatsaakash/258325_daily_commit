# Write a Python program to convert a list of tuples into a dictionary
list = [("x", 1), ("x", 5), ("x", 8), ("y", 9), ("y", 2), ("z", 4)]
dict = {}
for a1, a2 in list:
    dict.setdefault(a1, []).append(a2)
print (dict)
