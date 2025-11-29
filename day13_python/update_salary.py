class Employee: 
            
    def __init__(self, employee_name, salary): 
            self.name = employee_name 
            self.salary = salary

    def update_salary(self, new_salary): 
            self.salary = new_salary 

p1 = Employee("Ravi", 20) 
p1.update_salary(25000) 
print(p1.salary) 