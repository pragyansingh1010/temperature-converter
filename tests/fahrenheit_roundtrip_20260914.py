def f_to_c(f):
    return (f - 32) * 5 / 9

def c_to_f(c):
    return c * 9 / 5 + 32

for value in [-40, 32, 98.6, 212]:
    assert abs(c_to_f(f_to_c(value)) - value) < 1e-9
print('Fahrenheit round trips passed')
