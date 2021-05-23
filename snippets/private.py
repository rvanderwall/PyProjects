

class A:
  def p1(self):
      print("Called p1")

  def _p2(self):
      print("Called _p2")

  def __p3(self):
      print("Called __p3")

  def call_p3(self):
      self.__p3()


if __name__ == "__main__":
   a = A()
   a.p1()
   a._p2()
   #a.__p3()
   a.call_p3()
