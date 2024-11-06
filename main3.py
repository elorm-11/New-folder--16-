def factorial(n):
    if n == 0 or n == 1:
        return  1
    else: 
          return n * factorial(n - 1)
num = int(input("enter a number:"))

if num < 0:
   print("factorial does not exist for negative number.")
else:
   print(f"the factorial of {num} is {factorial(num)}")