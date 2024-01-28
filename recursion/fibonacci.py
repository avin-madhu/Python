# Give the Nth Fibonacci term

# 1 1 2 3 5 8 13  
#         ^

def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1)+fib(n-2))
    
n = 5
print(fib(n))

