import time
from datetime import datetime
import functools



##
## Functions are objects
##
def func_a():
    return "Function A"

def func_b():
    return "Function B"

def func_c(*funcs):
    for func in funcs:
        print(func())

main = func_c
main(func_a, func_b)


##
## nested functions
##
def outer():
    def inner():
        return "Inner function"
    return inner

inn = outer()
print(inn())


##
## Closures
##
def c(parm):
    def c_in():
        ## parm is bound
        return "c_in:" + parm.upper()
    return c_in

p = c("something")
print(p())


##
## Decorator basics
##
def deco(func):
    @functools.wraps(func)  ## Sets introspection
    def wrapper(*args, **kwargs):
        print("Before with arg[0]=" + args[0])
        r_val = func(*args, **kwargs)
        print("After")
        return r_val
    return wrapper

@deco
def f_2_wrap(runner):
    print("F 2 is running " + runner)
    return "F 2 has run"

#f_2_wrap = deco(f_2_wrap)

print(f_2_wrap.__name__)    ## Without functools.wraps, this prints 'wrapper'
print(f_2_wrap("my runner"))


##
## Timer example
##
def timer(func):
    """ Prints execution time """
    @functools.wraps(func)
    def timer(*args, **kwargs):
        start_time = time.time()
        return_val = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"finished running {func.__name__} in {run_time:.4f} seconds.")
        return return_val
    return timer

@timer
def t_test(n):
    print(f"Entering t_test with n = {n}")
    res = 0
    for _ in range(n):
        res += sum((i **3 for i in range(100_000)))
    return res

res = t_test(5)
print(res)


##
## Logger Example
##
def logexc(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_rep = [repr(arg) for arg in args]
        kwargs_rep = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = ", ".join(args_rep + kwargs_rep)

        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("Time: ", datetime.now().strftime("%Y-%m-%d [%H:%M:%S]"))
            print("Args: ", signature)
            print("Error:\n")
            # raise
    return wrapper

@logexc
def divint(a, b):
    return a / b

divint(1, 0)


##
## Decorater with parameters
##
def joinby(delim=" "):
    def outer_wrapper(func):
        @functools.wraps(func)
        def inner_wrapper(*args, **kwargs):
            val = func(*args, **kwargs)
            val = val.split(" ")
            val = delim.join(val)
            return val
        return inner_wrapper
    return outer_wrapper

@joinby(delim=",")
def hello(name):
    return f"Hello {name}"

@joinby(delim="#")
def bye(name):
    return f"bye {name}"

jb = joinby(delim="^")
bye2 = jb(bye)

print(hello("robert"))
print(bye("robert"))
print(bye2("robert2"))


##
## Decorator with/without params
##
def g_deco(func=None, foo="bar"):
    if func is None:
        return functools.partial(g_deco, foo = foo)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Wrapping {func.__name__} and foo={foo}")
        rv = func(*args, **kwargs)
        print("Finished")
        return rv
    return wrapper

@g_deco
def f1():
    pass

@g_deco(foo="buzz")
def f2():
    pass

f1()
f2()



##
## Decorator with Classes - Stateful decorator
##
class Bold:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.n_calls = 0

    def __call__(self, *args, **kwargs):
        self.n_calls += 1
        print(f"Bold wraps {self.func.__name__}, called {self.n_calls} times")
        val = self.func(*args, **kwargs)
        return f"<b>{val}</b>"

@Bold
def hello(name):
    return f"Hello {name}"

@Bold
def bye(name):
    return f"bye {name}"

print(hello("rob"))
print(bye("rob"))
print(hello("rob"))



##
## Registration without interceptin
##

logger_list = []
def register_logger(func):
    logger_list.append(func)
    return func

@register_logger
def logger(request):
    print(request.method, request.path)


