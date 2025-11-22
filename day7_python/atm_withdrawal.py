def main():
    amount = int(input("Enter the amount: "))
    balance = int(input("Enter the balance: "))
    check_money = withdraw(balance, amount)

    if  check_money == None:
         print("Transaction failed")
    else:
        print(f"New balance: {check_money}")

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient balance")
    else:
        return balance - amount


main()