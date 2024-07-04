# # Try: This block will test the excepted error to occur
# # Except:  Here you can handle the error
# # Else: If there is no exception then this block will be executed
# # Finally: Finally block always gets executed either exception is generated or not

# print("zero division error")
# try:
#     num=float(input("Enter any number here: "))
#     divi=float(input("Enter number you want to divide with num: "))
#     print(num/divi)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# print()

# print("Multiple statements!")
# try:
#     x = int(input("Enter a number: "))
#     result = 10 / x
# except ZeroDivisionError:
#     print("You cannot divide by zero.")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# except Exception as e:
#     # by this , we can know the error type occuring
#     print(f"An error occurred: {e}")
# else:
#     print("Yes, Your result is:",result)
# finally:
#     print("This will always be executed whether an exception has occured or not!!")
# print()

# # Yes, you can use finally without try-except in Python. The primary purpose of finally is to execute cleanup code
# # that should run regardless of whether an exception occurred or not. 
# # If there is no try block to catch exceptions, 
# # the finally block will still execute after other code in the program finishes execution.

# print("raise valuerror")
# try:
#     amount=int(input("Enter amount:"))
#     if amount<2000:
#         raise ValueError("Low balance!")
#     else:
#         print("Yes you can take the money!")
# except ValueError as e:
#     print(e)
# print()


print("if condition using not....")
str="abcdefghi"
str1="deft"
if not str1 in str :
    print("substring is not present in string")
else:
    print("substring is present in string")
print()

print("if condition without using not....")
str="abcdefghi"
str1="deft"
if str1 in str :
    print("substring is present in string")
else:
    print("substring is not present in string")
print()

print("args")
def function(*args):
    print(sum(args))
function(5,10)
function(50,100,20,20,10)
print()

print("kwargs")
def func(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
func(first='prachi',second='shah')
print()

print("both args kwargs")
def func(*args,**kwargs):
        print("args:",args)
        print("kwargs:",kwargs)
func('prachi','shah',first='prachi',second='shah')
print()

print("oops args")
class Car():
    # args receives unlimited no. of arguments as an array
    def __init__(self, *args):
        self.speed = args[0]
        self.color = args[1]
audi = Car(200, 'red')
bmw = Car(250, 'black')
print(audi.color)
print(bmw.speed)
print()

print("sum of multiple numberss:")
def num(*numbers):
    result=0
    for n in numbers:
        result=n+result
    print(result)
num(1,2)
num(1,2,3,4,5,6,7,8,9,10)
num(12,23,4,6,8,7,787,12)
num(0,1,23,233432,43,4)
print()


