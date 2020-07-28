#program to find the second largest program in python

listsize = int(input("enter the list size: "))

mylist =[]


for i in range(1, listsize+1):
    element = int(input("enter the element: "))
    mylist.append(element)

mylist.sort()

print("second largest element is: ", mylist[listsize-2])