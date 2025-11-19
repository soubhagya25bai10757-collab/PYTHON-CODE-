# Write a function is_deficient(n) that returns True if the sum of proper divisors of n is less than n.
# SOUBHAGYA KUMAR BEHURA (25BAI10757)
import time
def is_deficient(n):
    start_time = time.time()
    iterations = 0
    if n <= 1:
        end_time = time.time()
        return False, iterations, end_time - start_time    
    divisor_sum = 0
    i = 1
    while i * i <= n:
        iterations += 1
        if n % i == 0:
            if i != n:
                divisor_sum += i          
            other_divisor = n // i
            if other_divisor != n and other_divisor != i:
                divisor_sum += other_divisor        
        i += 1  
    end_time = time.time()
    execution_time = end_time - start_time
    return divisor_sum < n, iterations, execution_time
number = 12
is_def, iterations, exec_time = is_deficient(number)
print(f"Number: {number}")
print(f"Is deficient: {is_def}")
print(f"Iterations: {iterations}")
print(f"Execution time: {exec_time:.8f} seconds")

# Write a function for harshad number is_harshad(n) that checks if a number is divisible by the sum of its digits.
import time
import tracemalloc
def is_harshad(n):
    digits_sum = sum(int(digit) for digit in str(n))
    return n % digits_sum == 0 if digits_sum != 0 else False
def test_harshad_numbers():
    test_numbers = [18, 19, 21, 1729, 123, 6804, 0]
    for num in test_numbers:
        print(f"{num} is Harshad: {is_harshad(num)}")
tracemalloc.start()
start_time = time.time()
test_harshad_numbers()
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Execution Time: {end_time - start_time:.6f} seconds")
print(f"Current Memory Usage: {current / 1024:.2f} KB")
print(f"Peak Memory Usage: {peak / 1024:.2f} KB")

#code 8
import time
import tracemalloc
def is_automorphic(n):
    square = n * n
    return str(square).endswith(str(n))
start_time = time.time()
tracemalloc.start()
num = int(input("Enter a number: "))
if is_automorphic(num):
    print(num, "is an automorphic number.")
else:
    print(num, "is not an automorphic number.")
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
end_time = time.time()
print(f"\nExecution Time: {end_time - start_time:.10f} seconds")
print(f"Current Memory Usage: {current / 1024:.3f} KB")
print(f"Peak Memory Usage: {peak / 1024:.3f} KB")

# Write a function is_pronic(n) that checks if a number is the product of two consecutive integers.
import math
def is_pronic(n: int) -> bool:
    if n < 0:
        return False    
    if n == 0:
        return True        
    k = int(math.sqrt(n))    
    return k * (k + 1) == n
pronic_numbers = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
not_pronic_numbers = [1, 3, 4, 5, 7, 10, 11, 13, 14, 15]
test_results = {}
for num in pronic_numbers:
    test_results[num] = is_pronic(num)
for num in not_pronic_numbers:
    test_results[num] = is_pronic(num)
print("--- Pronic Number Test Results ---")
for num, is_p in sorted(test_results.items()):
    if is_p:
        k = int(math.sqrt(num))
        print(f"Number {num}: {is_p} ({k} * {k+1})")
    else:
        print(f"Number {num}: {is_p}")
print("\nTesting edge case n=100:")
print(f"is_pronic(100): {is_pronic(100)}")

# Write a function prime_factors(n) that returns the list of prime factors of a number.
import time
import tracemalloc
def prime_factors(n):
    tracemalloc.start()
    start_time = time.time()
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.append(n)
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    execution_time = end_time - start_time
    memory_used = peak / 1024  
    print("\nPrime factors:", factors)
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f"Peak memory usage: {memory_used:.2f} KB")
n = int(input("Enter a number: "))
prime_factors(n)
