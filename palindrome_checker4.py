# Main function
def palindrome_checker(word):
    init_word = word
    word = word.replace(' ', '')
    word1 = word[::-1]
    if word == word1:
        return f'The word {init_word} is a palindrome!'
    else:
        return f'The word {init_word} is not a palindrome!'

# Presentation
print('Welcome to our palindrome checker! \nEnter the word that you want to check:')
word = input()
print(palindrome_checker(word))
