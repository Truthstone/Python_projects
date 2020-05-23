import random

choice = ["python", "java", "javascript", "kotlin"]
prime_choice = random.choice(choice)
system_choice = list(prime_choice)
guessed_string = ["-"] * len(system_choice)
selection_set = set(prime_choice)
print("H A N G M A N")
start_choice = input('Type "play" to play the game, "exit" to quit: > play')
guesses = set()
life = 0
while start_choice == "play":
    while life < 8:
        print()
        print()
        print("".join(guessed_string))
        guess = input("Input a letter: ")
        if guess in selection_set:
            guessed_string[system_choice.index(guess)] = guess
            system_choice[system_choice.index(guess)] = "-"
            selection_set.remove(guess)

        else:
            if len(guess) != 1:
                print("You should print a single letter")
            elif not(97 <= ord(guess) <= 122):
                print("It is not an ASCII lowercase letter")
            elif guess in guesses:
                print("You already typed this letter ")
            else:
                print("No such letter in the word")
                life += 1
        guesses.add(guess)
        if "".join(guessed_string) == prime_choice:
            print("You guessed the word!")
            print("You survived!")
            break
    else:
        print("You are hanged!")
else:
    exit(0)
