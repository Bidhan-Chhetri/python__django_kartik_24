# # question 1

# class Student():
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def average(self):
#         sum = 0
#         for mark in self.marks:
#             sum = sum + mark 

#         ave = sum / len(self.marks)

#         # print(self.name, ":" , ave)
#         return ave
            

# s1 = Student("Bidhan Chhetri", [44, 55, 78])
# print(f"hi {s1.name} average score is {s1.average()}.")


# question 2

# class Account: 
#     def __init__(self, account_balance, account_number):
#         self.account_balance = account_balance
#         self.account_number = account_number
        
#     def debit(self, debit):
#         balancing = self.account_balance - debit
#         return balancing
    
#     def credit(self, credit):
#         balancing = self.account_balance + credit
#         return balancing



# a1 = Account(100000, 1101)

# print(f"The debited amount is {a1.debit(12000)}.")
# print(f"The credited amount is {a1.debit(12000)}.")