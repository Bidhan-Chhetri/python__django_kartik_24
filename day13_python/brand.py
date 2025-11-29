class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    
    def mobil_info(self):
        print("Brand : ", self.brand)
        print("Price : ", self.price)
        

mob1 = Mobile("Toyota", 1200000)
mob1.mobil_info()