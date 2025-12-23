def quadratic_generator(z_prev):
    """
    ეს ფუნქცია გამოთვლის შემდეგ მნიშვნელობას კვადრატული კონგრუენტული გენერატორისთვის:
    z_i = (11 * z_{i-1}^2 + 7 * z_{i-1} + 3) mod 16
    გამოიყენება ბიტური ოპერაცია (& 15) mod 16-ის ნაცვლად, რადგან 16=2^4 და & (16-1) იძლევა mod 16-ს დადებითი რიცხვებისთვის.
    """
    return (11 * z_prev * z_prev + 7 * z_prev + 3) & 15  # ბიტური AND 15-ით mod 16-ის გამოსათვლელად

def get_period(seed):
    """
    დამხმარე ფუნქცია პერიოდის გამოსათვლელად მოცემული საწყისი მნიშვნელობისთვის.
    იყენებს ლექსიკონს (dictionary) განმეორების აღმოსაჩენად.
    """
    seen = {}  # შენახული მდგომარეობები და მათი ნაბიჯები
    z = seed
    step = 0
    while z not in seen:
        seen[z] = step
        z = quadratic_generator(z)
        step += 1
    return step - seen[z]  # პერიოდის სიგრძე

periods = [get_period(i) for i in range(16)]
max_period = max(periods)
print(max_period)  # გამოტანს 4-ს