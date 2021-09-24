from random import randint

def count_mask(n):
    res = 0
    for i in range(n):
        res += 2 ** i
    return res

n = {
    "l11": 11,
    "l9": 9,
    "l10": 10,
    "l20" : 20,
    "l89" : 89
    }
taps = {
    "l11": (0, 2),
    "l9": (0, 1, 3, 4),
    "l10": (0, 3), 
    "l20" : (0, 11, 15, 17),
    "l89" : (0, 51)
    }

# masks = {
#     n["l11"]: count_mask(n["l11"]),
#     n["l9"]: count_mask(n["l9"]),
#     n["l10"]: count_mask(n["l10"]),
#     n["l20"]: count_mask(n["l20"]),
#     n["l89"]: count_mask(n["l89"]),
#     }

lehmer_const = (2**32, 2**16+1, 119, randint(1, 2**32-1))