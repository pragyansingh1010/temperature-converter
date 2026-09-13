def c_to_f(c):
    return c * 9 / 5 + 32

def f_to_c(f):
    return (f - 32) * 5 / 9

for c in [-40, 0, 37, 100]:
    assert abs(f_to_c(c_to_f(c)) - c) < 1e-9
print('Temperature round-trip tests passed')
