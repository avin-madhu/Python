# Form a List of vowels accepted from a given word

word = input('Enter the word: ')
vowels = "aeiouAEIOU"
vowel_list = []
for i in word:
    if i in vowels:
        vowel_list.append(i)
print(vowel_list)
