from collections import OrderedDict
from allpairspy import AllPairs

def is_valid_combination(row):
    """ 
    Filter returns True if row is valid
           returns False if row is not valid
    """

    n = len(row)
    if n > 1:
        # Brand Y does not support W98
        if "W98" == row[1] and "Brand Y" == row[0]:
            return False

        # Brand X does not work on XP
        if "XP" == row[1] and "Brand X" == row[0]:
            return False

    if n > 4:
        # Contractors are billed in 30 min increments
        if "Contractor" == row[3] and row[4] < 30:
            return False

    return True

parameters = OrderedDict({
    "brand": ["Brand X", "Brand Y"],
    "OS": ["W98", "NT", "2000", "XP"],
    "Comm": ["Internal", "Modem"],
    "Pay": ["Salaried", "Hourly", "Part-time", "Contractor"],
    "Minutes": [6, 10, 15, 30, 60],
})

print("Pairwise:")
for i, pairs in enumerate(AllPairs(parameters, filter_func=is_valid_combination)):
    print("{:2d}: {}".format(i, pairs))


