Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n=2
while(n<=10):
    if(n%2==0):
        print(n)
    n=n+1

    
2
4
6
8
10
def is_palindrome(string):
  string = string.replace(" ", "").lower()
  return string == string[::-1]
input_string = input("Enter a string: ")
if is_palindrome(input_string):
  print("The string is a palindrome.")
else:
  print("The string is not a palindrome.")
  
SyntaxError: invalid syntax
def is_palindrome(string):
    string=string.replace(" ","").lower()
    return string==string[::-1]
... input_string=input("enter a string:")
SyntaxError: invalid syntax
>>> 
==================== RESTART: C:/Users/SNEHA SINGH/QQQQ2.py ====================
Enter a string: sneha
The string is not a palindrome.
>>> 
==================== RESTART: C:/Users/SNEHA SINGH/QQQQ2.py ====================
Enter a string: sahas
The string is a palindrome.
>>> 
==================== RESTART: C:/Users/SNEHA SINGH/QQQQ2.py ====================
Enter a string: sneha
The string is not a palindrome.
>>> for num in range(1, 11):
...   print(num)
... 
...   
1
2
3
4
5
6
7
8
9
10
>>> 
==================== RESTART: C:/Users/SNEHA SINGH/QQQQ2.py ====================
Enter a number: 24
24 is not an Armstrong number
>>> 
==================== RESTART: C:/Users/SNEHA SINGH/QQQQ2.py ====================
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
>>> 
==================== RESTART: C:\Users\SNEHA SINGH\lab-10.py ===================
Enter your password: Yashasvi@2428sneha
Invalid password
