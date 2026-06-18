print("Password Security Auditor")
password = input("Enter a password: ")
length = len(password)

has_upper = False

for char in password:
    if char.isupper():
        has_upper = True

print("Password Length:", length)
print("Contains Uppercase:", has_upper)

