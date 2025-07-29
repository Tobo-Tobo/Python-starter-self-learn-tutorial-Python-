#Hello, welcome to your first lesson of python. We will be learning: Variables, data types
#你好，欢迎来到你的第一节Python课程。我们将学习：变量，数据类型

#There are 4 types of data(use majority), including: 
# int(integer: hole number that isn't a fraction)
# str(string: string is a sequence of characters enclosed in single (') or double (") quotes)
# float(float: a number that includes a decimal)
# bool(boolean: It contains true or false and usually is used in loops which you will learn later on)

#数据有四种类型(重要的那些)，包括：
# # int（整数：不是小数的整数）
# # str（字符串：字符串是包含在单引号（'）或双引号（"）
# float（浮点数：包含小数的数字）
# # bool（布尔值：包含真或假，通常用于循环，您稍后会学习这一点）

#when using print("hello world") the hello world will be a string(the computer classify everything as a string at first)
#使用 print("hello world") 时，hello world 将被视为一个字符串（计算机最初将一切都分类为字符串）
print("hello world")

#These are the follow data type added to each variable. Variables are those that can be changed while
#这些是添加到每个变量的后续数据类型。变量是那些可以在运行时改变的。

Test = 5
Test1 = False
Test2 = "Hello world"
Test3 = 5.44
#in order to check the data type you could enter the following:
#为了检查数据类型，您可以输入以下内容:

print(type(Test))
print(type(Test1))
print(type(Test2))
print(type(Test3))

#int(): Converts a value to an integer.
#float(): Converts a value to a floating-point number.
#str(): Converts a value to a string.
#int(): 将值转换为整数。
# #float(): 将值转换为点数。
# #str(): 将值转换为字符串。

# Integer to float
print(float(3)) # Output: 3.0

# Float to integer
print(int(3.9)) # Output: 3

# String to integer
print(int('123')) # Output: 123