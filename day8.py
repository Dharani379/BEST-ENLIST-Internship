>>> dict1={"name":"siva","class":"5","age":"14"}
>>> dict2={"school":"srinivasa","loc":"prathipadu","rank":"86","a":"[1,3,4,6]"}
>>> dict3={**dict1,*dict2}
SyntaxError: invalid syntax
>>> dict3={**dict1,**dict2}
>>> print(dict3)
{'name': 'siva', 'class': '5', 'age': '14', 'school': 'srinivasa', 'loc': 'prathipadu', 'rank': '86', 'a': '[1,3,4,6]'}
>>> #sorting the value and converting it to list
>>> num=[67,5,45,9,75,6,4,3,56]
>>> num.sort()
>>> print(num)
[3, 4, 5, 6, 9, 45, 56, 67, 75]
>>> num=set(num)
>>> print(num,"is of",type(num),"type")
{3, 4, 5, 6, 67, 9, 75, 45, 56} is of <class 'set'> type
>>> print(dict2)
{'school': 'srinivasa', 'loc': 'prathipadu', 'rank': '86', 'a': '[1,3,4,6]'}
>>> #3.to list no.of items in a dict key and sorting them
>>> print(dict2)
{'school': 'srinivasa', 'loc': 'prathipadu', 'rank': '86', 'a': '[1,3,4,6]'}
>>> #without func
>>> len(dict2)
4
>>> sorted(dict2)
['a', 'loc', 'rank', 'school']
>>> #with func
>>> print(dict2)
{'school': 'srinivasa', 'loc': 'prathipadu', 'rank': '86', 'a': '[1,3,4,6]'}
>>> len(dict2.keys())
4
>>> sorted(dict2.keys())
['a', 'loc', 'rank', 'school']
>>> #4.to get a str from a given str and change the first occurance of the word to a user specified input
>>> str1=input("Enter the string:")
Enter the string:key google
>>> char=input("Enter the character")
Enter the characterH
>>> x=list(str1)
>>> x[0]=char
>>> new_str=''.join([str(item) for item in x])
>>> print(new_str)
Hey google
>>> #5.to get a str from user where all occurances of its first char have benn changed to capital
>>> str=input("Enter the string:")
Enter the string:hey babe,how do you do
>>> str=str.title()
>>> print(str)
Hey Babe,How Do You Do
#6
>>> l=[1,2,3,4,5,2,3,4,7,9,5]
>>> l1=[]
>>> for i in l:
	if i not in l1:
	    l1.append(i)
	else:
	    print(i,end=' ')

	    
2 3 4 5 
>>> #7.
>>>a=int(input("Enter the number:"))
>>>Enter the number:2
>>> x=4
>>> y=45
>>> z=55
>>> sum=x+y+z
>>> if (sum%a)==0:
	print("The sum is divisible by num")
else:
	print("The sum is not divisible by num")

	
The sum is divisible by num
>>> #8.Mean,median,mode
>>>#mean
>>> a=int(input("Enter the number:"))
Enter the number:12
>>> b=int(input("Enter the number:"))
Enter the number:4
>>> c=int(input("Enter the number:"))
Enter the number:12
>>> sum=a+b+c
>>> l=3
>>> mean=sum/l
>>> print("mean of the numbers is",mean)
mean of the numbers is 9.333333333333334
>>> #median
>>> a=float(input("Input first number:"))
Input first number:45
>>> b=float(input("Input second number:"))
Input second number:4
>>> c=float(input("Input third number:"))
Input third number:5
>>> if a> b:
	if a<c:
		median=a
	elif b>c:
		median=b
		else:
                        
SyntaxError: invalid syntax
>>> if a> b:
	if a<c:
		median=a
	elif b>c:
		median=b
	else:
		median=c
else:
	if a >c:
		median=a
	elif b<c:
		median=b
	else:
		median=c

		
>>> print("The median is",median)
The median is 5.0
>>> #mode
>>> a=int(input("enter the number:"))
enter the number:5
>>> b=int(input("Enter the number:"))
Enter the number:4
>>> c=int(input("Enter the number:"))
Enter the number:4
>>> x=[a,b,c]
>>> print(x)
[5, 4, 4]
>>> import statistics
>>> x=[5,4,4]
>>> print("Mode of the given numbers is:", (statistics.mode(x)))
Mode of the given numbers is: 4
>>> #9.swap cases of given string
>>> str = "hELLo GoOgLE"
>>> print(str.swapcase())
HellO gOoGle
>>> #10.converting int to decimal and octa decimal numbers
>>> num1=int(input("Enter the number"))
Enter the number4
>>> print("Equivalent binary code is:",bin(num1))
Equivalent binary code is: 0b100
>>> print("Equivalent octa decimal code is:",oct(num1))
Equivalent octa decimal code is: 0o4
>>> 


