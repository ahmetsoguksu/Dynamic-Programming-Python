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
def can_construct (target, word_bank):
    if target == "": return True

    for word in word_bank :
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct(suffix, word_bank) == True:
                return True
    
    
    return False



print(can_construct("abcdef", ["ab","abc","cd","def","abcd"]))                # true
print(can_construct("skateboard", ["bo","rd","ate","t","ska","sk","boar"]))   # false
print(can_construct("enterapotentpot", ["a","p","ent","enter","ot","o","t"]))  # true
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[                    
    "e","eeee","eeeeeee","eeeeeeeeee","ee","eee","eeeee"                      # false
])) 

print("******* Tabulation *******")

def can_construct2(target, word_bank):
    table = [False for i in range((len(target)+1))]
    table[0] = True
    for i in range(len(target)):
        if table[i]:
            for word in word_bank:
                if target[i:i+len(word)] == word:
                    table[i+len(word)] = True
    return table[len(target)]

print(can_construct2("abcdef", ["ab","abc","cd","def","abcd"]))                # true
print(can_construct2("skateboard", ["bo","rd","ate","t","ska","sk","boar"]))   # false
print(can_construct2("enterapotentpot", ["a","p","ent","enter","ot","o","t"]))  # true
print(can_construct2("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",[                    
    "e","eeee","eeeeeee","eeeeeeeeee","ee","eee","eeeee"                      # false
])) 