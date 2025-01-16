#!/usr/bin/python
"""
purpose: print() function synatc and usage
"""
name = "Almighty" # stg
print(name)
print("name")

#print("name1"=name)
print()

print("Name of the student is =" , name)
print("Name of the student is" + name) #str concatination
print("Name of the student is " + name)
print("Name of the student is ", name)

#eg -2

print(1,2,3,4,5,6) #default sep=''
print(1,2,3,4,5,6, sep="~")
print(1,2,3,4,5,6, sep="-")
print(1,2,3,4,5,6, sep=":")

#note: python is a dynamic types language
name = 1232
print("Name of the student is", name)

#print("Name of the student is" + name) #stg and int can not concate

#note: python is s strictly typed language
print("1 +2            =", 1+2)
print("'1' +'2'  =", "1"+"2")

#1+'2' is type error : unsuppprted operand types for +: int and str
# so we can use types converters -str(),int(),float()

print("1 +int('2') =", 1+int("2"))
print("str(1) + '2' =", str(1)+ '2')

print("Name of the student is" + str(name))
print("Name of the student is" +" " +str(name))
