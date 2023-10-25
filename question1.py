print("Question 1:")
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

print('question 2:')
email = email.lower()

vowels = "aeiou"
vowel_count = 0
consonant_count = 0
special_count = 0
total_count = 0
char_counts = {}

for i in email:
    if i.isalpha():
        total_count += 1  # Increment the total character count
        if i in vowels:
            vowel_count += 1
            char_type = 'vowel'
        else:
            consonant_count += 1
            char_type = 'consonant'
    else:
        total_count += 1  # Increment the total character count for special characters
        special_count += 1
        char_type = 'special character'

    # Check if the character is already in char_counts, and increment the count, or add it to the dictionary with a count of 1.
    if i in char_counts:
        char_counts[i][0] += 1
    else:
        char_counts[i] = [1, char_type]


print(f"\nVowel Count: {vowel_count}")
print(f"Consonant Count: {consonant_count}")
print(f"Special Character Count: {special_count}")
print(f"Total Character Count: {total_count}")

print("\nCharacter Counts:")
for char, (count, char_type) in char_counts.items():
    print(f"'{char}' => {count} => {char_type}")

print("question 3:")

for i in email:
    if i.isdigit():  # Checking if the character is a digit
        num = int(i)  # Converting the character to an integer
        if (num % 2 == 0) or (num % 3 == 0) or (num % 5 == 0):
            print(str(num))

print("question 4:")


print("ASCII values for the characters in the email address:")

for char in email:
    ascii_value = ord(char)
    print(f"Character: {char}, ASCII Value: {ascii_value}")
