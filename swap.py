import dis


def swap():
    a, b = 1, 2
    a, b = b, a
    return


dis.dis(swap)
"""
$ pdm run swap.py

  5           0 LOAD_CONST               1 ((1, 2))
              2 UNPACK_SEQUENCE          2
              4 STORE_FAST               0 (a)
              6 STORE_FAST               1 (b)

  6           8 LOAD_FAST                1 (b)
             10 LOAD_FAST                0 (a)
             12 ROT_TWO
             14 STORE_FAST               0 (a)
             16 STORE_FAST               1 (b)

  7          18 LOAD_CONST               0 (None)
             20 RETURN_VALUE
"""
