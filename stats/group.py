

# 5634, (6543, 3456)
# 3087, (8730, 0378)
# 8352
#
#  Pattern:
#    1)   SETA -> (ESAT, TASE)
#    2)   order
#    3)   subtract
#
#    S E T A
# -  A T E S
# ----------
#    E A S T


def try_it(S, E, T, A):
    if S == E:
        return False
    if S == T:
        return False
    if S == A:
        return False
    if E == T:
        return False
    if E == A:
        return False
    if T == A:
        return False

    SETA = digits_to_num(S, E, T, A)
    ATES = digits_to_num(A, T, E, S)
    EAST = digits_to_num(E, A, S, T)

    if EAST == SETA - ATES:
        return True
    return False

def search_for_EAST():
    for S in range(10):
        for E in range(10):
            for T in range(10):
                for A in range(10):
                    if try_it(S, E, T, A):
                        print(f"Found solution: S:{S} E:{E} T:{T} A:{A}")

def num_to_digits(N):
    d1 = N // 1000
    N = N - d1 * 1000
    d2 = N // 100
    N = N - d2 * 100
    d3 = N // 10
    N = N - d3 * 10
    d4 = N
    return d1, d2, d3, d4

def digits_to_num(d1, d2, d3, d4):
    SETA = d1 * 1000 + d2 * 100 + d3 * 10 + d4
    return SETA

def rotate(N):
    S, E, T, A = num_to_digits(N)
    ESAT = digits_to_num(E, S, A, T)
    TASE = digits_to_num(T, A, S, E)
    return ESAT, TASE

def get_next(N):
    N1, N2 = rotate(N)
    if N2 > N1:
        t = N2
        N2 = N1
        N1 = t
    N3 = N1 - N2
    return N1, N2, N3

def cycle_through_nums(N):
    for i in range(20):
        N1, N2, N3 = get_next(N)
        print(f"{N}, ({N1}, {N2})")
        N = N3

def converge(x):
    k = 3.55
    for i in range(20):
        print(x)
        x = k * x * (1 - x)

#search_for_EAST()
#cycle_through_nums(6372)
converge(0.5)
print("Done")