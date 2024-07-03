# print("Rectangle!")
# rows=int(input("Enter the number of rows you want: "))
# cols=int(input("Enter the number of columns you want: "))
# for i in range(1,rows+1):
#     for j in range(1,cols+1):
#         print("*",end=' ')
#     print("")
# print()

# print("Right angled triangle star!")
# rows=int(input("Enter the number of rows you want: "))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print("*",end=' ')
#     print("")
# print()

# print("Reversed right triangle!")
# rows=int(input("Enter number of rows you want:"))
# for i in range(rows,0,-1):
#     print()
#     for j in range(0,i):
#         print("*",end=' ')

# print("Right angled triangle particular number!")
# rows=int(input("Enter the number of rows you want: "))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print("1",end=' ')
#     print("")
# print()

# print("Right angled with odd cols!")
# rows=int(input("Enter the number of rows you want: "))
# n=1
# for i in range(1,rows+1):
#     for j in range(1,n+1):
#         print("*",end=' ')
#     print("")
#     n=n+2
# print()

# print("Pyramid")
# rows=5
# for i in range(0,rows):
#     for j in range(rows-i-1):
#         print(end=' ')
#     for j in range(0,i+1):
#         print("*",end=' ')
#     print()

# print("Pyramid")
# rows=5
# for i in range(0,rows):
#     for j in range(rows-i-1):
#         print(end=' ')
#     for j in range(0,2*i+1):
#         print("*",end=' ')
#     print()

# print("Reverse Pyramid")
# rows=5
# for i in range(rows,0,-1):
#     for j in range(0,rows-i):
#         print(end=' ')
#     for j in range(0,i):
#         print("*",end=' ')
#     print()

# print(" Diamond Pyramid")
# rows=5
# rows=5
# for i in range(0,rows):
#     for j in range(0,rows-i-1):
#         print(end=' ')
#     for j in range(0,i+1):
#         print("*",end=' ')
#     print()
# for i in range(rows-1,0,-1):
#     for j in range(0,rows-i):
#         print(end=' ')
#     for j in range(0,i):
#         print("*",end=' ')
#     print()

# print("Hollow triangle")
# rows=int(input("Enter number of rows you want: "))
# for i in range(0,rows):
#     for j in range(0,rows):
#         if i==0 or j==rows-1 or i==j:
#             print("*",end='')
#         else:
#             print(end=' ')
#     print()

# print("right triangle")
# rows=int(input("Enter rows:"))
# for i in range(1,rows+1):
#     print('')
#     for j in range(1,i+1):
#         print(i+j,end='')


# print("triangle")
# for row in range(1,5):
#     for col in range(1,5):
#         if col>=5-row:
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()

# print("triangle")
# for row in range(1,5):
#     for col in range(1,5):
#         if col<=5-row:
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()

print("triangle")
for row in range(1,5):
    for col in range(1,5):
        if col>=row:
            print("*",end='')
        else:
            print(" ",end='')
    print()