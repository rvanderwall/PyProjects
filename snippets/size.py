from sys import getsizeof, version

print(version)

for n in range(13):
    a = [None] * n
    b = list(a)
    c = [x for x in a]
    d = [*a]
    print(f"a is {type(a)}")
    print(f"b is {type(b)}")
    print(f"c is {type(c)}")
    print(f"d is {type(d)}")
    print(n, getsizeof(a),
             getsizeof(b),
             getsizeof(c),
             getsizeof(d))
