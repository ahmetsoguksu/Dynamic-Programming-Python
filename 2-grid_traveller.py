import functools

print("******* Recursive and Memoization *******")

@functools.lru_cache(maxsize=None)
def grid_traveller(m,n):
    if (m == 1 and n == 1):
        return 1
    elif (m == 0 or n==0 ):
        return 0
    else:
        return (grid_traveller(m-1,n)+grid_traveller(m,n-1))
    
     


print(grid_traveller(1,1))   # 1          
print(grid_traveller(2,3))   # 3          
print(grid_traveller(3,2))   # 3          
print(grid_traveller(3,3))   # 6          
print(grid_traveller(18,18)) # 2333606220 

# tabulation

print("******* Tabulation *******")


def grid_traveller2(m,n):
    table = []
    for i in range(m+1):
        table.append([0 for i in range(n+1)])
    table[1][1] = 1
    for i in range(m+1):
        for x in range(n+1):
            current = table[i][x]
            if x+1 <= n:
                table[i][x+1] += current
            if i+1 <=m:
                table[i+1][x] += current
    return table[m][n]

    
print(grid_traveller2(1,1))   # 1          
print(grid_traveller2(2,3))   # 3          
print(grid_traveller2(3,2))   # 3          
print(grid_traveller2(3,3))   # 6          
print(grid_traveller2(18,18)) # 2333606220 