from VectorMath import check_length, normalize


class Qubit:
    def __init__(self, x0, x1):
        check_length([x0, x1])
        self.val_x0 = x0
        self.val_x1 = x1

    @staticmethod
    def Qubit0():
        return Qubit(1, 0)

    @staticmethod
    def Qubit1():
        return Qubit(0, 1)


class Vector:
    def __init__(self, x: Qubit, y: Qubit):
        self.x = x
        self.y = y

    def get_vec(self):
        # |00>  [1, 0, 0, 0]
        # |01>  [0, 1, 0, 0]
        # |10>  [0, 0, 1, 0]
        # |11>  [0, 0, 0, 1]
        b0 = self.x.val_x0 * self.y.val_x0
        b1 = self.x.val_x0 * self.y.val_x1
        b2 = self.x.val_x1 * self.y.val_x0
        b3 = self.x.val_x1 * self.y.val_x1
        v = normalize([b0, b1, b2, b3])
        return v


def H(q:Qubit):
    # |0> --> |0> + |1>
    # |1> --> |0> - |1>
    #    1   1
    #    1  -1
    x0 = q.val_x0 + q.val_x1
    x1 = q.val_x0 - q.val_x1
    v = normalize([x0, x1])
    return Qubit(v[0], v[1])

def H_V(v:Vector):
    h_x = H(v.x)
    h_y = H(v.y)
    return Vector(h_x, h_y)
