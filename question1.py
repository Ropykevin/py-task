email = input("Enter your email adress: ")
at_index = 1
dot_index = -1
for i in range(len(email)):
    if email[i] == '@':
        at_index = i
        parts = email.split('@')
    elif email[i] == '.':
        dot_index = i
if at_index >1 and dot_index <len(email)-1 and dot_index > at_index:
    print(f"{email} is a valid email")
else:
    print(f"{email}  is an invalid email")

id= f"ID: {parts[0]}"
domain=f"DOMAIN: {parts[1]}"
print(id)
print(domain)

