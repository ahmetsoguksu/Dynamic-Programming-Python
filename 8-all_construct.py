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
def all_construct(target, word_bank):
    if target == "": return [[]]

    r = []

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank)
            target_ways = [el[:] for el in suffix_ways]
            [el.insert(0, word) for el in target_ways]
            r.extend(target_ways)
    return r

print(all_construct('hello', ['cat', 'dog', 'mouse']))  
# []
print(all_construct('', ['cat', 'dog', 'mouse']))  
# [[]]
print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) 
# [['le', 'purp'], ['le', 'p', 'ur', 'p']]
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))  
# [['ef', 'cd', 'ab'], ['def', 'c', 'ab'], ['def', 'abc'], ['ef', 'abcd']]


print("******* Tabulation *******")

def all_construct2(target, word_bank):
    table = [[] for i in range(len(target)+1)]
    table[0] = [[]]

    for i in range(len(target)):
        for word in word_bank:
            if word == target[i:(i+len(word))]:
                for e in table[i]:
                    temp = e[:]
                    temp.append(word)
                    table[i+len(word)].append(temp[:])
    return table[len(target)]


print(all_construct2('hello', ['cat', 'dog', 'mouse']))  
# []
print(all_construct2('', ['cat', 'dog', 'mouse']))  
# [[]]
print(all_construct2('purple', ['purp', 'p', 'ur', 'le', 'purpl'])) 
# [['le', 'purp'], ['le', 'p', 'ur', 'p']]
print(all_construct2('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))  
# [['ef', 'cd', 'ab'], ['def', 'c', 'ab'], ['def', 'abc'], ['ef', 'abcd']]
