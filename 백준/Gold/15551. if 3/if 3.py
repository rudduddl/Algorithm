def make_same_hash_strings(n):
    prefix = '*' * (n - 2)
    a = prefix + '>>'
    b = prefix + '=]'
    return a, b

n = int(input())
a, b = make_same_hash_strings(n)
print(a)
print(b)
