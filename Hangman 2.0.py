import random
words = ["score", "flies", "stark", "slice", "flame", "light", "lazor", "fight", "sling", "sting", "quiet", "lemon", "phone", "write", "while", "stern", "block", "rusty", "start"]
while True:
    n = random.randint(0, 18)
    word = words[n]
    guessword =["_", "_", "_", "_", "_"]
    guesses = []
    lives = 6
    print(guessword[0], guessword[1], guessword[2], guessword[3], guessword[4])
    while True:
        guess = input("Please enter your guess: ")
        if guess in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" and len(guess) == 1:
            if guess.lower() in word:
                a = word.index(guess.lower())
                guessword[a] = guess.lower()
                print(guessword[0], guessword[1], guessword[2], guessword[3], guessword[4])
                guesses.append(guess)
                a = None
                guess = None
                if guessword[0] + guessword[1] + guessword[2] + guessword[3] + guessword[4] == word:
                    print("You have won with {0} chances left. The word was {1}".format(lives, word))
                    break
            else:
                if guess in guesses:
                    print("You have already guessed that letter")
                    print(guessword[0], guessword[1], guessword[2], guessword[3], guessword[4])
                else:
                    lives = lives - 1
                    guesses.append(guess)
                    if lives > 0:
                        print("That was a wrong guess. You now have {} chance left".format(lives))
                        print(guessword[0], guessword[1], guessword[2], guessword[3], guessword[4])
                        continue
                    elif lives == 0:
                        print("GAME OVER")
                        print("That was a wrong guess")
                        print("You have lost")
                        print("The word was {}".format(word))
                        break
        else:
            print("Please enter a single letter as your guess")
            print(guessword[0], guessword[1], guessword[2], guessword[3], guessword[4])
            continue
    while True:
        playagain = input("Do you want to play again?: ")
        if playagain.lower() == "yes" or playagain.lower() == "no":
            break
        else:
            print("Please enter 'Yes' or 'No'")
            continue
    if playagain.lower() == "yes":
        continue
    else:
        print("Thank you for playing. Please come back again")
        break