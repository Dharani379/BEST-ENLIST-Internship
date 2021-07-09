def listofTuples(l1,l2):
    return list(map(lambda x,y:(x,y),l1,l2))
list1 = [1,2,3]
list2 = ['a','b','c']
print(listofTuples(list1,list2))
def merge(list1,list2):
    merged_list = list(zip(list1,list2))
    return merged_list
list1 = [1,2,3]
list2 = ['a','b','c']
print(merge(list1,list2))

#2q
list1=[1,2,3,4,5,6,7,8]
list2=['a','b','c','d','e','f','g']
result=tuple(zip(list1,list2))
print(result)

#3q
list1=[46,57,38,96,20,45,23]
list2=sorted(list1)
print(list2)


#4q
def filtereven(nums):
    if nums%2 !=0:
        return True
    else:
        return False

numbers=[22,11,44,55,67,23,27,56,21,78,34,41]
result=filter(filtereven,numbers)
for i in result:
    print(i)
    
