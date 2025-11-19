# Write a function aliquot_sum(n) that returns the sum of all proper divisors of n (divisors less than n).
# SOUBHAGYA KUMAR BEHURA (25BAI10757)
import time
def aliquot_sum(n):
    if n == 1:
        return 0
    sum_div = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_div += i
            if i * i != n:
                sum_div += n // i                
    return sum_div
num = 30  
start_time = time.time()
result = aliquot_sum(num)
end_time = time.time()
print(f"The number is: {num}")
print(f"The sum of proper divisors (aliquot sum) is: {result}")
print(f"Time of execution: {end_time - start_time:.6f} seconds")

# Write a function are_amicable(a, b) that checks if two numbers are amicable (sum of proper divisors of a equals b and vice versa).
import time
import tracemalloc
def sum_of_proper_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)
def are_amicable(a, b):
    return sum_of_proper_divisors(a) == b and sum_of_proper_divisors(b) == a
a = 220
b = 284
tracemalloc.start()
start_time = time.time()
result = are_amicable(a, b)
current, peak = tracemalloc.get_traced_memory()
end_time = time.time()
tracemalloc.stop()
print(f"Are {a} and {b} amicable? -> {result}")
print(f"Execution Time: {(end_time - start_time):.10f} seconds")
print(f"Memory Usage: {current / 1024:.4f} KB")
print(f"Peak Memory Usage: {peak / 1024:.4f} KB")

# Write a function multiplicative_persistence(n) that counts how many steps until a number's digits multiply to a single digit.
import time
import sys
import mat
def calculate_digit_product(n):
    if n < 0:
        n = abs(n)        
    product = 1
    for digit_char in str(n):
        product *= int(digit_char)
    return product
def multiplicative_persistence(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    current_number = n
    steps = 0    
    while current_number > 9:
        steps += 1
        current_number = calculate_digit_product(current_number)        
    return steps
if __name__ == "__main__":
    TEST_NUMBER = 77    
    print(f"--- Running Multiplicative Persistence for N = {TEST_NUMBER} ---")  
    start_time = time.perf_counter()   
    persistence_result = multiplicative_persistence(TEST_NUMBER)   
    end_time = time.perf_counter()   
    print(f"\n1. Number of Steps (Multiplicative Persistence): {persistence_result}")
    elapsed_time_ms = (end_time - start_time) * 1000
    print(f"2. Time Taken (Execution Time): {elapsed_time_ms:.6f} milliseconds")
    input_memory = sys.getsizeof(TEST_NUMBER)
    output_memory = sys.getsizeof(persistence_result)
    print(f"\n3. Memory Used (Bytes):")
    print(f"   - Input Number ({TEST_NUMBER}): {input_memory} bytes")
    print(f"   - Resulting Steps ({persistence_result}): {output_memory} bytes")
    if TEST_NUMBER <= 999:
        print("\n--- Step Breakdown ---")
        n_current = TEST_NUMBER
        step = 0
        while n_current > 9:
            step += 1
            product = calculate_digit_product(n_current)
            print(f"Step {step}: {n_current} -> {list(str(n_current))} -> Product: {product}")
            n_current = product
        print(f"Final Result: Single digit {n_current} reached in {step} steps.")

# Write a function is_highly_composite(n) that checks if a number has more divisors than any smaller number.
import math
import time
import sys
import collections
def count_divisors(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    count = 0
    limit = int(math.sqrt(n))
    for i in range(1, limit + 1):
        if n % i == 0:
            count += 1
            if i * i != n:
                count += 1
    return count
def is_highly_composite(n):
    if n <= 0:
        return False
    if n == 1:
        return True

    divisors_n = count_divisors(n)

    for k in range(1, n):
        divisors_k = count_divisors(k)
        
        if divisors_k >= divisors_n:
            return False
    return True
def run_analysis(n_to_check):
    mem_before = sys.getsizeof(collections.Counter(locals()))
    start_time = time.time()
    is_hcn = is_highly_composite(n_to_check)
    end_time = time.time()
    mem_after = sys.getsizeof(collections.Counter(locals()))
    print(f"\n--- Checking if N = {n_to_check} is Highly Composite ---")
    print(f"Result: {n_to_check} is {'Highly Composite' if is_hcn else 'NOT Highly Composite'}")
    elapsed_time_ms = (end_time - start_time) * 1000
    print(f"TIME TAKEN: {elapsed_time_ms:.4f} milliseconds")
    memory_used_bytes = mem_after - mem_before
    print(f"MEMORY USED: {memory_used_bytes} bytes")
    estimated_steps = int(n_to_check * math.sqrt(n_to_check) * 1.5)
    print(f"NO. OF STEPS: ~{estimated_steps:,} operations")
RUN_N = 12
run_analysis(RUN_N)

# Write a function for Modular Exponentiation mod_exp(base, exponent, modulus) that efficiently calculates (baseexponent) % modulus.
import time
import tracemalloc
def mod_exp(base, exponent, modulus):
    start_time = time.time()
    tracemalloc.start() 
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:     
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    current, peak = tracemalloc.get_traced_memory()
    end_time = time.time()
    tracemalloc.stop()
    exec_time = end_time - start_time
    return result, exec_time, current, peak
base = 7
exponent = 256
modulus = 13
value, exec_time, current_mem, peak_mem = mod_exp(base, exponent, modulus)
print(f"Result: {value}")
print(f"Execution Time: {exec_time} seconds")
print(f"Current Memory Usage: {current_mem} bytes")
print(f"Peak Memory Usage: {peak_mem} bytes")
