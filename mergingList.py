# program to merge two list

mylist1 =[]
mylist2 =[]

listsize1 = int(input("enter list size for list 1: "))

for i in range(1, listsize1+1):
    elements1 = int(input("enter the elements of list 1: "))
    mylist1.append(elements1)

listsize2 = int(input("enter the size of list 2: "))

for i in range(1, listsize2+1):
    elements2 = int(input("enter the elements of list 2: "))
    mylist2.append(elements2)

mergeList = mylist1 + mylist2

mergeList.sort()

print("your new sorted list is: " , mergeList)