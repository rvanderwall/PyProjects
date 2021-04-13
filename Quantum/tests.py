import unittest
from VectorMath import LengthException
from Quantum import Qubit, Vector, H

class QubitTests(unittest.TestCase):
    def test_Qubit_0(self):
        q = Qubit(1, 0)
        self.assertIsNotNone(q)

    def test_Qubit_1(self):
        q = Qubit(0, 1)
        self.assertIsNotNone(q)

    def test_Qubit_pi_over_4(self):
        q = Qubit(0.707, 0.707)
        self.assertIsNotNone(q)

    def test_Qubit_too_long(self):
        self.assertRaises(LengthException, Qubit, 1.0, 1.0)

class VectorTests(unittest.TestCase):
    def test_init(self):
        q1 = Qubit.Qubit0()
        q2 = Qubit.Qubit1()
        v = Vector(q1, q2)
        self.assertIsNotNone(v)

    def test_00(self):
        v = Vector(Qubit.Qubit0(), Qubit.Qubit0())
        self.assertEqual([1, 0, 0, 0], v.get_vec())

    def test_01(self):
        v = Vector(Qubit.Qubit0(), Qubit.Qubit1())
        self.assertEqual([0, 1, 0, 0], v.get_vec())

    def test_10(self):
        v = Vector(Qubit.Qubit1(), Qubit.Qubit0())
        self.assertEqual([0, 0, 1, 0], v.get_vec())

    def test_11(self):
        v = Vector(Qubit.Qubit1(), Qubit.Qubit1())
        self.assertEqual([0, 0, 0, 1], v.get_vec())

    def test_mix0(self):
        v = Vector(Qubit(0.707, 0.707), Qubit.Qubit0())
        self.lists_almost_equal([0.707, 0, 0.707, 0], v.get_vec())

    def test_mix1(self):
        v = Vector(Qubit(0.707, 0.707), Qubit.Qubit1())
        self.lists_almost_equal([0, 0.707, 0, 0.707], v.get_vec())

    def test_double_mix(self):
        v = Vector(Qubit(0.900, 0.436), Qubit(0.60, 0.80))
        self.lists_almost_equal([0.54, 0.72, 0.2616, 0.3488], v.get_vec())

    def lists_almost_equal(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for i in range(len(l1)):
            self.assertAlmostEqual(l1[i], l2[i], places=3)


class TestHadamard(unittest.TestCase):
    def test_0(self):
        h = H(Qubit.Qubit0())
        self.assertAlmostEqual(h.val_x0, 0.707, places=3)
        self.assertAlmostEqual(h.val_x1, 0.707, places=3)

    def test_1(self):
        h = H(Qubit.Qubit1())
        self.assertAlmostEqual(h.val_x0, 0.707, places=3)
        self.assertAlmostEqual(h.val_x1, -0.707, places=3)

    def test_0_back(self):
        h_plus = H(Qubit.Qubit0())
        h_0 = H(h_plus)
        self.assertAlmostEqual(h_0.val_x0, 1.000, places=3)
        self.assertAlmostEqual(h_0.val_x1, 0.000, places=3)

