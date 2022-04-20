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
def how_sum(target_sum, numbers):
    if target_sum == 0: return []
    if target_sum < 0 : return None

    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, numbers)
        if (remainder_result is not None):
            return remainder_result + (num,)

    else: return None


print(how_sum(7, [2,3]))      # [3,2,2]
print(how_sum(7, [5,3,4,7]))  # [4,3]
print(how_sum(7, [2,4]))      # null
print(how_sum(8, [2,3,5]))    # [2,2,2,2]
print(how_sum(300, [7,14]))   # null

print("******* Tabulation *******")

def how_sum2(target_sum, numbers):
    table = [None for i in range(target_sum+1)]
    table[0] = []

    for i in range(target_sum):
        if table[i] is not None:
            for num in numbers:
                if (i+num) <= target_sum:
                    table[i+num] = table[i].copy()
                    table[i+num].append(num)
    return table[target_sum]

print(how_sum2(7, [2,3]))      # [3,2,2]
print(how_sum2(7, [5,3,4,7]))  # [4,3]
print(how_sum2(7, [2,4]))      # null
print(how_sum2(8, [2,3,5]))    # [2,2,2,2]
print(how_sum2(300, [7,14]))   # null