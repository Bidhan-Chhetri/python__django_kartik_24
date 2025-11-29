class Player():
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello! {self.name}, How are you?")
        

p1 = Player("Bidhan Chhetri")
p2 = Player("Bishesh Chhetri")
p1.greet()
p2.greet()