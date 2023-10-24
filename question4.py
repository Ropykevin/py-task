email = input("Enter your email address: ")

print("ASCII values for the characters in the email address:")

for char in email:
    ascii_value = ord(char)
    print(f"Character: {char}, ASCII Value: {ascii_value}")
