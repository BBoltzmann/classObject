
def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    numbers = [str(alphabet.index(letter.lower())) for letter in text if letter.lower() in alphabet]
    print(numbers)
    return ' '.join(numbers)

print(alphabet_position("abcdefghijklmnopqrstuvwxyz"))