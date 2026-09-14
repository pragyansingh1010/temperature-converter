def c_to_f(c):
    return c * 9 / 5 + 32

assert c_to_f(-40) == -40
assert c_to_f(-10) == 14
assert c_to_f(-1) == 30.2
print('Negative Celsius rules passed')
