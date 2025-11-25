number = []

while(True):
    check = input("Enter Y if you want to continue to add the number in list: ").lower()
    if check == "y":
        get_number = int(input("Enter the number for square: "))
        number.append(get_number)
        continue
    else:
        break

sq_number = []

print(f"The added number in the list {number}")

for num in number: 
    square = num * num
    sq_number.append(square) 

print(f"The square of added number in the list {sq_number}")

