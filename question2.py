# email = input("Enter your email address: ")

# vowels = "aeiou,AEIOU"
# vowel_count = 0
# consonant_count = 0
# special_count = 0

# for i in email:
#     if i.isalpha():
#         if i in vowels:
#             vowel_count += 1
#         else:
#             consonant_count += 1
#     else:
#         special_count += 1

# print("Vowels: ", vowel_count)
# print("Consonants: ", consonant_count)
# print("Special characters: ", special_count)

email = input("Enter your email address: ")

# Convert the email to lowercase for case-insensitive counting
email = email.lower()

vowels = "aeiou"
vowel_count = 0
consonant_count = 0
special_count = 0

for i in email:
    if i.isalpha():
        if i in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    else:
        special_count += 1

    print(f"{i} is a {'vowel' if i in vowels else 'consonant' if i.isalpha() else 'special character'}")

print(f"\nVowel Count: {vowel_count}")
print(f"Consonant Count: {consonant_count}")
print(f"Special Character Count: {special_count}")
