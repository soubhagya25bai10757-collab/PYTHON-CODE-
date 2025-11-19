# Implement the probabilistic Miller-Rabin test is_prime_miller_rabin(n, k) with k rounds.
# SOUBHAGYA KUMAR BEHURA (25BAI10757)
import time
import random
def is_prime_miller_rabin(n, k=20):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue  
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break  
        else:
            return False
    return True
number_to_test = 100000007 
rounds = 20 
start_time = time.time()
is_prime_1 = is_prime_miller_rabin(number_to_test, rounds)
end_time = time.time()
print(f"Testing number: {number_to_test} with {rounds} rounds.")
print(f"Is {number_to_test} prime? {'Yes, probably' if is_prime_1 else 'No, it is composite'}")
print(f"Time of execution: {end_time - start_time:.6f} seconds")

# Implement pollard_rho(n) for integer factorization using Pollard's rho algorithm.
import random
import math
import time
import tracemalloc
def pollard_rho(n):
    if n % 2 == 0:
        return 2, 1
    def f(x, c):
        return (x * x + c) % n
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1
    steps = 0
    while d == 1:
        steps += 1     
        x = f(x, c)       
        y = f(f(y, c), c)
        d = math.gcd(abs(x - y), n)
        if d == n:
            new_factor, new_steps = pollard_rho(n)
            return new_factor, steps + new_steps           
    return d, steps
if __name__ == "__main__":
    n = 8051   
    print(f"--- Starting Factorization of N={n} ---")
    tracemalloc.start()
    start_time = time.time()
    factor, steps = pollard_rho(n)       
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print("\n--- Results ---")
    print(f"Number to factorize (n): {n}")
    print(f"A factor of {n} is: {factor}")
    print(f"Number of Steps/Iterations: {steps}")
    print(f"Execution Time: {(end_time - start_time):.10f} seconds")
    print(f"Memory Usage: {current / 1024:.4f} KB")
    print(f"Peak Memory Usage: {peak / 1024:.4f} KB")

#Write a function zeta_approx(s, terms) that approximates the Riemann zeta function ζ(s) using the first 'terms' of the series.
import time
import sys
import math
def zeta_approx(s: float, terms: int) -> float:
    if s <= 1.0:
        raise ValueError("The series approximation is only valid for s > 1.")
    if terms <= 0:
        return 0.0
    result = 0.0
    for k in range(1, terms + 1):
        term = 1.0 / (k ** s)
        result += term    
    return result
def run_zeta_approx_with_metrics(s: float, terms: int):
    print(f"--- Riemann Zeta Approximation (s={s}, Terms={terms}) ---")    
    try:
        start_time = time.perf_counter()   
        approximation = zeta_approx(s, terms) 
        end_time = time.perf_counter()
        time_taken = (end_time - start_time) * 1000 
        memory_used_bytes = sys.getsizeof(approximation)     
        steps = terms
        print(f"Approximation ζ({s}): {approximation:.10f}")
        if s == 2.0:
            theoretical_value = (math.pi**2) / 6
            error = abs(theoretical_value - approximation)
            print(f"Theoretical Value (ζ(2)): {theoretical_value:.10f}")
            print(f"Absolute Error: {error:.10f}")
        print("\n--- Performance Metrics ---")
        print(f"No. of Terms: {terms}")
        print(f"Time Taken: {time_taken:.6f} milliseconds")
        print(f"Memory Used (Size of Result Float): {memory_used_bytes} bytes")
        print(f"No. of Steps (Loop Iterations/Additions): {steps}")
    except ValueError as e:
        print(f"ERROR: {e}")
if __name__ == "__main__":
    run_zeta_approx_with_metrics(s=2.0, terms=100)
    print("\n" + "="*70 + "\n")
    
    run_zeta_approx_with_metrics(s=3.0, terms=1000)
    print("\n" + "="*70 + "\n")

#Write a function Partition Function p(n) partition_function(n) that calculates the number of distinct ways to write n as a sum of positive integers.
import time
import tracemalloc
def partition_function(n):
    p = [0] * (n + 1)
    p[0] = 1  
    for k in range(1, n + 1):
        total = 0
        m = 1
        while True:
            g1 = m * (3*m - 1) // 2
            g2 = m * (3*m + 1) // 2
            if g1 > k:
                break
            sign = -1 if (m % 2 == 0) else 1
            total += sign * p[k - g1]

            if g2 <= k:
                total += sign * p[k - g2]
            m += 1
        p[k] = total
    return p[n]
n = int(input("Enter n: "))
tracemalloc.start()
start = time.time()
result = partition_function(n)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
exec_time = time.time() - start
print(f"\np({n}) = {result}")
print(f"Execution Time: {exec_time:.6f} seconds")
print(f"Memory Used: {peak/1024:.2f} KB")
