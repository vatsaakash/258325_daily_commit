# Write a Python program to get next day of a given date using if-elif-else
d = int(input("Day : "))

m = int(input("Month : "))

y = int(input("Year : "))

if ((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0):

    if m == 2:

        d1 = 29

    elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:

        d1 = 31

    else:

        d1 = 30

else:

    if m == 2:

        d1 = 28

    elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:

        d1 = 31

    else:

        d1 = 30

if d == 31 and m == 12:

    d = 1

    m = 1

    y = y + 1

elif d1 - d == 0:

    m = m + 1

    d = 1

else:

    d = d + 1

print("Next day is : ", d, "/", m, "/", y)