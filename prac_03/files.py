#Create or write name in name.txt

FILENAME = "name.txt"
out_file = open(FILENAME, 'w')
user_name = input("What is your name ")
print(user_name, file=out_file)
out_file.close()

#Open name.txt and say hi
out_file = open(FILENAME, 'r')
print(f" Hi {out_file.read()}")

#Open numbers to add the numbers
with open("numbers.txt", 'r') as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    result = first_number + second_number
print(result)

#Read all numbers and calculate total
total = 0
with open("numbers.txt", 'r') as in_file:
    for line in in_file:
        total = total + int(line)
print(total)

