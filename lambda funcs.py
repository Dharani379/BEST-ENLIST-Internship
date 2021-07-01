>>> #create lambda fun that multiplies argx with arg y
>>> l=lambda x,y:x*y
>>> print(l(93,7))
651
>>> #creating a fibonacci series to n using lambda
>>> from functools import reduce
>>> fib=lambda n :reduce(lambda number :number*n,nums)
>>> fib=lambda n :reduce(lambda x,_:x+[x[-1]+x[-2]],range (n-2),[0,1])
>>> print(fib(15))
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
>>> #3q
>>> numms = [2,3,6,5]
>>> n = 2
>>> print("orginal list : ",numms)
orginal list :  [2, 3, 6, 5]
>>> filtered_nums=list(map(lambda number : number*n,numms))
>>> print("Result : ",''.join(map(str,filtered_nums)))
Result :  461210
>>> #4q
>>> list1=[1,3,5,7,8,9,90,65,71,63]
>>> list2=(list(map(lambda j : j%9==0,list1)))
>>> print(list1)
[1, 3, 5, 7, 8, 9, 90, 65, 71, 63]
>>> print("Result : ",''.join(map(str,list2)))
Result :  FalseFalseFalseFalseFalseTrueTrueFalseFalseTrue
>>> list2=(list(filter(lambda j : j%9==0,list1)))
>>> print("Result : ",''.join(map(str,list2)))
Result :  99063
>>> #5q
>>> list1=[2,0,12,3,45,6,78,55,7,43,80,96,71,22]
>>> print(list1)
[2, 0, 12, 3, 45, 6, 78, 55, 7, 43, 80, 96, 71, 22]
>>> list2=list(filter(lambda j:j%2==0,list1))
>>> print("Result : ",''.join(map(str,list2)))
Result :  2012678809622
>>> print(len(list2))
8
>>> 
