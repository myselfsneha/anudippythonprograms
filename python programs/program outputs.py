Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("helloworld")
helloworld
print('helloworld')
helloworld
def my_function():
    local_variable=10
    print(local_variable)
my_function()
SyntaxError: invalid syntax
def my_function():
    local_variable=10
    print(local_variable)
    my_function()

    

================ RESTART: C:/Users/SNEHA SINGH/local variable.py ===============
10
>>> 
=============== RESTART: C:/Users/SNEHA SINGH/global variable.py ===============
Traceback (most recent call last):
  File "C:/Users/SNEHA SINGH/global variable.py", line 4, in <module>
    life()
NameError: name 'life' is not defined. Did you mean: 'slice'?
>>> 
=============== RESTART: C:/Users/SNEHA SINGH/global variable.py ===============
7
>>> 
============== RESTART: C:/Users/SNEHA SINGH/indentation error.py ==============
>>> 
== RESTART: C:/Users/SNEHA SINGH/global and local variables with same name.py ==
I love Geeksforgeeks
>>> 
== RESTART: C:/Users/SNEHA SINGH/global and local variables with same name.py ==
I love my India
>>> 
== RESTART: C:/Users/SNEHA SINGH/global and local variables with same name.py ==
global :  1
Inside f() :  1
global :  1
Inside g() :  2
global :  1
Inside h() :  3
global :  3
>>> 
============ RESTART: C:/Users/SNEHA SINGH/string, int and float.py ============
Enter your name:sneha
Enter your age:20
Enter your marks:89
The name is: sneha
The age is: 20
The marks is: 89.0
>>> 
================== RESTART: C:/Users/SNEHA SINGH/helloworld.py =================
helloworld
helloworld
