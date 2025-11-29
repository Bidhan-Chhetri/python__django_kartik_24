class Laptop():
    def __init__(self, company, price):
        self.company = company
        self.price = price

    

l1 = Laptop("Dell", 120000)
l2 = Laptop("HP", 2344445)

print(f"Company name : {l1.company}\n Price : {l1.price}")
print(f"Company name : {l2.company}\n Price : {l2.price}")