
test = [1, 2, 3]

def harmonic_mean(data):
    N = len(data)
    sum_recip = 0
    for d in data:
        if d != 0:
            sum_recip += 1/d
    h_mean = N / sum_recip
    return h_mean


h = harmonic_mean(test)

print(h)
