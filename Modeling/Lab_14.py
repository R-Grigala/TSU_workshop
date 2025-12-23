import random  # იმპორტი random მოდულის, რომელიც გვაძლევს შემთხვევითი რიცხვების გენერაციის შესაძლებლობას

def generate_bernoulli(p):
    """
    დამხმარე ფუნქცია ბერნულის განაწილებისთვის Be ~ Bernoulli(p):
    აბრუნებს 1 ალბათობით p, ან 0 ალბათობით 1-p.
    """
    return 1 if random.random() < p else 0  # random.random() იძლევა U ~ Uniform(0,1)

def generate_binomial(n, p):
    """
    ეს ფუნქცია გენერირებს ბინომიალურ შემთხვევით სიდიდეს Bi ~ Binomial(n, p),
    როგორც n დამოუკიდებელი ბერნულის შემთხვევითი სიდიდის ჯამი.
    """
    return sum(generate_bernoulli(p) for _ in range(n))  # ჯამი n ბერნულის ცდის

print(generate_binomial(10, 0.5))  # მაგალითად n=10, p=0.5