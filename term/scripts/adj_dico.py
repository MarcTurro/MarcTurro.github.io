def conversion_dico(m):
    ...

# Tests
m = [[0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 0, 0], [0, 0, 0, 0]]
assert conversion_dico(m) == {0: [1, 3], 1: [0, 2, 3], 2: [1], 3: []}
