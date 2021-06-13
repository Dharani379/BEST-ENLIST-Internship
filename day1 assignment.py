Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("30 days 30 hours challenge")
30 days 30 hours challenge
>>> #assigning variables to strings
>>> hours ="thirty"
>>> print(hours)
thirty
>>> days ="thirty days"
>>> print(days)
thirty days
>>> print(days[0])
t
>>> print(days[7])
d
>>> print(days[-1])
s
>>> challenge =" i will win"
>>> print(challenge[1:10])
i will wi
>>> print(challenge[1:3)
      
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> print(challenge[1:3])
i 
>>> print(challenge[1:2])
i
>>> print(challenge[2:3])
 
>>> print(challenge[0])
 
>>> print(challenge[11])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(challenge[11])
IndexError: string index out of range
>>> #converting string to lower characters
>>> CHALLENGE = "I WILL WIN"
>>> print(challenge.lower())
 i will win
>>> challenge = this is Dharani
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    challenge = this is Dharani
NameError: name 'this' is not defined
>>> challenge = thisis Dharani
SyntaxError: invalid syntax
>>> challenge = " this is Dharani"
>>> print(challenge.upper())
 THIS IS DHARANI
>>> # string concatenation
>>> a = " 30 days"
>>> b = " 30 hours"
>>> c = a+b
>>> print(c)
 30 days 30 hours
>>> a = " hello"
>>> b = "everyone"
>>> c = "this is"
>>> d = "Dharani"
>>> x = a+b+c+d
>>> print(x)
 helloeveryonethis isDharani
>>> # casefold() usage
>>> text ="thirty days and thirty hours"
>>> x=text.casefold()
>>> print(x)
thirty days and thirty hours
>>> work ="coding"
>>> x= text
>>> print(x)
thirty days and thirty hours
>>> text ="HELLO BUDDIES"
>>> x=text.casefold()
>>> print(x)
hello buddies
>>> # casefold returns the string into lower cased letters string
>>> best friend =" Nanditha Shetty"
SyntaxError: invalid syntax
>>> bestfriend ="Nanditha  shetty"
>>> x=text.capitalize()
>>> print(x)
Hello buddies
>>> x=bestfriend.capitalize()
>>> print(x)
Nanditha  shetty
>>> bestie="nanditha SHETY"
>>> x=bestie.capitalize()
>>> print(x)
Nanditha shety
>>> #capitalize() func capitalizes thebfirst letter of a string while remaing to lower case
>>> text="don't trouble trouble until the trouble troubles you"
>>> x=text.find()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    x=text.find()
TypeError: find() takes at least 1 argument (0 given)
>>> x=text.find(6))
SyntaxError: unmatched ')'
>>> x= text.find((6))
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    x= text.find((6))
TypeError: must be str, not int
>>> x=text.find([6])
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    x=text.find([6])
TypeError: must be str, not list
>>> x=text.find(6)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    x=text.find(6)
TypeError: must be str, not int
>>> x=text.find()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    x=text.find()
TypeError: find() takes at least 1 argument (0 given)
>>> x=text.find(" trouble")
>>> print(x)
5
>>> text="don't trouble trouble until the trouble troubles you"
>>> x=text.isalpha()
>>> print(x)
False
>>> #is alpha returns true is all the characters are alphabets false otherwise
>>> #is alnum returnd true if the string id alpha numeric i.e string contains both alphabets and numerics false othrwise
>>> text="don't trouble trouble until the trouble troubles you 547"
>>> x=text.isalnum()
>>> print(x)
False
>>> text="don't trouble trouble until the trouble troubles you"
>>> x=text.isalnum()
>>> print(x)
False
>>> text="don't trouble trouble until the trouble troubles you 541,7,4"
>>> x=text.isalnum()
>>> print(x)
False
>>> 