
def analyze_password(password):
    length = len(password)
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
    
    has_special = False
    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if char in special_characters:
            has_special = True
    
    return length, has_upper, has_lower, has_digit, has_special


def calculate_score(length,
                    has_upper,
                    has_lower,
                    has_digit,
                    has_special):

    score = 0
    
    if length >= 8:
        score += 1
    
    if has_upper:
        score += 1
    
    if has_lower:
        score += 1
    
    if has_digit:
        score += 1
    
    if has_special:
        score += 1
    
    return score


def get_strength(score):

    if score <= 2:
        strength = "Weak"
    
    elif score <= 4:
        strength = "Moderate"
    
    else:
        strength = "Strong"
    
    return strength


def check_common_password(password):

    with open("common_passwords.txt", "r") as file:
        common_passwords = [p.lower() for p in file.read().splitlines()]
    return password.lower() in common_passwords


def display_results(length, has_upper, has_lower, has_digit, has_special,
                    score, strength, is_common):

    print("Password Length:", length)
    print("Contains Uppercase:", has_upper)
    print("Contains Lowercase:", has_lower)
    print("Contains Digit:", has_digit)
    print("Contains Special Character:", has_special)

    print("Score:", score)
    print("Strength:", strength)

    if is_common:
        print("Warning: This is a common password!")


def generate_report(length,
                    has_upper,
                    has_lower,
                    has_digit,
                    has_special,
                    score,
                    strength,
                    is_common
                   ):


    report = f"""
PASSWORD AUDIT REPORT
=====================

Length: {length}
Uppercase: {has_upper}
Lowercase: {has_lower}
Digits: {has_digit}
Special Characters: {has_special}
Common Password: {is_common}

Score: {score}
Strength: {strength}
"""

    with open("reports/audit_report.txt", "w") as file:
        file.write(report)
    print("\nReport generated successfully!")


def show_suggestions(length,
                     has_upper,
                     has_lower,
                     has_digit,
                     has_special):
    print("\nSuggestions:")
    
    if length < 8:
        print("- Use at least 8 characters")
    
    if not has_upper:
        print("- Add uppercase letters")
    
    if not has_lower:
        print("- Add lowercase letters")
    
    if not has_digit:
        print("- Add numbers")
    
    if not has_special:
        print("- Add special characters")
        
def main():
    print("Password Security Auditor")

    password = input("Enter a password: ")

    length, has_upper, has_lower, has_digit, has_special = analyze_password(password)

    score = calculate_score(
        length,
        has_upper,
        has_lower,
        has_digit,
        has_special
    )

    strength = get_strength(score)
    is_common = check_common_password(password)

    display_results(
        length,
        has_upper,
        has_lower,
        has_digit,
        has_special,
        score,
        strength,
        is_common
    )

    
    generate_report(
        length,
        has_upper,
        has_lower,
        has_digit,
        has_special,
        score,
        strength,
        is_common
    )

    show_suggestions(
        length,
        has_upper,
        has_lower,
        has_digit,
        has_special
    )

if __name__ == "__main__":
    main()



