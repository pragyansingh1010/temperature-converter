def f_to_c(f):
    return (f - 32) * 5 / 9

assert round(f_to_c(32), 5) == 0
assert round(f_to_c(212), 5) == 100
