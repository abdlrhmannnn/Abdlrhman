###Constructors explanations

# class Customer:
#     def __init__(self, name, balance):  
#         self.name = name
#         self.balance = balance
#         print("The	init	method was called")

# cust = Customer("Lara de Silva" , 100) # <-- don't specify balance explicitly  print(cust.name)
# print(cust.name) # <-- attribute is created anyway
# print(cust.balance) # <-- attribute is created anyway


###Constructors with default values

# class Customer:
#     def	__init__(self, name, balance=0):  
#         self.name = name
#         self.balance = balance
#         print("The	init	method was called")
        

# cust = Customer("Lara de Silva") # <-- don't specify balance explicitly  print(cust.name)
# print(cust.balance) # <-- attribute is created anyway


###Class other special functions

# class Customer:
#     def	__init__(self, name, balance=0):  
#         self.name = name
#         self.balance = balance
#         print("The	init	method was called")
        
#     def __str__(self):
#         return 'Customer : ' +str(self.name)+ ' , balance: ' + str(self.balance) 
    
#     def __add__(self, other): # On "self + other"
#         return Customer("Test_Customer",self.balance + other)

# cust = Customer("Lara de Silva") # <-- don't specify balance explicitly  print(cust.name)
# # print(cust.balance) # <-- attribute is created anyway
# # print(cust)

# c2 = cust + 230
# print(c2.balance)



###Constructors Vs. Destructors

class Employee:

	# Initializing
	def __init__(self):
		print('Employee created.')

	# Deleting (Calling destructor)
	def __del__(self):
		print('Destructor called, Employee deleted.')

obj = Employee()
del obj


################################################################################
class Person(object):

# 	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name

	# To check if this person is an employee
	def isEmployee(self):
		return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

	# Here we return true
	def isEmployee(self):
		return True


# Driver code
person = Person("Ahmed") # An Object of Person
print(person.getName(), person.isEmployee())

emp = Employee("Ali") # An Object of Employee
print(emp.getName(), emp.isEmployee())



print("############################################################")


# Python code to demonstrate how parent constructors
# are called.

## parent class
# class Person(object):

	# __init__ is known as the constructor
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)

# child class
class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post

		# invoking the __init__ of the parent class
		Person.__init__(self, name, idnumber)

# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()


print("########################################################")

# Python code to demonstrate how to use super()

# parent class
class Person():
    def __init__(self, name, age):
    	self.name = name
    	self.age = age
    
    def display(self):
    	print(self.name, self.age)

# child class
class Student(Person):
    def __init__(self, name, age):
		self.name = name
		self.age = age
    # inheriting the properties of parent class
    super().__init__("Osama", age)
    def displayInfo(self):
    	print(self.sName, self.sAge)

obj = Student("Khalid", 23)
obj.display()
obj.displayInfo()

###############################################################
value  =int(input("Enter "))
try:
    print(10/0)
    int(input("Enter"))
    print(10/0)
except ZeroDivisionError:
    print("Zero Error")
except:
    print("This Is Not Integer")
else:
    print("Good, This IS Integer")

parent class
class Person():
    def __init__(self, name, age):
    	self.name = name
    	self.age = age
    
    def display(self):
    	print(self.name, self.age)
    
    # child class
class Student(Person):
    def __init__(self, name, age, dob):
    	self.dob = dob
    	# inheriting the properties of parent class
    	super().__init__(name, age)
    
    def displayInfo(self):
    	print(self.name, self.age, self.dob)

obj = Student("Mayank", 23, "16-03-2000")
obj.display()
obj.displayInfo()

Python example to show the working of multiple
inheritance

class Base1(object):
	def __init__(self):
		self.str1 = "Geek1"
		print("Base1")


class Base2(object):
	def __init__(self):
		self.str2 = "Geek2"
		print("Base2")


class Derived(Base1, Base2):
	def __init__(self):

		# Calling constructors of Base1
		# and Base2 classes
		Base1.__init__(self)
		Base2.__init__(self)
		print("Derived")

	def printStrs(self):
		print(self.str1, self.str2)


ob = Derived()
ob.printStrs()

# A Python program to demonstrate multilevel 

# inheritance 

class Base(object):

	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name


