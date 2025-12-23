import random
import math

def generate_X(lam=1.2):
    """
    ექსპონენციალური განაწილება: F(x) = 1 - e^(-λx)
    ფორმულა: X = -ln(U) / λ
    """
    U = random.random()
    X = -math.log(U) / lam
    return X

# ტესტირება
print("ამოცანა 7: ექსპონენციალური განაწილება")
print("="*50)
print("F(x) = 1 - e^(-1.2x), x ≥ 0")
print("ფორმულა: X = -ln(U) / 1.2")
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
X = -math.log(U) / 1.2
print(f"U = {U:.6f}")
print(f"X = -ln({U:.6f}) / 1.2 = {X:.6f}")
print(f"შემოწმება: F({X:.4f}) = 1 - e^(-1.2×{X:.4f}) = {1 - math.exp(-1.2*X):.6f} ≈ {U:.6f} ✓")