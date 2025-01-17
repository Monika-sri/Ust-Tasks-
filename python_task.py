"""
1)Write a program which contains one class named as Demo.
That class contains one class variable as value
There are two instance methods of class as Fun and Gun which displays values of instance variables
Initialise instance variable in constructor by accepting the values from user
After creating the class create the two objects of Demo class as
Obj1 =Demo(11,21)
Obj2 = Demo(51,101)

Now call the instance methods as
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()"""

class Demo:
    value = 0
    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2
    def Fun(self):
        print(f"Value of no1 (instance variable) in Fun: {self.no1}")
    def Gun(self):
        print(f"Value of no2 (instance variable) in Gun: {self.no2}")
Obj1 = Demo(11, 21) 
Obj2 = Demo(51, 101)
Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()


"""
2)Write a program which contains one class named as BookStore.
Bookstore class contains two instance variables as Name , Author.
That class contains one class variable as NoofBooks which is initialize to 0
There is one instanace methods of class as Display which displays name, author and number of books.
Initialise instance variable in init method by accepting the values from user as name and author.
Inside init method increment value of NoOfBooks by one.
After creating the class create the two objects of BookStore class as
Obj1=Bookstore(“Linux System Programming”,”Robert Love”)
Obj1.Display()  # Linux System Programming. No of books : 1

Obj2=Bookstore(“C Programming”,”Robert Love”)
Obj2.Display()  # C Programming by Dennis Ritchie. No of books :2
"""

class Bookstore:
    NoofBooks=0
    def __init__(self,name,author):
        self.name = name
        self.author = author
        Bookstore.NoofBooks += 1
    def Display(self):
        print(f"{self.name}. No of books : {Bookstore.NoofBooks}")

Obj1=Bookstore("Linux System Programming","Robert Love")
Obj1.Display()

Obj2=Bookstore("C Programming","Robert Love")
Obj2.Display() 
        

"""
3)Write a program which contains one class named as Circle
Circle class contains three instance variables as Radius,Area ,Circumference.
That class contains one class variable as PI which is initialize to 3.14
Inside init method initialize all instance variables to 0.0
There are three instance methods inside class as Accept(), CalculateArea(), CalculateCircumference( ),
,Display( )
Accept method will accept value of Radius from user.
CalculateArea () method will calculate area of circle and store it into instance variable Area.
CalculateCircumference () method will calculate circumference of circle and store it into instance variable 
Circumference.
And Display( ) method will display value of all the instance variables as radius , Area , Circumference.
After designing the above class call all instance methods by creating multiple objects
"""

class Circle:
    PI = 3.14
    def __init__(self):
        self.radius=0
        self.area = 0
        self.circumference = 0
    def Accept(self,radius):
        self.radius = radius
        
    def CalculateArea(self):
        self.area = Circle.PI * radius ** 2
        
    def CalculateCircumference(self):
        self.circumference = 2 * Circle.PI * radius
        
    def Display(self): 
        print(f"radius is {self.radius} Area is {self.area} Circumference is {self.circumference}")
        
    
radius = float(input("enter the radius"))
obj1 = Circle()
obj1.Accept(radius)
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()
    


"""
4) Write a program which contains one class named as BankAccount.
BankAccount class contains two instance variables as Name & Amount.
That Class Contains one class variable as ROI which is initialize to 10.5
Inside init method initialize all name and amount variable by accepting the values from user.
There are four instance methods inside class as Display() , Deposit (), Withdraw( ), CalculateInterest()
Deposit( ) method will accept the amount from user and add that value in class instance variable Amount.
Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
CalculateInterst() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI
And Display () method will display value of all the instance variables as Name and Amount.
After designing the above class call all instance methods by creating multiple objects
"""

class BankAccount:
    ROI=10.5
    
    def __init__(self,name,amount):
        self.name = name 
        self.amount = amount
    def Deposit(self):
        deposit_amount = float(input("Enter the amount to deposit: "))
        self.amount += deposit_amount
        
    def CalculateInterest(self):
        interest = (self.amount * BankAccount.ROI) / 100
        print(f"the interest is {interest}")
        
        
    def Withdraw(self):
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        self.amount -= withdraw_amount
        
    def Display(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: {self.amount:.2f}")

account1 = BankAccount("Lohith", 15000.00)
account1.Display()
account1.Deposit()
account1.Withdraw()
account1.CalculateInterest()
account1.Display()

account2 = BankAccount("Kumar", 10000.00)
account2.Display()
account2.Deposit()
account2.Withdraw()
account2.CalculateInterest()
account2.Display()

 

"""
5)Write a program which contains one class named as Numbers.
 Arithmetic class contains one instance variables as Value.
 Inside init method initialize that instance variables to the value which is accepted from user.
There are four instance methods inside class as ChkPrime(), ChkPerfect() , SumFactors(), Factors().
ChkPrime() method will returns true if number is prime otherwise return false
ChkPerfect () method will returns true if number is perfect otherwise return false.
Factors () method will display all factors of instance variable.
SumFactors() method will return addition of all factors. Use this method in any another method
As a helper method if required.
After Designing the above class call all instance methods by creating multiple objects.
"""

class Numbers:
    def __init__(self, value):
        self.Value = value

    def ChkPrime(self):
        if self.Value < 2:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        return self.SumFactors() == self.Value

    def Factors(self):
        factors = [i for i in range(1, self.Value) if self.Value % i == 0]
        return factors

    def SumFactors(self):
        return sum(self.Factors())

num1 = Numbers(28)
print(num1.ChkPrime())
print(num1.ChkPerfect())
print(num1.Factors())
print(num1.SumFactors())


num2 = Numbers(28)
print(num2.ChkPrime())
print(num2.ChkPerfect())
print(num2.Factors())
print(num2.SumFactors())



"""
6)Write a program which contains one class named as Numbers.
Arithmetic class contains one instance variables as Value1,Value2.
Inside init method initialize all instance variables to 0.
There are three instance methods inside class as Accept(),Addition(),Subtraction(),Multiplication(),Division().
Accept method will accept value of value1 and value2 from user.
Addition() method will perform addition of Value1 and Value2 and return result.
Subtraction() method will perform subtraction of Value1 and Value2 and return result.
Multiplication() method will perform multiplication of Value1 and Value2 and return result.
Division() method will perform division of Value1 and Value2 and return result.
After Designing the above class call all instance methods by creating multiple objects.
"""

class Numbers:
    def __init__(self):
        self.x = 0
        self.y = 0

    def Accept(self):
        self.x = float(input("Enter the first value (x): "))
        self.y = float(input("Enter the second value (y): "))

    def Addition(self):
        return self.x + self.y

    def Subtraction(self):
        return self.x - self.y

    def Multiplication(self):
        return self.x * self.y

    def Division(self):
        if self.y == 0:
            return "Division by zero is not allowed"
        return self.x / self.y



obj1 = Numbers()
obj1.Accept()
print(f"Addition: {obj1.Addition()}")
print(f"Subtraction: {obj1.Subtraction()}")
print(f"Multiplication: {obj1.Multiplication()}")
print(f"Division: {obj1.Division()}")



obj2 = Numbers()
obj2.Accept()
print(f"Addition: {obj2.Addition()}")
print(f"Subtraction: {obj2.Subtraction()}")
print(f"Multiplication: {obj2.Multiplication()}")
print(f"Division: {obj2.Division()}")
