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
def count_construct (target, word_bank):
    if target == "" : return 1
    
    total_count = 0

    for word in word_bank:
        if target.startswith(word):
            num_ways = count_construct(target[(len(word)):],word_bank)
            total_count += num_ways

    return total_count


print(count_construct("purple", ["purp", "p","ur","le","purpl"])) 
# 2
print(count_construct("abcdef",["ab","abc","cd","def","abcd"]))    
# 1
print(count_construct("skateboard",[
    "bo","rd","ate","t","ska","sk","boar"]))    
# 0
print(count_construct("enterapotentpot", [
    "a","p","ent","enter","ot","o","t"])) 
# 4
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[                    
    "e","eeee","eeeeeee","eeeeeeeeee","ee","eee","eeeee"]))                     
# 0

print("******* Tabulation *******")


def count_construct2(target, word_bank):
    table = [0 for i in range(len(target)+1)]
    table[0] = 1
    for i in range(len(target)):
        for word in word_bank:
            if word == target[i:(i+len(word))]:
                table[i+len(word)] += table[i]
    return table[len(target)]

print(count_construct2("purple", ["purp", "p","ur","le","purpl"])) 
# 2
print(count_construct2("abcdef",["ab","abc","cd","def","abcd"]))    
# 1
print(count_construct2("skateboard",[
    "bo","rd","ate","t","ska","sk","boar"]))    
# 0
print(count_construct2("enterapotentpot", [
    "a","p","ent","enter","ot","o","t"])) 
# 4
print(count_construct2("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[                    
    "e","eeee","eeeeeee","eeeeeeeeee","ee","eee","eeeee"]))                     
# 0