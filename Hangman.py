
input_word = input("Insert the word to be guessed:").strip().lower()
tried_letters = set()
encoded_word = []

tried_letters.add(input_word[0])
tried_letters.add(input_word[-1])

for index, value in enumerate(input_word):
    if value == input_word[0]:
        encoded_word.append(value)
    elif value == input_word[-1]:
        encoded_word.append(value)
    else:
        encoded_word.append("_")

nr_of_lives = 7
while nr_of_lives > 0:
    print(encoded_word)
    input_letter = input("Insert lower letter:").strip().lower()
    if input_letter.isalpha():
        if input_letter not in tried_letters:
            tried_letters.add(input_letter)
            found_match = False
            for index, value in enumerate(input_word):
                if value == input_letter:
                    encoded_word[index] = input_letter
                    found_match = True

            if found_match is True:
                print("Letter {letter} matches in word".format(letter=input_letter))
                if "_" not in encoded_word:
                    break;
            else:
                nr_of_lives -= 1
                print("Letter {letter} does not match.\nYou have {lives} lives left".format(letter=input_letter, lives=nr_of_lives))
        else:
            print("Letter {letter} has already been tried".format(letter=input_letter))
    else:
        print("Character {char} is not a valid letter".format(char=input_letter))

if nr_of_lives == 0:
    print("You lost. The word was {word}".format(word=input_word))
else:
    print("You won. Congrats!!!")
