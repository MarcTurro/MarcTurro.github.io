def conversion_liste(m):
    ...

# Tests
m = [[0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 0, 0], [0, 0, 0, 0]]
assert conversion_liste(m) == [[1, 3], [0, 2, 3], [1], []]
