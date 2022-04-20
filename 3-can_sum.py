import functools
import numbers

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
def can_sum(target_sum, numbers = None):
    if (target_sum == 0): return True
    if (target_sum < 0): return False

    for num in numbers:
        remainder = target_sum - num
        if (can_sum(remainder, numbers)): 
            return True

    return False



print(can_sum(7, [2, 3])) # True
print(can_sum(7, [5, 3, 4, 7])) # True
print(can_sum(7, [2, 4])) # False
print(can_sum(8, [2, 3, 5])) # True
print(can_sum(1000, [7, 14])) # False

print("******* Tabulation *******")


def can_sum2(target_sum, numbers):
    table = []
    [table.append(False) for i in range(target_sum+1)]
    table[0] = True

    for i in range (len(table)):
        if table[i]:
            for num in numbers:
                if (i+num) <= target_sum:
                    table[i+num] = True
    return table[target_sum]

    
print(can_sum(7, [2, 3])) # True
print(can_sum2(7, [5, 3, 4, 7])) # True
print(can_sum2(7, [2, 4])) # False
print(can_sum2(8, [2, 3, 5])) # True
print(can_sum2(1000, [7, 14])) # False
