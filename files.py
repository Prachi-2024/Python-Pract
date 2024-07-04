# f=open("file_1.txt","x")            
# x is used to create an empty file if file is not present in the folder 
# you cannot create a file with the same name 


# f=open("file_1.txt","r")  
# data=f.read()     
# print(data)     
# r is used to read the content of the file mentioned, if there is no such file , it will raise an error.
# if we dont write "r" output will be the same, it will read that file mentioned.

# f=open("file_1.txt","w")  
# f.write("Welcome to MMT")
# whatever will be written will be written in that file and the old content will get erased
# if file doesnot exists, it will create one

# f=open("file_1.txt","r+") 
# f.write("hi")           it will remove first 2 letters from the statement from starting as cursor is at beginning
# print(f.read()) 
# f.write("Have a seat..")
# it will read the file first and then write the other print statement in tet file without erasing the previous
# r+ is used for both read and write
# use first read and then write

#print(f.tell())  will show the cursor position ,file pointer

# r+ will show an error if the file doesnot exist but w+ will create a new file if it doesnot exists.


f=open("file_1.txt","w+")
print(f.tell())
f.write("hello")
print(f.tell())
f.seek(0)
print(f.tell())
data=f.read()
print(data)
print(f.tell())
f.close()
# seek is used to move the cursor

# "a" = append mode , that is print statement will be written at the end of the line
# if you want to read in append(write)mode , use "a+"
# in a+ mode, cursor will be at the end of the line , hence use seek(0)

# rb,wb,rb+,wb+.... used to read and write any binary file

# import os
# os.remove("demofile.txt")


# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")


# to delete entire folder
# import os
# os.rmdir("myfolder")

