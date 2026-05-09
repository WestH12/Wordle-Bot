import frequency
import entropy

frequency.check_hashes()
word_freq = frequency.get_freq()

guess = 1
legal_guesses = frequency.legal_guesses
print("Welcome to Westley's Wordle Bot!")
print('Try the first guess of: crane')
while True:
    if guess == 1:
        word = 'crane'
    else:
        word = entropy.tot_guess_eval(legal_guesses)

    feedback = input('Feedback: ').strip()
    if feedback == '22222':
        print(f"Congratulations on guessing the word in {guess} turn")
        again = input("Do you want to play again? ").lower()
        if again == 'yes':
            legal_guesses = frequency.legal_guesses
            guess = 1
            print("\nWelcome to Westley's Wordle Bot!")
            print('Try the first guess of: crane')
        else:
            break
    else:
        legal_guesses = entropy.redefine_list(word, legal_guesses, feedback)
        guess += 1

