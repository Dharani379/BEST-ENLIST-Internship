Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dict1={"name":"Dharani","roll no":"118","college":"BIHER"}
>>> dict2={"hobby":"drawing","college":"BIHER","age":"19"}
>>> dict3={**dict1,**dict2}
>>> print{dict3}
SyntaxError: invalid syntax
>>> print(dict3)
{'name': 'Dharani', 'roll no': '118', 'college': 'BIHER', 'hobby': 'drawing', 'age': '19'}
>>> del dict1["roll no"]
>>> print(dect1)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(dect1)
NameError: name 'dect1' is not defined
>>> print(dict1)
{'name': 'Dharani', 'college': 'BIHER'}
>>> #finding length of a set
>>> set={'dhoni','virat','sachin','gangooly','sushanth'}
>>> print(len(set))
5
>>> #finding the intersection of 2 dictionaries
>>> print(dict1)
{'name': 'Dharani', 'college': 'BIHER'}
>>> print(dict2)
{'hobby': 'drawing', 'college': 'BIHER', 'age': '19'}
>>> interdict=dict(dict1.items()&dict2.items())
>>> print(interdict)
{'college': 'BIHER'}
>>> del dict1["interdict"]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    del dict1["interdict"]
KeyError: 'interdict'
>>> #removing the intersection of 2nd from 1st
>>> sn1={1,2,3,4,5}
>>> s2={4,5,6,7,8}
>>> sn1.difference
<built-in method difference of set object at 0x04185728>
>>> sn1.difference_update(s2)
>>> print("sn1: ",sn1)
sn1:  {1, 2, 3}
>>> #task done