def second_order_generator(z1, z2):
    # 11*z1 = 8*z1 + 2*z1 + z1
    term1 = (z1 << 3) + (z1 << 1) + z1

    # 7*z2 = 4*z2 + 2*z2 + z2
    term2 = (z2 << 2) + (z2 << 1) + z2

    # mod 16
    return (term1 + term2) & 15

def get_period():
    z0, z1 = 11, 14   # სწორად, ამოცანის მიხედვით
    seen = {}
    step = 0

    while (z0, z1) not in seen:
        seen[(z0, z1)] = step
        z_next = second_order_generator(z1, z0)
        z0, z1 = z1, z_next
        step += 1

    period = step - seen[(z0, z1)]
    return period


print(get_period())
