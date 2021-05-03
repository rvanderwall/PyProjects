from math import exp
import unittest
from unittest import TestCase
import numpy as np
#
#  The problem:
#   Often, discrete data is categorized for use as a feature in some classifier or regression.
#   The problem comes when essentially arbitrary boundaries are set
#   For example:   small project < $100K.  medium project $100K .. $1M,  large project > $1M
#   a project of $1.001M is categorized as large even though it more closely resembles projects
#   of size $999M, then it does projects of size $999M
#
#   Solution:
#      rather than strict one-hot vectors, each vector is a weight.
#      the $1.001M project embedding would look like [0.001, 0.59, 0.309]
#
#  Limits:
#      when the boundaries are not arbitrary (age < 18, age > 62) this is not appropriate


def normalized(vec):
    a = np.asarray(vec)
    l2 = np.sqrt(np.sum(a ** 2))
    return vec / l2


class Quantizer:
    def __init__(self, vals):
        if isinstance(vals, tuple):
            self.__set_up_buckets(vals[0], vals[1], vals[2])
        elif isinstance(vals, list):
            self.buckets = vals

    def __set_up_buckets(self, num_buckets, b_min, b_max):
        self.buckets = []
        bucket_size = (b_max - b_min) / num_buckets
        lower = b_min
        for i in range(num_buckets):
            upper = lower + bucket_size
            self.buckets.append((lower, upper))
            lower = upper

    @staticmethod
    def __quantize(value, mean, std):
        x = ((value - mean) / std) ** 2
        q = exp(-x)
        return q

    def build_vector(self, value):
        vec = []
        for i in range(len(self.buckets)):
            bucket = self.buckets[i]
            b_min = bucket[0]
            b_max = bucket[1]
            mid = (b_min + b_max) / 2.0
            std = (b_max - b_min)
            bucket_val = self.__quantize(value, mid, std)
            vec.append(bucket_val)
        return normalized(vec)


class QuantizerTests(TestCase):
    def test_simple_range(self):
        # Arrange
        # Build 4 buckets, [0.00 .. 0.25], [0.25 .. 0.50], [0.50 .. 0.75], [ 0.75 .. 1.00]
        buckets = (4, 0.0, 1.0)
        q = Quantizer(buckets)

        # Act
        vec = q.build_vector(0.5)

        # Assert
        self.assertEqual(4, len(vec))
        self.assertAlmostEqual(0.0948, vec[0], places=4)
        self.assertAlmostEqual(0.7007, vec[1], places=4)
        self.assertAlmostEqual(0.7007, vec[2], places=4)
        self.assertAlmostEqual(0.0948, vec[3], places=4)

    def test_simple_buckets(self):
        # Arrange
        # Build 4 buckets, [0.00 .. 0.25], [0.25 .. 0.50], [0.50 .. 0.75], [ 0.75 .. 1.00]
        buckets = [(0.00, 0.25), (0.25, 0.50), (0.50, 0.75), (0.75, 1.00)]
        q = Quantizer(buckets)

        # Act
        vec = q.build_vector(0.5)

        # Assert
        self.assertEqual(4, len(vec))
        self.assertAlmostEqual(0.0948, vec[0], places=4)
        self.assertAlmostEqual(0.7007, vec[1], places=4)
        self.assertAlmostEqual(0.7007, vec[2], places=4)
        self.assertAlmostEqual(0.0948, vec[3], places=4)

    def test_wide_range_buckets(self):
        # Arrange
        buckets = [(0.00, 100.00),
                   (100.00, 100_000.00),
                   (100_000.00, 1_000_000.00),
                   (1_000_000.00, 10_000_000.00),
                   (10_000_000.00, 100_000_000.00)]
        q = Quantizer(buckets)
        print(q.buckets)

        # Act
        vec = q.build_vector(2_000_000.00)

        # Assert
        self.assertEqual(5, len(vec))
        self.assertAlmostEqual(0.0000, vec[0], places=4)
        self.assertAlmostEqual(0.0000, vec[1], places=4)
        self.assertAlmostEqual(0.0669, vec[2], places=4)
        self.assertAlmostEqual(0.7706, vec[3], places=4)
        self.assertAlmostEqual(0.6338, vec[4], places=4)


if __name__ == "__main__":
    unittest.main()
