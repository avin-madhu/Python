# print 1 2 3 4 using backtracking recursion

i = 4 # started with 4

def printer(i):
    if i < 1:
        return 
    else:
        printer(i-1)
        print(i)


printer(i)