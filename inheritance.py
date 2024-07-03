# class Person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname

#     def Display(self):
#         print(self.firstname,self.lastname)
# a=Person("Prachi","Shah")
# a.Display()

# class Employee(Person):
#     def isEmployee(self):
#         return True

# a=Employee("Prachi","Shah")
# print(a.isEmployee())

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def circle_area(self):
        return self.radius*2*3.14
    
    def circle_perimeter(self):
        return self.radius*self.radius*3.14
    
c=Circle(7)
print("Area of a circle is:",c.circle_area())
print("Perimeter of a circle is:",c.circle_perimeter())

class Calculator:
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def mul(self,x,y):
        return x*y
    def div(self,x,y):
        return x/y
a=Calculator()
print("Addition:",a.add(5,5))
print("Subtraction:",a.sub(5,4))
print("Division:",a.div(4,2))
print("Multiplication:",a.mul(3,3))

print()
print("Shopping sc")

class Shoppingcart:
    def __init__(self,name="prachi"):
        
        self.items=[]

    def additem(self,itemname,qty):
        items=(itemname,qty)
        self.items.append(items)

    def removeitem(self,itemname):
        for items in self.items:
            if items[0]==itemname:
                self.items.remove(items)
                break

    def calculate_total(self):
        total = 0
        for items in self.items:
            total += items[1]
        return total

sc=Shoppingcart()
sc.additem("Burger",2)
sc.additem("Orange",3)
sc.additem("Mango",1)
sc.additem("Pizza",5)
sc.additem("Sandwich",6)

print("Current Items in sc:")
for items in sc.items:
    print(items[0], "-", items[1])

total_qty = sc.calculate_total()
print("Total Quantity:", total_qty)

sc.removeitem("Orange")
print("\nUpdated Items in sc after removing Orange:")
for items in sc.items:
    print(items[0], "-", items[1])

total_qty = sc.calculate_total()
print("Total Quantity:", total_qty) 

print()
print("bank system")

class Bank:
    def __init__(self):
        self.customers={}

    def create_acc(self,accno,balance=0):
        if accno in self.customers:
            print("Account number already exists!!")
        else:
            self.customers[accno]=balance
            print("Account created succesfully...")

    def deposit(self,amount,accno):
        if accno in self.customers:
            self.customers[accno]+=amount
        else:
            print("Account doesnot exists!")

    def withdraw(self,amount,accno):
        if accno in self.customers:
            if self.customers[accno]>=amount:
                self.customers[accno]-=amount
            else:
                print("Less balance!")
        else:
            print("Account doesnot exists!")

    def check_balance(self, accno):
        if accno in self.customers:
            balance = self.customers[accno]
            print(f"Account balance: {balance}")
        else:
            print("Account number does not exist.")


b=Bank()
b.create_acc("Acc1",0)
b.create_acc("Acc2",0)
b.deposit(100,"Acc3")
b.deposit(50000,"Acc1")
b.withdraw(6000,"Acc1")
b.withdraw(15000,"Acc1")
b.check_balance("Acc1")
