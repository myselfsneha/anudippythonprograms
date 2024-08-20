Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
5+2*4
13
a=int(input("enter the first number:"))
enter the first number:12
b=int(input("enter the second number:"))
enter the second number:50
multiplication=a*b
sum=a+b
print("multiplication of two nos is:",multiplication)
multiplication of two nos is: 600
print("sum of two nos is:",sum)
sum of two nos is: 62
a=12
b=50
if(a>b):
    print("a is greatest",a)
else:
    print("b is greatest",b)

    
b is greatest 50
celsius=int(input("enter the temperature to be calculated:"))
enter the temperature to be calculated:11
fahrenheit=(9/5)*celsius+32
print("temperature in fahrenheit is:",fahrenheit)
temperature in fahrenheit is: 51.8
9/5
1.8
1.8*11
19.8
19.8+32
51.8
a=3
b=6
c=9
h=int(input("enter the height of the triangle is:"))
enter the height of the triangle is:12
b=int(input("enter the base of the triangle is:"))
enter the base of the triangle is:15
print("area of triangle is:",area)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print("area of triangle is:",area)
NameError: name 'area' is not defined
area=1/2*(b*h)
print("area of triangle is:",area)
area of triangle is: 90.0
12*15
180
180/2
90.0
s=(a+b+c)/2
import sqrt
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    import sqrt
ModuleNotFoundError: No module named 'sqrt'
import math.sqrt
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    import math.sqrt
ModuleNotFoundError: No module named 'math.sqrt'; 'math' is not a package
import math
area=sqrt(s(s-a)(s-b)(s-c))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    area=sqrt(s(s-a)(s-b)(s-c))
NameError: name 'sqrt' is not defined
math.sqrt(area)
9.486832980505138
area=s*(s-a)*(s-b)*(s-c)
math.sqrt(area)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    math.sqrt(area)
ValueError: math domain error
import math
area=s*(s-a)*(s-b)*(s-c)
math.sqrt(area)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    math.sqrt(area)
ValueError: math domain error
>>> a=3
>>> b=6
>>> c=9
>>> s=(a+b+c)/2
>>> area=(s*(s-a)*(s-b)*(s-c))**0.5
>>> print("area of triangle is %0.2f",%area)
SyntaxError: invalid syntax
>>> print("area of triangle is %0.2f",area)
area of triangle is %0.2f 0.0
>>> %area=(s*(s-a)*(s-b)*(s-c))**0.5
SyntaxError: invalid syntax
>>> area=(s*(s-a)*(s-b)*(s-c))**0.5
>>> print(area)
0.0
>>> a=s*(s-a)*(s-b)*(s-c)
>>> area=a**0.5
>>> print(area)
0.0
>>> a+b+c
15.0
>>> 15.0/2
7.5
>>> 7.5-3
4.5
>>> 7.5-6
1.5
>>> 7.5-9
-1.5
>>> 7.5*4.5*1.5*(-1.5)
-75.9375
>>> (-75.9375)**0.5
(5.335916240344407e-16+8.714212528966687j)
>>> a=24
>>> b=43
>>> c=45
>>> s=(a+b+c)/2
>>> area=(s*(s-a)*(s-b)*(s-c))**0.5
>>> print(area)
506.217344625804
