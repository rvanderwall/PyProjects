
import sys
import re

print("List of paths to look down to import")
print(sys.path)

sys.path.append(f'/Users/rvanderwall/projects/python/ModulesPackages')
print(sys.path)

print("Use dunder to emulate which")
print(re.__file__)


def f(arg1, *args, **kwargs):
  print(f"positional arg: {arg1}")
  print(f"positional arg: {args[0]}")
  print(f"positional_arg: {args[1]}")
  for kwarg_name in kwargs.keys():
      print(f"kwarg[{kwarg_name}] = {kwargs[kwarg_name]}")

f("first arg", "second arg", "third arg", x=1, y=2)


