Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #creating a list of n numbers
>>> n=5
>>> L=[1,23,4,6,9]
>>> L=L*n
>>> print(L)
[1, 23, 4, 6, 9, 1, 23, 4, 6, 9, 1, 23, 4, 6, 9, 1, 23, 4, 6, 9, 1, 23, 4, 6, 9]
>>> #adding an item tothe list
>>> L.append(5)
>>> print(L)
[1, 23, 4, 6, 9, 1, 23, 4, 6, 9, 1, 23, 4, 6, 9, 1, 23, 4, 6, 9, 1, 23, 4, 6, 9, 5]
>>> del.L[6:-1]
SyntaxError: invalid syntax
>>> del L[6:-1]
>>> print(L)
[1, 23, 4, 6, 9, 1, 5]
>>> #storing the largest number of list to a var
>>> x=max(L)
>>> print(x)
23
>>> Y=min(L)
>>> print(Y)
1
>>> #creating a tuple and printing reverse of it
>>> T=(3,8,'hey','hi',5,76,'A','b')
>>> print(T)
(3, 8, 'hey', 'hi', 5, 76, 'A', 'b')
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> print(T)
SyntaxError: invalid syntax
>>> def Reverse(tuples):
	new_tup = tuples[::-1]
	return new_tup
tuples = ('z','a','b','o','n')
SyntaxError: invalid syntax
>>> #creating a tuple
>>> x=('hey','hi',1,3)
>>> y=reversed(x)
>>> print(tuple(y))
(3, 1, 'hi', 'hey')
>>> #Creting a tuple and Converting a tuple to list
>>> X=(1,2,'hello','world')
>>> type(X)
<class 'tuple'>
>>> x=list(X)
>>> type(x)
<class 'list'>
>>> print(x)
[1, 2, 'hello', 'world']
>>> #today's task completed