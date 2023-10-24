email = input("Enter your email address: ")

for i in email:
    if i.isdigit():  # Checking if the character is a digit
        num = int(i)  # Converting the character to an integer
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            print(str(num))
