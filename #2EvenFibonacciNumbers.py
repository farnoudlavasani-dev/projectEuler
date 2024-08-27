#problem2
#By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
first = 1
second = 2
sum = 0
while (first < 4000000):
    if is_even(first):
        sum = sum + first
    new = first + second
    first = second
    second = new
print(sum)