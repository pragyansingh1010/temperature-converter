def c_to_k(c):
    return c + 273.15

def k_to_c(k):
    return k - 273.15

assert c_to_k(0) == 273.15
assert k_to_c(273.15) == 0
assert k_to_c(0) == -273.15
print('Kelvin conversion rules passed')
