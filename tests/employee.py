class Employee():
    '''A simple class to model an employee'''
    all = []
    #defining attributes
    def __init__(self, first_name: str, last_name: str, salary=0.0):
        '''Constructor for class instantiation'''

        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

        self.all.append(self)

    # creating the give rise method
    def give_raise(self, amount=5000):
        self.amount = amount

        return (self.salary + self.amount)

    def __repr__(self) -> str:
        return "{} {}, salary: Ksh. {}".format(self.first_name.title(), self.last_name.title(), self.salary)

# emp = Employee('John', 'Doe', 5000)

# print(emp.give_raise(60000))
    