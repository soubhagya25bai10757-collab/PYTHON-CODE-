# Write a function factorial(n) that calculates the factorial of a non-negative integer n (n!).
# SOUBHAGYA KUMAR BEHURA (25BAI10757)  
import time
n=int(input("enter a number:"))
start= time.time()
t=1
for i in range(1,n+1):
    t*=i
end=time.time()
print("factorial of" ,n,"=",t)
execution_time =end-start
print("execution time:",execution_time,"seconds")
divisors=0
for i in range(1, n + 1):
    if n % i == 0:
        divisors += 1
memory_used = divisors * 28  
print("Memory used (approx):", memory_used,"bytes")

# Write a function is_palindrome(n) that checks if a number reads the same forwards and backwards.
import time
import sys
def is_palindrome(n):
    if n < 0:
        return False, {
            "time_taken_ms": 0.0,
            "math_iterations": 0,
            "space_used_bytes": 0,
            "notes": "Negative number treated as non-palindrome, no computation performed."
        }     
    start_time = time.perf_counter()
    original_number = n
    reversed_number = 0
    temp_n = n
    iterations = 0 
    while temp_n > 0:
        digit = temp_n % 10
        reversed_number = (reversed_number * 10) + digit
        temp_n = temp_n // 10
        iterations += 1
    is_palin = original_number == reversed_number
    end_time = time.perf_counter()
    time_taken_ms = (end_time - start_time) * 1000 
    space_used_bytes = 120 
    metrics = {
        "time_taken_ms": time_taken_ms, 
        "math_iterations": iterations,
        "space_used_bytes": space_used_bytes,
        "notes": "Time is in milliseconds (ms). Iterations count the number of loop cycles."
    }
    return is_palin, metrics
test_numbers = [
    12321,          
    1001,           
    12345,          
    7,              
    12345678987654321, 
    -121            
]
print("--- In-Memory Palindrome Checker Results ---")
for number in test_numbers:
    result, metrics = is_palindrome(number) 
    print("-" * 40)
    print(f"Checking Number: {number}")
    print(f"Is Palindrome: {result}")
    print("\n--- Performance Metrics ---")
    print(f"1. Time Taken: {metrics['time_taken_ms']:.4f} ms")
    print(f"2. Number of Steps (Iterations): {metrics['math_iterations']}")
    print(f"3. Memory Used (Estimated): {metrics['space_used_bytes']} bytes")

# Write a function mean_of_digits(n) that returns the average of all digits in a number.
import time
import sys
def mean_of_digits(n: int) -> float:
    num = abs(n)
    if num == 0:
        return 0.0
    total_sum = 0
    count = 0
    while num > 0:
        digit = num % 10
        total_sum += digit
        count += 1
        num //= 10
    return total_sum / count
print("Welcome to the Digit Mean Calculator!")
try:
    user_input = input("Enter a whole number: ")
    number = int(user_input)
    start_time = time.time()
    result = mean_of_digits(number)
    end_time = time.time()
    print(f"\nThe number: {number}")
    print(f"The mean of the digits is: {result:.2f}")
    print("-" * 30)
    print(f"Execution Time: {end_time - start_time:.6f} seconds")
    print(f"Memory utilization: {sys.getsizeof(result)} bytes")
except ValueError:
    print("\nSorry, that wasn't a valid whole number. Please enter only digits."

# Write a function digital_root(n) that repeatedly sums the digits of a number until a single digit is obtained.
import time
def digital_root(n):
    iterations = 0
    start_time = time.time()   
    while n >= 10:   
        s = 0
        temp = n
        while temp > 0:  
            s += temp % 10
            temp //= 10
        n = s
        iterations += 1
    end_time = time.time()   
    execution_time = end_time - start_time
    print("Digital root:", n)
    print("Iterations:", iterations)
    print("Execution time:", execution_time, "seconds")
    return n

# Write a function is_abundant(n) that returns True if the sum of proper divisors of n is greater than n.
n=int(input("n: "))
f=1
for i in range(2,n+1): f*=i
s=str(n); pal = s==s[::-1]
d=[int(c) for c in s if c.isdigit()]; mean=sum(d)/len(d)
dr=abs(n)
while dr>9: dr=sum(int(c) for c in str(dr))
sd=0
if n>1:
    sd=1
    import math
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            sd+=i
            if i!=n//i: sd+=n//i
abundant = sd>n
print("factorial =",f)
print("is_palindrome =",pal)
print("mean_of_digits =",mean)
print("digital_root =",dr)
print("is_abundant =",abundant)
