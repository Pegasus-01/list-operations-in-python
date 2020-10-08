# ask user to input string
string = input("Please enter your string: ")

# split the string into a list
liststr = string.split()

# get rid of second letter of string through the list
liststr = liststr.remove(liststr[1])

# output the resultant list
print(liststr)

# join the list back into a string and output that
string = liststr.join()
print(string)
