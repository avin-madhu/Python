# Generate a list of positive integers from a list of n numbers

lst = [2,-3,7,-4,2,5,-10,0]
NewList = []
for i in lst:
    if i>=0:
        NewList.append(i)
print(NewList)

