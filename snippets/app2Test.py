import requests
from datetime import datetime


def is_weekday():
    today = datetime.today()
    #print(today)
    # Monday = 0, Sunday = 6
    return (0 <= today.weekday() < 5)

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None


def f1(x):
  return "f1:" + x

def f2(x):
  return "f2:" + x

def f3(x):
  return "f3:" + x


def fa(x):
  x = f1(x)
  x = f2(x)
  x = f3(x)
  return x

def fb(x):
  return "b:" + fa(x)


class C1:
    def __init__(self):
        pass
    def a(self):
        return "A"
    def b(self):
        return "B"
    def a_b(self):
        return self.a() + self.b()

