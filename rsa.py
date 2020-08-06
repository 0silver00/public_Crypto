

def MyExpMod(a, n, m):
    return (a**n)%m

def MyInvMod(a, m):
    x, y, z = egcd(a, m)
    if x != 1:
        print("No Inverse modular")
    else:
        return y % m

def egcd(a, m):
    if a == 0:
        return(m, 0, 1)
    else:
        x, y, z = egcd(m%a, a)
        return (x, z-(m//a)*y, y)

a = int(input("input 'a': "))
n = int(input("input 'n': "))
m = int(input("input 'm': "))

print("a^n mod m : ", MyExpMod(a, n, m))
print("a^-1 mod m : ", MyInvMod(a, m))
