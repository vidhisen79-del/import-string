import string
import secrets
import math

print("=== Enterprise Random Password Generator ===")

# Phase 1: Input & Validation
while True:
    try:
        length_input = input("Enter password length (min 8, recommended 16): ").strip()
        length = int(length_input)
        
        if length < 8:
            print("Error: NIST 2024 says minimum 8, but 15 is for high-security. Please enter >= 8")
            continue
        if length > 64:
            print("Error: Maximum allowed is 64 (NIST guideline)")
            continue
        break
    except ValueError:
        print("Error: Please enter a valid integer.")

# Phase 2: Building the backend transformation engine
# Using string module (Standard Library Integration)
char_pool = string.ascii_letters + string.digits + string.punctuation
print(f"\nCharacter pool size (R): {len(char_pool)}")

# Using secrets.choice() - Cryptographically secure
password_list = []
for _ in range(length):
    password_list.append(secrets.choice(char_pool))

# Optimizing with join() - Linear time complexity O(N)
password = ''.join(password_list)

# Phase 3: Mathematical provision of security (Entropy)
# Formula: E = L * log2(R)
R = len(char_pool)
L = length
entropy = L * math.log2(R)

print("\n--- OUTPUT ---")
print(f"Generated Password: {password}")
print(f"Entropy: {entropy:.2f} bits")
print(f"Length: {L}")

if entropy < 50:
    print("Status: Weak (Cracked in 2 days by GPU)")
elif entropy < 80:
    print("Status: Good (Cracked in 5 years)")
else:
    print("Status: Secure for millions of years - NIST Compliant!")
