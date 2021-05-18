import time
from functools import lru_cache

def check_time():
    time_without_cache_start = time.time()

    factorial(120)

    time_without_cache_end = time.time()
    time_without_cache_result = time_without_cache_end - time_without_cache_start
    print(f"Time without cache: {time_without_cache_result}")

    time_with_cache_start = time.time()

    factorial(120)

    time_with_cache_end = time.time()
    time_with_cache_result = time_with_cache_end - time_with_cache_start
    print(f"Time with cache: {time_with_cache_result}")

    print(f"Difference in time: {time_without_cache_result - time_with_cache_result}")

    print(f"Time without cache longer than with: {time_without_cache_result > time_with_cache_result}")

    return time_with_cache_result

print("Results with a dict for the caching")

factorial_memo = {}
def factorial(k):
    if k < 2: return 1
    if k not in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)
    return factorial_memo[k]

dict_caching_result = check_time()

# Memoize decorator
class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)

        #Warning: You may wish to do a deepcopy here if returning objects
        return self.memo[args]

@Memoize
def factorial(k):
    if k < 2: return 1
    return k * factorial(k - 1)

print("\nResults with decorator")
memoize_decorator_result = check_time()


# lru_cache decorator
@lru_cache(maxsize=None)
def factorial(k):
    if k < 2: return 1
    return k * factorial(k - 1)

print("\nResults with functools @lru_cache")
lru_cache_result = check_time()

# Comparison between three methods
print(f"\nComparison between three methods")

all_results = {"Dict method": dict_caching_result,
               "Memoize decorator method": memoize_decorator_result,
               "lru_cache decorator method": lru_cache_result}

the_best_result_key = max(all_results, key=all_results.get)
the_best_result_value = all_results[the_best_result_key]

print(f"The best result has {the_best_result_key} with time: {the_best_result_value}")