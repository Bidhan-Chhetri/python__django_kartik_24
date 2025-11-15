num = int(input("Enter the number to check the number with 7 remainder between 1 to nth: "))

for i in range(1, num+1):
    if i % 10 == 7:
        print(i)