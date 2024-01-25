# print the number 1 2 3 4
i = 1
n = 5

def printer(i):
    if i < n:
        print(i)
        printer(i+1)
    else: 
        return

printer(i)
print(" ")

# Print the numbers in reverse order

n = 1
m = 6

def printer1(m):
    if n < m:
        print(m)
        printer1(m-1)
    else:
        print(n)
        return 
    

printer1(m)


