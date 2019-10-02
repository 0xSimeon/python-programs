# A program to determine type of numbers
num = float(input("Enter the number: "))
if num >= 0:
    number = 'Postive number'
    if num == 0:
        number = "Zero number"
else:
    number = "Negative number"
print(f" {num} is a {number} ")        