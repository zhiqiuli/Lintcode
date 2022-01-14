'''
Removing chocolates 1 & 3 at a time

A box contains a number of chocolates that can only be removed 1 at a time or 3 at a a time. How many ways can the box be emptied? The answer can be very large so return it modulo of 10^9+7
'''
def count(n):
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 2   
    
    c1, c2, c3 = 2, 1, 1
    
    for _ in range(4, n):
    
        c1_tmp = c1
        c2_tmp = c2
        c3_tmp = c3

        c1 = c1_tmp + c3_tmp
        c2 = c1_tmp
        c3 = c2_tmp
        
    return c1 + c3

print(count(4))
print(count(5))
print(count(6))
print(count(7))


def f(n):

    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 2
    return f(n-3) + f(n-1)


print(f(4))
print(f(5))
print(f(6))
print(f(7))
