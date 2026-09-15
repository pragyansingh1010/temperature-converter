def c_to_k(c):
    return c + 273.15

assert round(c_to_k(-273.15), 5) == 0
assert round(c_to_k(0), 5) == 273.15