# Inherited or Sub class (Note Person in bracket)
class Child(Base):

	# Constructor
	def __init__(self, name, age):
		Base.__init__(self, name)
		self.age = age

	# To get name
	def getAge(self):
		return self.age

# Inherited or Sub class (Note Person in bracket)


class GrandChild(Child):

	# Constructor
	def __init__(self, name, age, address):
		Child.__init__(self, name, age)
		self.address = address

	# To get address
	def getAddress(self):
		return self.address


# Driver code
g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())


# class Person(object):

 	# __init__ is known as the constructor
 	def __init__(self, name, idnumber):
         self.name = name
         self.idnumber = idnumber

 	def display(self):
         print(self.name)
         print(self.idnumber)



obj = Person("Khalid", 257853)

# accessing public data member
print("Name: ", obj.name)
print("Id: ", obj.idnumber)
########################################################

# calling public member function of the class
obj.display()


"""
Protected Access Modifier:
    The members of a class that are declared protected are only accessible to a class derived 
    from it. Data members of a class are declared protected by adding a single underscore ‘_’ 
"""

# program to illustrate protected access modifier in a class

class Student:
	
	# protected data members
	_name = None
	_roll = None
	_branch = None
	
	# constructor
	def __init__(self, name, roll, branch): 
		self._name = name
		self._roll = roll
		self._branch = branch
	
	# protected member function 
	def _displayRollAndBranch(self):

		# accessing protected data members
		print("Roll: ", self._roll)
		print("Branch: ", self._branch)


# derived class
class Geek(Student):

	# constructor 
	def __init__(self, name, roll, branch): 
         Student.__init__(self, name, roll, branch) 
		
	# public member function 
	def displayDetails(self):
         # accessing protected data members of super class 
         print("Name: ", self._name) 
		 # accessing protected member functions of super class 
         self._displayRollAndBranch()

# creating objects of the derived class	 
obj = Geek("Ali", 1706256, "Information Technology") 

# calling public member functions of the class
obj.displayDetails() 





"""
Private Access Modifier:
    The members of a class that are declared private are accessible within the class only, 
    Data members of a class are declared private by adding a double underscore ‘__’
"""

# program to illustrate private access modifier in a class

class Geek:
	
	# private members
	__name = None
	__roll = None
	__branch = None

	# constructor
	def __init__(self, name, roll, branch): 
		self.__name = name
		self.__roll = roll
		self.__branch = branch

	# private member function 
	def __displayDetails(self):
		# accessing private data members
		print("Name: ", self.__name)
		print("Roll: ", self.__roll)
		print("Branch: ", self.__branch)
	
	# public member function
	def accessPrivateFunction(self):
		# accessing private member function
		self.__displayDetails() 

	# getter method for name
	def get_name(self):
		self.__name 
        
	# setter method name
	def set_name(self , name):
		self.__name = name 

	# getter method for roll
	def get_roll(self):
		self.__roll
        
	# setter method roll
	def set_roll(self , roll):
		self.__roll = roll 

	# getter method for branch
	def get_branch(self):
		self.__branch
        
	# setter method branch
	def set_branch(self , branch):
		self.__branch = branch 

             
# creating object 
obj = Geek("Osama", 1706256, "Information Technology")

# calling public member function of the class
obj.accessPrivateFunction()

# class A(object): 
# 	def __init__(self, x): 
# 		self.x = x 
# 	
# 	def getX(self): 
# 		return self.X 
# 	
# class B(object): 
# 	def __init__(self, x, y): 
# 		self.x = x 
# 		self.y = y 
# 	def getSum(self): 
# 		return self.X + self.y 


# # inherits from A 
# class C_A(A): 
# 	def isA(self): 
# 		return True
# 	
# 	def isB(self): 
# 		return False


# # inherits from B 
# class C_B(B): 
# 	def isA(self): 
# 		return False
# 	
# 	def isB(self): 
# 		return True

# # return required Object of C based on cond 
# def getC(cond): 
# 	if cond: 
# 		return C_A(1) 
# 	else: 
# 		return C_B(1,2) 

# # Object of C_A 
# ca = getC(True) 
# print(ca.isA()) 
# print(ca.isB()) 
# 	
# # Object of C_B 
# cb = getC(False) 
# print(cb.isA()) 
# print(cb.isB()) 


