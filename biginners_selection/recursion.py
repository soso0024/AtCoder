def find_gcd1(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def find_gcd2(a, b):
    if b == 0:
        return a
    return find_gcd2(b, a % b)


a = 1071
b = 1029

print(find_gcd1(a, b))
print(find_gcd2(a, b))
