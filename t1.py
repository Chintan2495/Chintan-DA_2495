# Lecture 1

# print( "Hello Chintan")
# print("I am from Anand")
# print("Welcome to Data Analytics")


# name=input("your name")
# age=input("your age")
# print( "my name is",name)
# print( "my age is",age)


# name=input("enter name:")
# course=input("enter course:")
# fees=input("enter fees:")
# print(name,course,fees)

# student_name= "Chintan"
# marks= 80
# passed= True
# print(student_name)
# print(marks)
# print(passed)


# a=10
# b=20
# c=30
# a,b=b,a
# print("a=",a)
# print("b=",b)


# num=10
# decimal=5.5
# text="Data Analytics"
# status= True
# print(int(num))
# print(float(decimal))
# print(str(text))
# print(bool(status))

# x=10
# y=5.5
# result=x+y
# print(result)
# print(float(result))

# num1=float(input("enter first number"))
# num2=float(input("enter second number"))
# print("addition=", num1 + num2)
# print("substraction=", num1 - num2)
# print("multiplicationn=", num1 * num2)
# print("divison=", num1 / num2)
# print("modulus=", num1 % num2)



# a=input("enter true/false:")=="true"
# b=input("enter true/false:")=="true"
# print("AND=", a and b)
# print("OR=", a or b)
# print("NOT A=", not a)

# num=int(input("enter number"))
# num +=5
# print("after +=5",num)
# num-=2
# print("after -=2",num)
# num *=3
# print("after *=3",num)


# text=input("enter string: ")
# char=input("enter character: ")
# print(char in text)


# a=[1,2,3]
# b=a
# c=[1,2,3]
# print(a is b)
# print(a is not c)


# Lecture 2

# num=int(input("enter the number:"))
# if num % 2 == 0:
#     print("even number")
# else:
#     print("odd number") 


# number=float(input("enter the number:"))
# if number>0:
#     print("positive")
# elif number<0:
#     print("negative")
# else:
#     print("zero")






# Lecture 3

# For Loop
# for i in range(101):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# for i in range(1,8,2):
#     print(i)


# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)

# total = 0
# for i in range(1, 6):
#     total += i
# print(total)










    

# Lecture 4

# integer
# age = 20
# print(age + 5)

# name = "Rahul"
# # print(name + 5)



# age = 22
# marks = 95
# print(type(age))
# print(type(marks))


# a = 10
# b = 3
# print(a + b)   # Addition
# print(a - b)   # Subtraction
# print(a * b)   # Multiplication
# print(a / b)   # Division
# print(a % b)   # Modulus


# price = 199.99
# temperature = 36.7
# print(type(price))


# name = "Python"
# city = 'Ahmedabad'
# print(name)
# print(city)



# string indexing
# word = "Python"
# print(word[0])
# print(word[1])
# print(word[2])
# print(word[3])
# print(word[4])
# print(word[5])

# negative indexing
# word = "Python"
# print(word[-1])
# print(word[-2])
# print(word[-3])
# print(word[-4])
# print(word[-5])
# print(word[-6])

# string method upper
# name = "python"
# print(name.upper())

# string method lower
# name = "PYTHON"
# print(name.lower())


# string replace
# text = "I like data analytics"
# print(text.replace("data analytics", "Python"))




# Boolean 
# is_student = True
# print(type(is_student))


# comparison
# age = 20
# print(age >= 18)


# LIST
# fruits = ["Apple", "Banana", "Mango"]
# print(fruits[2])
# print(fruits[1])

# Modify List
# fruits = ["Apple", "Banana", "Mango"]
# fruits[1] = "Orange"
# fruits[0] = "kiwi"
# print(fruits)


# List Method
# Append, reomove, pop

# fruits = ["Apple", "Banana", "Mango"]
# fruits.append("Grapes")
# fruits.remove("Apple")
# fruits.pop(1)
# print(fruits)

# Tuple
# colors = ("Red", "Green", "Blue")
# print(colors)


# # SET
# numbers = {1,2,3,4,5,6,5,4,6,3}        
# print(numbers)


# ADD
# numbers = {1,2,3,3,4}
# numbers.add(10)
# print(numbers)


# remove
# numbers = {1,2,3,3,4}
# numbers.remove(2)
# print(numbers)


# dictionary (dict)

# student = {
#     "name": "Vansh",
#     "age": 25,
#     "city": "Ahmedabad"
# }
# print(student["name"])
# # print(student["age"])
# # print(student["city"])


# Add, Update

# student = {
#     "name": "Rahul",
#     "age": 21,
#     "city": "Delhi"
# }
# student["marks"] = 95
# student["age"] = 22
# print(student)



# # Type Checking
# x = 10
# print(type(x))

# y = "Hello"
# print(type(y))

# Type Conversion
# string to integer

# age = "25"
# new_age = int(age)
# print(new_age + 5)

# integer to String
# num = 100
# text = str(num)
# print(text)

# # integer to float
# x = 10
# print(float(x))

# float to integer
# price = 99.99
# print(int(price))

# Dynamic Typing in Python
# x = 10
# print(type(x))

# x = "Python"
# print(type(x))


# Nested Data Types
# student = {
#     "name": "Rahul",
#     "marks": [80, 90, 70]
# }
# print(student["marks"][0])




# Real-Life Example
# employee = {
#     "name": "Rahul",
#     "age": 22,
#     "salary": 35000.50,
#     "skills": ["Excel", "SQL", "Power BI"],
#     "is_working": True
# }
# print(employee)



# Mixing String and Integer
# age = "20"
# print(int(age) + 5)

# Task 1
# name= "chintan"
# age=30
# percentage= 85.5
# is_pass= True

# print(type(name))
# print(type(age))
# print(type(percentage))
# print(type(is_pass))

# Task 2
# cities = ["Ahmedabad", "Baroda", "Surat","Jamnagar"]
# cities[2]= "Bhavnagar"
# print(cities)


# Task 3
# student = {
#     "name": "Rahul",
#     "age": 21,
#     "city": "Delhi"
# }
# print(student["name"])


# Task 4
# a= int("100")
# print(a)
# print(type(a))








































