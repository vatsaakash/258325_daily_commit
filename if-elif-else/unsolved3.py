'''Write Python code that asks a user how many pizza slices they want.
The pizzeria charges Rs 123.00 a slice.
If user order even number of slices, price per slice is Rs 120.00.
Print the total price depending on how many slices user orders.'''

ps= int(input("Enter the number of slices= "))
if (ps%2==0):
    print("price of the slices= ",120*ps)
else:
    print("Price of the slices= ",123*ps)