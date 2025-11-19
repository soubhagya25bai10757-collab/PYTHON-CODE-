# Write a function count_distinct_prime_factors(n) that returns how many unique prime factors a number has.
# SOUBHAGYA KUMAR BEHURA (25BAI10757)
import time
import sys
def prime_factors(n):
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n //= 2
        
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
        
    if n > 2:
        factors.append(n)
        
    return factors
def count_distinct_prime_factors(n):
    factors = prime_factors(n)
    return len(set(factors))
def analyze_execution(func, *args, **kwargs):
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    time_taken_ms = (end_time - start_time) * 1000
    memory_used_bytes = sys.getsizeof(result)
    return result, time_taken_ms, memory_used_bytes
number = 100
distinct_count, time_ms_distinct, memory_bytes_distinct = analyze_execution(count_distinct_prime_factors, number)
print(f"The number of distinct prime factors of {number} is: {distinct_count}")
print(f"Execution Time: {time_ms_distinct:.6f} milliseconds")
print(f"Memory Used (Result Object): {memory_bytes_distinct} bytes")

#Write a function is_prime_power(n) that checks if a number can be expressed as pk where p is prime and k ≥ 1.
import time
def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True
def is_prime_power(n):
    if n <= 1:
        return False
    for p in range(2, int(n**0.5) + 1):
        if is_prime(p):
            power = p
            while power <= n:
                if power == n:
                    return True
                power *= p
    return is_prime(n)
start = time.time()
num = int(input("Enter number: "))
result = is_prime_power(num)
end = time.time()
print("Is prime power:", result)
print("Execution time:", (end - start),"seconds")

# Write a function is_mersenne_prime(p) that checks if 2p - 1 is a prime number (given that p is prime).
import time
import tracemalloc
def is_mersenne_prime(p: int) -> bool:
    
    if p == 2:
        return True  
    if p < 2:
        return False

    M = (1 << p) - 1  
    s = 4
    for _ in range(p - 2):
        s = (s * s - 2) % M
    return s == 0
p = 7
start_time = time.time()
tracemalloc.start()
result = is_mersenne_prime(p)
current, peak = tracemalloc.get_traced_memory()
end_time = time.time()
tracemalloc.stop()
print(f"Is 2^{p} - 1 a Mersenne Prime? : {result}")
print(f"Execution Time: {end_time - start_time:.6f} seconds")
print(f"Current Memory Usage: {current / 1024:.3f} KB")
print(f"Peak Memory Usage: {peak /1024:.3f} KB")

#Write a function twin_primes(limit) that generates all twin prime pairs up to a given limit.
import time
import tracemalloc
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def twin_primes(limit):
    start_time = time.time()           
    tracemalloc.start()                

    twins = []
    prev_prime = 2

    for num in range(3, limit + 1):
        if is_prime(num):
            if num - prev_prime == 2:
                twins.append((prev_prime, num))
            prev_prime = num
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.time()
    print(f"Twin primes up to {limit}:")
    print(twins)
    print(f"\nExecution time: {end_time - start_time:.6f} seconds")
    print(f"Current memory usage: {current / 1024:.2f} KB")
    print(f"Peak memory usage: {peak / 1024:.2f} KB")
twin_primes(100)

# Write a function Number of Divisors (d(n)) count_divisors(n) that returns how many positive divisors a number has.
import time
import tracemalloc

def count_divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
        i += 1
    return count
num = int(input("Enter a number: "))
tracemalloc.start()
start_time = time.time()
result = count_divisors(num)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Number of divisors of {num}: {result}")
print(f"Execution time: {end_time - start_time:.8f} seconds")
print(f"Current memory usage: {current / 1024:.4f} KB")
print(f"Peak memory usage: {peak /1024:.4f} KB")
