import random
import math

def uniform_integer(m, n):
    """
    დისკრეტული შემთხვევითი სიდიდის გენერაცია
    თანაბარი განაწილებით ინტერვალზე [m, m+n]
    """
    # შემთხვევითი რიცხვი U ~ (0,1)
    U = random.random()

    # შებრუნებული გარდაქმნის ფორმულა
    X = m + math.floor((n + 1) * U)

    return X


# ==========================
# ტესტირება
# ==========================

m = 3
n = 4   # ინტერვალი იქნება [3, 7]

for i in range(10):
    print(uniform_integer(m, n))
