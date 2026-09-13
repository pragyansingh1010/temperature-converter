def c_to_f(c):
    return (c * 9 / 5) + 32

def f_to_c(f):
    return (f - 32) * 5 / 9

assert c_to_f(0) == 32
assert f_to_c(32) == 0
assert round(c_to_f(100), 5) == 212
assert round(f_to_c(212), 5) == 100
print("Temperature conversion tests passed")
