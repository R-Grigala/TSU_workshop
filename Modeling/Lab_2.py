import struct  # IEEE 754 single precision float-ის ბიტური მანიპულაციისთვის

def float_to_bits(f):
    """Float-ს გარდაქმნის 32-ბიტიან unsigned int-ად (ბიტური წარმოდგენა)"""
    return struct.unpack('!I', struct.pack('!f', float(f)))[0]

def bits_to_float(bits):
    """32-ბიტიან unsigned int-ს გარდაქმნის float-ად"""
    return struct.unpack('!f', struct.pack('!I', bits))[0]

# მოცემული მნიშვნელობები ამოცანა 2-დან
a = 98710293.53201
b = 189029.238

# 1. 256 * a — ბიტურად: ექსპონენტას +8 (რადგან 256 = 2^8)
a_bits = float_to_bits(a)
sign_a = a_bits >> 31
exp_a = (a_bits >> 23) & 0xFF
mant_a = a_bits & 0x7FFFFF

new_exp_a = exp_a + 8  # არ ხდება overflow (exp_a ≈153)
scaled_a_bits = (sign_a << 31) | (new_exp_a << 23) | mant_a
scaled_a = bits_to_float(scaled_a_bits)  # ზუსტად 256 * a (მანტისა არ კარგავს სიზუსტეს)

# 2. 7 % 1024 = 7 (უბრალოდ კონსტანტა)
add_part = 7.0

# 3. b / 256 — ბიტურად: ექსპონენტას -8
b_bits = float_to_bits(b)
sign_b = b_bits >> 31
exp_b = (b_bits >> 23) & 0xFF
mant_b = b_bits & 0x7FFFFF

new_exp_b = exp_b - 8  # არ ხდება underflow
scaled_b_bits = (sign_b << 31) | (new_exp_b << 23) | mant_b
scaled_b = bits_to_float(scaled_b_bits)  # ზუსტად b / 256 (მანტისა უცვლელი)

# 4. საბოლოო შედეგი: (256*a + 7) % 1024 + b/256
# ჯერ გამოვთვალოთ (scaled_a + 7) % 1024 ბიტურად (მთელ ნაწილზე)
int_part = int(scaled_a + add_part)  # მთელი ნაწილი (scaled_a დიდი დადებითია)
mod_part = int_part % 1024          # % 1024 მთელზე (ბიტურად: & 1023)
result = mod_part + scaled_b        # + b/256 (წილადი ნაწილი)

print("შედეგი ბიტური ოპერაციებით:", result)