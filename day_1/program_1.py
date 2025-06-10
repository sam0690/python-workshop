"""
print("Hello world !!")

user_name = input("What is your name ???")
print(f"Timro naam {user_name} ho")


for i in range(5):
    print(i+1)
"""


#calculator
"""
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0 :
        return "division by 0 is not possible"
    return  x / y 

print("Select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


choice = input("Enter the operation you want to perform")

try:
    num1 = float(input("Enter the 1st number : "))
    num2 = float(input("Enter the 2nd number : "))
    
    if(choice == "1"):
        print("Result is : ", add(num1,num2))
    elif(choice == "2"):
        print("Subtraction result is  : ", subtract(num1,num2))
    elif(choice == "3"):
        print("Multiplication result is : ", multiply(num1,num2))
    elif(choice == "4"):
        print("Division result is : ", divide(num1,num2))
    else:
        print("Invalid input")
except ValueError:
    print("Invalid number entered")
"""

#even or odd
"""def check(a):
    if (a%2 == 0):
        print("The number is even")
    else :
        print("The number is odd")
    

num = int(input("Enter a number you want to check : "))
check(num) """

#square of number 
"""def sq(a):
    return pow(a,2)

num = int(input("Enter the number you want to square : "))

print("The square of the number is ",sq(num))"""


#max of 3 number 
"""def high(a,b,c):
    print("the max number is : ",max(a,b,c))


high(2,3,4)
"""

#guessnumber

"""import random
import math

x = random.randint(0,1000)

total_Chances = math.ceil(math.log(1000 - 1,2))

print(f"You have {total_Chances} to guess the number .")
flag = False
guess_count = 0

while guess_count < total_Chances:
    guess_count+=1
    guess = int(input("Guess your number : "))
    if x == guess:
        print("congratulation !! You guessed right")
        flag = True 
    elif x > guess:
        print("You guessed low")
        flag = False
    elif x < guess:
        print("you guessed high")
        flag = False


if not flag:
    print("\n The number is : ",x)
    print("\n Better luck next time : (")
"""

#lists
"""fruits = ["apple","mango","banana","litchi"]
for fruit in fruits:
    print(fruit)
"""
#dictionary
"""my_dict = {
    "name" : "HAri",
    "Age":99,
    "subjects":{"math","english"},
}

print(my_dict["Age"])
"""
"""student = {
    'name':'Oscar Bob',
    'marks':10000,
    'hobbies':("reading",'chessing'),
    'skills':{'juggling','clown'},
}

print(student['name'].upper())
"""
#class and constructors and objects

"""class Person:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        
    def display(self):
        print(f"Hello my name is {self.name} and id is {self.id}")

user = Person(12,"SAM")
user.display()
"""

#inheritance polymorphism abstraction
"""class Car:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop

    def ignition(self):
        print("Car started")

    def stopping(Self):
        print("Car has stopped")

class volvo(Car):
    def __init__(self, start, stop,stall):
        super().__init__(start, stop)
        self.stall = stall
        print(f"car has {self.stall}")

my_car = volvo("started","stopped","stalled")
my_car.ignition()
"""
"""class shape:
    def area(self):
        pass

class Square(shape):
    def __init__(self,side):
        super().__init__()
        self.side  = side

    def area(self):
        return self.side**2
class circle(shape):
    def __init__(self,side):
        super().__init__()
        self.side = side
    def area(self):
        return 3.17*self.side**2
shapes= [Square(2),circle(5)]

for shape in shapes:
    print(f"{shape.__class__.__name__} Area: {shape.area():.2f}")
"""