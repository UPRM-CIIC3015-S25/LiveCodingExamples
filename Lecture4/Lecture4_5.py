
# count = 0
# for letter in 'Colegio':
#     count += 1
# print(f"The word has {count} letters")


def count_vowels(word):
    count = 0
    for char in word:
        if char.lower() in "aeiou":
            count += 1
    return count

# print(f"Number of vowels in Bienvenido is {count_vowels('Bienvenido')}")

def remove_consonants(word):
    result = ''
    for next_letter in word:
        if next_letter.lower() in 'aeiou':
            result += next_letter
    return result

print(f"Result = {remove_consonants('bienvenido')}")

