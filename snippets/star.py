
# https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/


#  *a unpacks the elements in a
a = ['x', 'y', 'z' ]

# a is a list of three elements
#  f(a) ->  f gets a single argument which is a list
# *a
#  f(*a) -> f gets three arguments
#  

b = {'year': '2020', 'month': 'jan', 'day': '01'}


def f(*args):
    idx = 0
    for a in args:
        print(f"arg{idx} = {a}")
        idx += 1

def g(a0, a1, a2):
    print(f"g_a0 = {a0}")
    print(f"g_a1 = {a1}")
    print(f"g_a2 = {a2}")


f(a)
f(*a)
#  g(a) --> throws error, arg count
g(*a)


f(b)
f(*b)
