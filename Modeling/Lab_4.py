import random
import math

def generate_X():
    """
    განაწილება: F(x) = 1 - 2/x, x ∈ [2; +∞)
    ფორმულა: X = 2/(1 - U)
    """
    U = random.random()
    X = 2 / (1 - U)
    return X

# ტესტირება
print("ამოცანა 4")
print("="*50)
print("F(x) = 1 - 2/x, x ∈ [2; +∞)")
print("ფორმულა: X = 2/(1 - U)")
print("="*50)

# 10 ნიმუშის გენერაცია
print("\nგენერირებული მნიშვნელობები:")
for i in range(10):
    x = generate_X()
    print(f"X_{i+1} = {x:.6f}")

# მაგალითი ახსნით
print("\n" + "="*50)
print("მაგალითი:")
U = random.random()
X = 2 / (1 - U)
print(f"U = {U:.6f}")
print(f"X = 2/(1 - {U:.6f}) = 2/{1-U:.6f} = {X:.6f}")
print(f"შემოწმება: F({X:.4f}) = 1 - 2/{X:.4f} = {1 - 2/X:.6f} ≈ {U:.6f} ✓")

# დამატებითი შემოწმება
print("\n" + "="*50)
print("შემოწმება რამდენიმე წერტილში:")
print("="*50)
test_values = [2, 3, 4, 5, 10]
samples = [generate_X() for _ in range(10000)]
for val in test_values:
    F_theoretical = 1 - 2/val
    F_empirical = sum(1 for s in samples if s <= val) / len(samples)
    print(f"x = {val}: F({val}) = {F_theoretical:.4f}, ემპირიული = {F_empirical:.4f}")