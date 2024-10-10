total = 0
num_of_items = int(input("How many items would you like to add? "))
print(num_of_items)
while num_of_items < 0:
    print("Please enter a positive integer")
    num_of_items = int(input("How many items would you like to add? "))
for i in range(num_of_items):
    price = float(input("What is the price of item {}? ".format(i+1)))
    total += price
    print(price)
if total > 100:
    total *= 0.9
print(f"Total price for {num_of_items} items is ${total:.2f}")
