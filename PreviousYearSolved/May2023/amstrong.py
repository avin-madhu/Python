num = int(input("Enter the number: "))

# finding length of number
length = len(str(num))

# initializing sum
amstrongSum = 0

# finding the sum of the cube of each digit
n = num
while(n):
  rem = n%10
  amstrongSum += rem**length
  n //= 10

if num == amstrongSum:
  print(num,"is an amstrong number")
else:
  print(num,"is not an amstrong number")