class A(object): 
	def __init__(self, x): 
		self.x = x 
	
	def getX(self): 
		return self.X 

# Based on condition C inherits 
# from A or it inherits from 
# object i.e. does not inherit A 
cond = True

# inherits from A or B 
class C(A if cond else object): 
	def isA(self): 
		return True

# Object of C_A 
ca = C(1) 
print(ca.isA()) 


#######################################################
class CSStudent:
	stream = 'cse'				 # Class Variable (Static)
	def __init__(self,name,roll):
		self.name = name		 # Instance Variable
		self.roll = roll		 # Instance Variable

# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

print(a.stream) # prints "cse"
print(b.stream) # prints "cse"
print(a.name) # prints "Geek"
print(b.name) # prints "Nerd"
print(a.roll) # prints "1"
print(b.roll) # prints "2"

# Class variables can be accessed using class
# name also
print(CSStudent.stream) # prints "cse"


# To change the stream for all instances of the class we can change it 
# directly from the class
CSStudent.stream = 'mech'

print(a.stream) # prints 'mech'
print(b.stream) # prints 'mech'



# Defining parent class 
class Parent(): 
	
	# Constructor 
	def __init__(self): 
		self.value = "Inside Parent"
		
	# Parent's show method 
	def show(self): 
		print(self.value) 
		
# Defining child class 
class Child(Parent): 
	
	# Constructor 
	def __init__(self): 
		self.value = "Inside Child"
		
	# Child's show method 
	def show(self): 
		print(self.value) 
		
		
# Driver's code 
obj1 = Parent() 
obj2 = Child() 

obj1.show() 
obj2.show() 

print('################################################')

# Python program to demonstrate 
# calling the parent's class method 
# inside the overridden method 
class Parent(): 
	
	def show(self): 
		print("Inside Parent") 
		
class Child(Parent): 
	
	def show(self): 
		
		# Calling the parent's class 
		# method 
		Parent.show(self)    #or super().show()
		print("Inside Child") 
		
# Driver's code 
obj = Child() 
obj.show() 



def product(a, b):
	p = a * b
	print(p)

# Second product method
# Takes three argument and print their
# product


def product(a, b, c):
	p = a * b*c
	print(p)

# Uncommenting the below line shows an error
# product(4, 5)


# This line will call the second product method
product(4, 5, 5)


print('####################################################')

"""
Solution : Method 1 (Not The Most Efficient Method):
"""
# Function to take multiple arguments
def add(datatype, *args):

	# if datatype is int
	# initialize answer as 0
	if datatype == 'int':
		answer = 0

	# if datatype is str
	# initialize answer as ''
	if datatype == 'str':
		answer = ''

	# Traverse through the arguments
	for x in args:

		# This will do addition if the
		# arguments are int. Or concatenation
		# if the arguments are str
		answer = answer + x

	print(answer)


# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'Geeks')

print('####################################################')

"""
Solution : Method 2 (Not the efficient one):
"""
# code
def add(a=None, b=None):
	# Checks if both parameters are available
	# if statement will be executed if only one parameter is available
	if a != None and b == None:
		print(a)
	# else will be executed if both are available and returns addition of two
	else:
		print(a+b)


# two arguments are passed, returns addition of two
add(2, 3)
# only one argument is passed, returns a
add(2)

print('####################################################')

"""
Solution : Method 3 (Efficient One)
    By Using Multiple Dispatch Decorator 
    Multiple Dispatch Decorator Can be installed by: 
        
        conda install -c anaconda multipledispatch
"""

from multipledispatch import dispatch

# passing one parameter


@dispatch(int, int)
def product(first, second):
	result = first*second
	print(result)

# passing two parameters


@dispatch(int, int, int)
def product(first, second, third):
	result = first * second * third
	print(result)

# you can also pass data type of any value as per requirement


@dispatch(float, float, float)
def product(first, second, third):
	result = first * second * third
	print(result)


# calling product method with 2 arguments
product(2, 3) # this will give output of 6

# calling product method with 3 arguments but all int
product(2, 3, 2) # this will give output of 12

# calling product method with 3 arguments but all float
product(2.2, 3.4, 2.3) # this will give output of 17.985999999999997





