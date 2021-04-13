from math import isclose
from Quantum import Vector, H, H_V
from Quantum import Qubit


F_0 = 0
F_1 = 1
F_x = 2
F_not_x = 3

func_to_use = F_not_x

def f_x(x):
    # one of four functions
#    assert x == 0 or x == 1
    assert x >= 0.0 and x <= 1.0
    if func_to_use == F_0:
        return 0
    if func_to_use == F_1:
        return 1
    if func_to_use == F_x:
        return x
    if func_to_use == F_not_x:
        return 1-x


def xor(a,b):
    if isclose(abs(a), abs(b)):
        return Qubit.Qubit0()
    else:
        return Qubit.Qubit1()


def oracle_U(v: Vector):
    # U(|x>|y>) --> |x> |y xor f(x)>
    x = v.x
    # y
    y_new = xor(v.y.val_x1, f_x(x.val_x1))
    return Vector(x, y_new)

for i in range(4):
    func_to_use = i
    input = Vector(Qubit.Qubit0(), Qubit.Qubit1())
#    print(f"Input: {input.x.val_x1}, {input.y.val_x1}")
    step2 = H_V(input)
#    print(f"step2: {step2.x.val_x1}, {step2.y.val_x1}")
    step3 = oracle_U(step2)
#    print(f"step3: {step3.x.val_x1}, {step3.y.val_x1}")
    step4 = H_V(step3)
    print(f"step4: {step4.x.val_x1}, {step4.y.val_x1}")
