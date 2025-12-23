def linear_congruential_generator(a, c, m, z0):
    """
    წრფივი კონგრუენტული გენერატორი: z_i = (a*z_{i-1} + c) mod m
    
    პარამეტრები:
    a = 25 (მამრავლი)
    c = 5 (მიმატება)
    m = 16 (მოდული)
    z0 = 5 (საწყისი მნიშვნელობა)
    """
    
    # პარამეტრები
    print("პარამეტრები:")
    print(f"a = {a}")
    print(f"c = {c}")
    print(f"m = {m}")
    print(f"z₀ = {z0}")
    print("\n" + "="*50 + "\n")
    
    # გენერირება
    sequence = [z0]
    z_current = z0
    
    print("მიმდევრობის გენერირება:\n")
    print(f"z₀ = {z0}")
    
    for i in range(1, m + 5):  # გენერირება m+5 ელემენტამდე
        z_next = (a * z_current + c) % m
        
        print(f"z_{i} = (25 × {z_current} + 5) mod 16 = {25 * z_current + 5} mod 16 = {z_next}")
        
        # შევამოწმოთ ციკლი
        if z_next in sequence:
            period_start = sequence.index(z_next)
            period = i - period_start
            print(f"\n{'='*50}")
            print(f"ციკლი აღმოჩენილია! z_{i} = z_{period_start} = {z_next}")
            print(f"{'='*50}\n")
            
            print(f"სრული მიმდევრობა: {sequence}")
            print(f"\nპერიოდი: {period}")
            print(f"პერიოდი იწყება ინდექსიდან: {period_start}")
            
            if period_start == 0:
                print(f"\n✓ მაქსიმალური პერიოდი = {period}")
            else:
                print(f"\n⚠ პერიოდი არის {period}, მაგრამ იწყება z_{period_start}-დან")
            
            return sequence, period
        
        sequence.append(z_next)
        z_current = z_next
    
    print("\nპერიოდი ვერ მოიძებნა მოცემულ რაოდენობაში")
    return sequence, None


# გაშვება
a = 25
c = 5
m = 16
z0 = 5

sequence, period = linear_congruential_generator(a, c, m, z0)

print("\n" + "="*50)
print("დასკვნა:")
print("="*50)
print(f"მაქსიმალური პერიოდი: {period}")
print(f"მიმდევრობა: {sequence[:period+1] if period else sequence}")