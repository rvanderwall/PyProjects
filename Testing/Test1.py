from allpairspy import AllPairs

parameters = [
    ["Brand X", "Brand Y"],
    ["98", "NT", "Win7", "W10"],
    ["Internal", "Model"],
    ["Salaried", "Hourly", "Part-time", "Contractor"],
    [6, 10, 15, 30, 60],
]

print("Pairwise")
for i, pairs in enumerate(AllPairs(parameters)):
    print("{:2d}: {}".format(i, pairs))

