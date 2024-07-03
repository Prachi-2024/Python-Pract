print("Even numbers!")
num=2
while num<=10:
    print(num)
    num=num+2
print()

print("Odd numbers!")
num=1
while num<=10:
    print(num)
    num=num+2
print()

print("Natural numbers!")
num=1
while num<=10:
    print(num)
    num+=1
print()

print("Whole numbers!")
num=0
while num<=10:
    print(num)
    num+=1
print()

print("Numbers and its squares!")
num=1
while num<=10:
    print(num,num**2)
    num=num+1
print()

print("Print in gap of 10")
num=0
while num<=100:
    print(num,end=' ')
    num+=10
print()

print("reverse gap 5")
num=50
while num>0:
    print(num,end =' ')
    num=num-5
print()

print("Sum of 10 natural numbers!")
num=10
sum=0
while num>=1:
    sum=sum+num
    num=num-1
    print(sum, end=' ')
print()

print("Even numbers sum!")
num=2
sum=0
while num<=10:
    sum=sum+num
    num=num+2
    print(sum,end=' ')
print()
print("Even numbers sum starting from 10 to 2!")
num=10
sum=0
while num>=2:
    sum=sum+num
    num=num-2
    print(sum,end=' ')
print()

print("Table")
a=int(input("Enter the number of which you want multiplication table: "))
num=1
while num<=10:
    print(a,"X",num,"=",a*num)
    num+=1
print()

print("Prime number checking!")
pnum=int(input("Enter any number: "))
if pnum==0 or pnum==1:
        print("Not a Prime Number!")
else:
    for i in range(2,pnum+1):
        if pnum%i==0:
            print("Not a Prime Number!")
            break
        else:
            print("Yes, Prime number")
            break
        