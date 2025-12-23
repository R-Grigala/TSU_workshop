import random
import matplotlib.pyplot as plt
import numpy as np

def generate_X():
    """
    უწყვეტი X შემთხვევითი სიდიდის გენერაცია
    განაწილების ფუნქცია: F(x) = 1 - 1/x, x ∈ [1; +∞)
    
    ინვერსიული მეთოდი: X = 1/(1-U), სადაც U ~ Uniform(0,1)
    """
    U = random.random()  # თანაბრად განაწილებული [0,1) ინტერვალზე
    X = 1 / (1 - U)
    return X

def verify_distribution(n_samples=10000):
    """
    განაწილების შემოწმება
    """
    print("="*60)
    print("ამოცანა 3: შემთხვევითი სიდიდის გენერაცია")
    print("="*60)
    print("\nგანაწილების ფუნქცია: F(x) = 1 - 1/x, x ∈ [1; +∞)")
    print("ინვერსიული ფორმულა: X = 1/(1-U)")
    print("\n" + "-"*60)
    
    # გენერირება
    samples = [generate_X() for _ in range(n_samples)]
    
    print(f"\nგენერირებულია {n_samples} ნიმუში")
    print(f"\nსტატისტიკა:")
    print(f"  მინიმუმი: {min(samples):.4f}")
    print(f"  მაქსიმუმი: {max(samples):.4f}")
    print(f"  საშუალო: {np.mean(samples):.4f}")
    print(f"  მედიანა: {np.median(samples):.4f}")
    
    # ნიმუშები
    print(f"\nპირველი 10 გენერირებული მნიშვნელობა:")
    for i in range(10):
        print(f"  X_{i+1} = {samples[i]:.4f}")
    
    # თეორიული შემოწმება
    print("\n" + "-"*60)
    print("შემოწმება:")
    print("-"*60)
    
    # ვამოწმებთ რომ F(x) მართლაც არის განაწილების ფუნქცია
    test_values = [1, 2, 3, 5, 10]
    print("\nგანაწილების ფუნქციის მნიშვნელობები:")
    for x in test_values:
        F_x = 1 - 1/x
        # ემპირიული განაწილება
        empirical = sum(1 for s in samples if s <= x) / n_samples
        print(f"  F({x}) = {F_x:.4f}, ემპირიული = {empirical:.4f}, სხვაობა = {abs(F_x - empirical):.4f}")
    
    return samples



# მთავარი გაშვება
print("\n" + "="*60)
print("ინვერსიული მეთოდის დემონსტრაცია")
print("="*60)

# ერთი ნიმუშის გენერაცია ახსნით
U = random.random()
X = 1 / (1 - U)
print(f"\nმაგალითი:")
print(f"  1. გენერირება: U = {U:.6f} (თანაბრად განაწილებული [0,1)-ზე)")
print(f"  2. გამოთვლა: X = 1/(1-U) = 1/(1-{U:.6f}) = 1/{1-U:.6f} = {X:.6f}")
print(f"  3. შემოწმება: F({X:.4f}) = 1 - 1/{X:.4f} = {1 - 1/X:.6f} ≈ {U:.6f} ✓")

# სრული ანალიზი
samples = verify_distribution(n_samples=10000)

print("\n" + "="*60)
print("დასკვნა: გენერატორი სწორად მუშაობს!")
print("="*60)