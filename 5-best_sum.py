import functools

print("******* Recursive and Memoization *******")

def list_to_tuple(function):
    def wrapper(*args):
        args = [tuple(x) if type(x) == list else x for x in args]
        result = function(*args)
        result = tuple(result) if type(result) == list else result
        return result
    return wrapper


@list_to_tuple
@functools.lru_cache(maxsize=None)
def best_sum (target_sum, numbers):
    if (target_sum == 0): return []
    if (target_sum < 0):  return None

    shortest_combination = None

    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum(remainder, numbers)
        if (remainder_combination is not None):
            combination = remainder_combination +(num,)
            if (shortest_combination is None or len(combination) < len(shortest_combination)):
                shortest_combination = combination

    return shortest_combination


print(best_sum(7, [5,3,4,7]))    # (7)
print(best_sum(8, [2,3,5]))      # (3,5) or (5,3)
print(best_sum(8, [1,4,5]))      # (4,4)
print(best_sum(100, [1,2,5,25])) # (25,25,25,25)

print("******* Tabulation *******")


def best_sum2 (target_sum ,numbers):
    table = [None for i in range(target_sum+1)]
    table[0] = []

    for i in range(target_sum):
        if table[i] is not None:
            for num in numbers:
                if (i+num) <= target_sum:
                    c = table[i].copy()
                    c.append(num)
                    if table[i+num] is None or (len(table[i+num])) > len(c):
                        table[i+num] = c
        
    return table[target_sum]


print(best_sum2(7, [5,3,4,7]))    # (7)
print(best_sum2(8, [2,3,5]))      # (3,5) or (5,3)
print(best_sum2(8, [1,4,5]))      # (4,4)
print(best_sum2(100, [1,2,5,25])) # (25,25,25,25)