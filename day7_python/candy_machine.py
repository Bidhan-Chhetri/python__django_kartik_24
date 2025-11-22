def main():
    candy = int(input("Enter the rs: "))
    check = buy_candy(candy)
    if check == "Candy bought!":
        print("Customer got the candy")
    elif check == None:
        print("No candy given")

def buy_candy(candy):
    if candy >= 10:
        return "Candy bought!"
    elif candy < 10:
        print("Not enough money")
        
  
main()