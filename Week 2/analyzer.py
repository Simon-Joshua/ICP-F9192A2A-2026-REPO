import math
import zxcvbn

def calculate_entropy(password):
    if not password:
        return 0
    # Calculate unique characters to find the "pool size" (charset)
    charset = 0
    if any(c.islower() for c in password): charset += 26
    if any(c.isupper() for c in password): charset += 26
    if any(c.isdigit() for c in password): charset += 10
    if any(not c.isalnum() for c in password): charset += 32 # Special chars approx
    
    if charset == 0:
        return 0
        
    # Shannon Entropy formula: Length * log2(charset)
    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

def check_password_strength(password):
    # 1. Basic length check
    length = len(password)
    
    # 2. Basic character checks
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    # 3. Advanced analysis using zxcvbn
    z_results = zxcvbn.zxcvbn(password)
    score = z_results['score'] # Returns a rating from 0 (very weak) to 4 (very strong)
    feedback = z_results['feedback']['suggestions']
    
    # 4. Calculate Entropy
    entropy = calculate_entropy(password)
    
    # Display Results
    print("\n--- Password Analysis Results ---")
    print(f"Password: {password}")
    print(f"Length: {length} characters")
    print(f"Shannon Entropy: {entropy} bits")
    print(f"Security Score (0-4): {score}/4")
    
    if feedback:
        print("Suggestions for improvement:")
        for suggestion in feedback:
            print(f" - {suggestion}")
    else:
        print("Strength Status: Excellent password structure!")
    print("-" * 33)

if __name__ == "__main__":
    print("=== Cyber Security Password Analyzer ===")
    user_password = input("Enter a password to test: ")
    check_password_strength(user_password)
