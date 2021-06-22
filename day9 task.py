>>>L1=[9,8,7,6,5,4,3,2,1]
>>> l=[]
>>> for i in L1:
	l.append(i+2)
	print(l)

	
[11]
[11, 10]
[11, 10, 9]
[11, 10, 9, 8]
[11, 10, 9, 8, 7]
[11, 10, 9, 8, 7, 6]
[11, 10, 9, 8, 7, 6, 5]
[11, 10, 9, 8, 7, 6, 5, 4]
[11, 10, 9, 8, 7, 6, 5, 4, 3]
>>> #2. print fibonacci series
>>> n=int(5)
>>> for i in range(n):
	print("".join(map(str,range(n-i,0,-1))))

	
54321
4321
321
21
1
>>> #fibonacci series prgrm
>>> n=int(5)
>>> a=0
>>> b=1
>>> sum=0
>>> count=1
>>> print("fibonacci series:",end ="")
fibonacci series:
>>> while(count<=n):
	print(sum,end ="")
	count +=1
	a=b
	b=sum
	sum=a+b

	
01123
>>> #amstrong number programe
>>> num1=int(154)
>>> sum1=0
>>> temp1=num1
>>> while  temp1>0:
	digit1 = temp1%10
	sum1+=digit1**3
	temp1//=10
	if num1==sum1:
		print(num1,"is amstrong")
	else:
		print(num1,"is not amstrong")

		
154 is not amstrong
154 is not amstrong
154 is not amstrong
>>> #prgrm to convert days to age
>>> x=input("Enter the no.of days::")
Enter the no.of days::8976
>>> d=int(x)
>>> y=int(d/365)
>>> print("the age of",x,"number of days is",y)
the age of 8976 number of days is 24
>>> #5. prgrm of multiplication table of9
>>> num=int(9)
>>> mul=0
>>> print("multiplication table of : 9")
multiplication table of : 9
>>> for i in range(1,10+1)
SyntaxError: invalid syntax
>>> for i in range(1,10+1):
	mul=num*i
	print(num,"x",i,"=",mul)

	
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90
>>> #6.prgrm to find if a num is pos or neg
>>> a=int(65)
>>> if a>0:
	print("Number is positive")
elif a<0:
	print("Number is negative")
else a=0:
	
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> #6.prgrm to find if a num is pos or neg
>>> a=int(65)
>>> if a>0:
	print("Number is positive")
elif a<0:
	print("Number is negative")
else:
	print("Number is zero")

	
Number is positive
>>> #8. trignometry using math fumction
>>> import math
>>> a_b = math.pi/6
>>> print("The value of sine of pi/6 is:",end="")
The value of sine of pi/6 is:
>>> print(math.sin(a_b))
0.49999999999999994
>>> print("the values of cosine of pi/6 is:",math.cos(a_b))
the values of cosine of pi/6 is: 0.8660254037844387
>>> #basic calculator
>>> print("calculator")
calculator
>>> print("1.add")
1.add
>>> print("2.subtract")
2.subtract
>>> print("3.multiply")
3.multiply
>>> print("4.divide")
4.divide
>>> ch=int(input("Enter choice(1-4):"))
Enter choice(1-4):3
>>> if ch==1:
	a=int(input("Enter a:"))
	b=int(input("Enter b:"))
	c=a+b
	print("sum=",c)
elif ch==2:
	a=int(input("Enter a:"))
	b=int(input("Enter b:"))
	d=a-b
	print("subtraction=",d)
elif ch==3:
	a=int(input("Enter a:"))
	b=int(input("Enter b:"))
	x=a*b
	print("product=",x)
elif ch==4:
	a=int(input("Enter a:"))
	b=int(input("Enter b:"))
	y=a/b
	print("division is=",y)

	
Enter a:4
Enter b:5
product= 20
>>> 

	
