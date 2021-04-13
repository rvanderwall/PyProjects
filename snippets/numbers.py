print("     types")
big = 1_000_000
print(type(big))
print(big)

really_big = 1_234_567_890_123_456_789_012_345_678_901
print(type(really_big))
print(really_big)
print(really_big * 2)

f = -2.76
print(type(f))

num = 2.5
print(num.is_integer())
num = 2.0
print(num.is_integer())


print("     Division")
print(3.0 / 2.0)
print(3 / 2)
print(3.0 // 2.0)
print(3 // 2)


print("     Representation errors")
print(0.1 + 0.2)

print("     Power")
print(2 ** 3)
print(pow(2,3))


print("     Printing")
n=7.1258967
print(f"Full value is {n}")
print(f"formatted value is {n:.2f}")
n=123_456.7890
print(f"Separators:  {n:,.2f}")
n=0.1234
print(f"Percents: {n:.2%}")


print("     Complex numbers")
n = 1 + 2j
print(f"Complex number:  {n}")
print(f"Conjugate:  {n.conjugate()}")
print(f"product:  {n * n.conjugate()}")
nr = n.real
ni = n.imag
