import functools

print("******* Recursive and Memoization *******")


def fib(n):
    if(n <= 2): 
        return 1
    else:
        return fib(n-1) + fib(n -2)


# print(fib(50))

# Memoization fib2(n) 

@functools.lru_cache(maxsize=None)
def fib2(n):
    if(n <= 2): 
        return 1
    else:
        return fib2(n-1) + fib2(n -2)

print(fib2(6))
print(fib2(7))
print(fib2(50)) 
print(fib2(100)) 
print(fib2(250)) 

# Tabulation fib3(n)

print("******* Tabulation *******")

def fib3 (n):
    table = []
    for i in range(n+1):
        table.append(0)
    table[1]=1
    for i in range(n):
        table[i+1] += table[i]
        if i < len(table)-2:
            table[i+2] += table[i]
    
    return table[n]

print(fib3(6))
print(fib3(7))
print(fib3(50)) 
print(fib3(100)) 
print(fib3(250)) 