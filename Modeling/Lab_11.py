import random
import math

def generate_normal_approx(mu=2, variance=3):
    """
    ნორმალური შემთხვევითი სიდიდის მიახლოებითი გენერაცია
    12 ერთგვაროვანი შემთხვევითი რიცხვის გამოყენებით

    პარამეტრები:
    mu        -- საშუალო მნიშვნელობა (აქ 2)
    variance  -- დისპერსია (აქ 3)

    აბრუნებს:
    X ~ N(mu, variance)
    """

    # 1. გენერირდება 12 ერთგვაროვანი შემთხვევითი რიცხვი (0,1)-დან
    uniform_numbers = [random.random() for _ in range(12)]

    # 2. ვპოულობთ მათ ჯამს
    S = sum(uniform_numbers)

    # 3. ვიღებთ სტანდარტული ნორმალური სიდიდის მიახლოებას
    Z = S - 6

    # 4. ვგადავდივართ N(mu, variance)-ზე
    sigma = math.sqrt(variance)
    X = mu + sigma * Z

    return X
