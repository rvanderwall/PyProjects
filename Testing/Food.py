import pytest
from collections import OrderedDict
from allpairspy import AllPairs

def is_valid_combination(row):
    """ 
    Filter returns True if row is valid
           returns False if row is not valid
    """
    if len(row) < 3:
        return True

    font = row[0]
    size = row[1]
    style = row[2]

    return True

parameters = OrderedDict({
    "A": ["a1", "a2", "a3"],
    "B": ["b1", "b2"],
    "C": ["c1", "c2", "c3", "c4"],
    "D": ["d1", "d2", "d3"],
})

print("Pairwise:")
for i, pairs in enumerate(AllPairs(parameters, filter_func=is_valid_combination)):
    print("{:2d}: {}".format(i, pairs))




