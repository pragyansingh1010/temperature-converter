def c_to_k(c):
    return c + 273.15

def k_to_c(k):
    return k - 273.15

assert round(c_to_k(0), 2) == 273.15
assert round(k_to_c(273.15), 2) == 0
assert round(c_to_k(100), 2) == 373.15
print('Kelvin conversion tests passed')
