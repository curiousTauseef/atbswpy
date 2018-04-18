import datetime

class Employee:
    raise_amt = 1.04
    num_of_emp = 0
    #below is a constructor    ( Special Method -- Dunder Init )
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    #there is no email argument, still we can create
        self.email = first + '.' + last + '@gmail.com'
        Employee.num_of_emp += 1

    def fullname(self):
        return ('{} {}'.format(self.first, self.last))

    def applyRaise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return ("Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay))

    def __str__(self):
        return ('{} - {}'.format(self.fullname(), self.email))

    def __add__(self, other):
        return (self.pay + other.pay)

    def __len__(self):
        return (len(self.fullname()))
    #now creating a class method, (working with class insted of instances)
    @classmethod  #just like self it is mandatory for us to pass cls
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    #defining one  classmethod which parses input
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod  #no need to pass cls or self in static methods
    def isWorkDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee): #inhereted from Employee class using syntax as show
    raise_amt = 1.10
    num_of_dev = 0
    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay)
        self.language = language
        Developer.num_of_dev += 1

class Manager(Employee):
    num_of_manage = 0

    def __init__(self, first, last, pay, employ = None): #we dont pass list here, avoid passing mutable objects
        super().__init__(first, last, pay)
        Manager.num_of_manage += 1
        if employ is None:
            self.employ = []
        else:
            self.employ = employ

    def addEmployee(self, emp):
        if emp not in self.employ:
            self.employ.append(emp)

    def remEmployee(self, emp):
        if emp in self.employ:
            self.employ.remove(emp)

    def printEmployees(self):
        for emp in self.employ:
            print('--->',emp.fullname())

emp1 = Employee('Arush', 'Garg', 60000)
emp2 = Employee('Test', 'User', 70000)
print(emp1.fullname() +'.'+ str(emp1.pay ))
print(emp2.fullname() +'.'+ str(emp2.pay ))
#when class calls the method
Employee.applyRaise(emp2)#inside here pass any instance as an argument (self))
#print details after applying raise
print(emp1.fullname() +'.'+ str(emp1.pay ))
print(emp2.fullname() +'.'+ str(emp2.pay ))
#calling a classmethod with the help of className
Employee.set_raise_amt(1.05)
Employee.applyRaise(emp1)
print(emp1.fullname() +'.'+ str(emp1.pay ))
print(emp2.fullname() +'.'+ str(emp2.pay ))
#calling a static method with Class name
emp_str_3 = 'Kapil-Israni-12000'
emp_str_4 = 'Raghav-Jindal-15000'
emp3 = Employee.from_string(emp_str_3)
emp4 = Employee.from_string(emp_str_4)
print(emp3.fullname() +'.'+ str(emp3.pay ))
print(emp4.fullname() +'.'+ str(emp4.pay ))
myDate = datetime.date(2017, 3, 29)
print(Employee.isWorkDay(myDate))
#Developer class has inhereted all the features from the Employee class
dev1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev2 = Developer('Bucky', 'Roberts', 60000, 'Java')
#still Developer class has no __init__ method, but since it was inhereted it will look the base class
print(dev1.fullname() +'. '+ str(dev1.email))
print(dev2.fullname() +'. '+ str(dev2.email))
#using help() function
help(Developer)
print(dev1.fullname() +'. '+ str(dev1.pay))
print(dev2.fullname() +'. '+ str(dev2.pay))
print(dev1.fullname() +'. '+ str(dev1.pay)+'. '+ str(dev1.language))
print(dev2.fullname() +'. '+ str(dev2.pay)+'. '+ str(dev2.language))
Developer.set_raise_amt(1.15)
Developer.applyRaise(dev1)
Developer.applyRaise(dev2)
print(dev1.fullname() +'. '+ str(dev1.pay)+'. '+ str(dev1.language))
print(dev2.fullname() +'. '+ str(dev2.pay)+'. '+ str(dev2.language))
print(Developer.num_of_dev)
print(Employee.num_of_emp)
mgr1 = Manager('Sue', 'Smith', 90000, [dev1])
print(mgr1.email)
mgr1.addEmployee(dev2)
mgr1.printEmployees()
#isinstance or issubclass
print(isinstance(mgr1, Employee))
print(isinstance(mgr1, Developer))
print(issubclass(Developer,Employee))
print(repr(emp1)) #or emp1.__repr__()
print(str(emp1)) # or emp1.__str__()
print(1+2)
#is same as
print(int.__add__(1, 2))
#Operator Overloading
print( emp1 + emp2 ) #we have redefined dunder add method to add pays of two Employees
#there are plenty of dunder methods in Python Documentation ( check out Emulating numeric types)
#__repr__ - unambiguos representation of the object and should be used for debugging and logging and etcself.
#__str__  - meant to be more of a readable representation of an object
print(len('test'))
print('test'.__len__())
print(len(emp1))  # it will print lenght of employee.fullname


