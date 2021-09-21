from math import inf
from random import randint
import sys
def count_mask(n):
    res = 0
    for i in range(n):
        res += 2 ** i
    return res

n = {
    "l11": 11,
    "l9": 9,
    "l10": 10
    }
taps = {
    "l11": (0, 2),
    "l9": (0, 1, 3, 4),
    "l10": (0, 3)
    }

masks = {
    n["l11"]: count_mask(n["l11"]),
    n["l9"]: count_mask(n["l9"]),
    n["l10"]: count_mask(n["l10"])
    }

lehmer_const = {'m': 2**32, 'a': 2**16+1, 'c': 119, 'x0': randint(1, sys.maxsize)}