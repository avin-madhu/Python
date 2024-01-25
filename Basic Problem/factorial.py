# Find the factorial of a number n



def fact(n):
    if n==0:
        return 1
    else:
        return (n*fact(n-1))

n = 3
num = fact(n)
print("The factorial is: ",num)
