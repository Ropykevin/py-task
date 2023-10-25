email = input("Enter your email address: ")
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
