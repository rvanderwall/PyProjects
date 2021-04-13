import pytest
from collections import OrderedDict
from allpairspy import AllPairs

def function_to_be_tested(font, size, style):
    return True


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
    if font == "Ariel":
        return True

    if font == "Times":
        if size not in [10, 12, 14, 16]:
            return False

#    if font == "System":
#        if not size == 10:
#            return False
#        if not style == "Normal":
#            return False


    return True

parameters = OrderedDict({
    "Font": ["Ariel", "Times", "System"],
    "Size": [8, 9, 10, 12, 14, 16, 20],
    "Style": ["Normal", "Bold", "Italic"],
})

print("Pairwise:")
for i, pairs in enumerate(AllPairs(parameters, filter_func=is_valid_combination)):
    print("{:2d}: {}".format(i+1, pairs))




