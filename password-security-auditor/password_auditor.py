print("Password Security Auditor")
password = input("Enter a password: ")
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

print("Password Length:", length)
print("Contains Uppercase:", has_upper)
print("Contains Lowercase:", has_lower)
print("Contains Digit:", has_digit)
print("Contains Special Character:", has_special)
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

print("Score:", score)

if score <= 2:
    strength = "Weak"

elif score <= 4:
    strength = "Moderate"

else:
    strength = "Strong"

print("Strength:", strength) 


