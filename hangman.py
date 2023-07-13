import random, hangman_words, hangman_art

stages = hangman_art.stages
print(hangman_art.logo)
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
print("chosen word ",chosen_word)
lives = 6
display = []
for item in chosen_word:
    display.append('_')
while '_' in display:
    guess = input("Guess a latter ").lower()
    if guess in display:
        print("You'h alread guessed it.")
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[lives])
        lives -=1
        if lives < 0:
            print("You Lose!")
            break
    if '_' not in display:
        print("You Win!")

    print(' '.join(display))