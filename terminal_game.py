
import os
import time
import sys
import questionary

def main_menu(turns = 0):
    action = questionary.select(
        "What would you like to do?",
        choices=[
            "Start Game",
            "Options",
            "Quit"
        ]
    ).ask()

    if action == "Start Game":
        if turns <5 :
        # Start the game
            game_loop()
            main_menu()
        else:
            print("You have reached the maximum number of turns.")
    elif action == "Options":
        # Display options
        pass
    elif action == "Quit":
        # Quit the game
        pass


def game_loop():
    player = input("Enter a your name : ")

    print(f"\n\nWelcome {player} the brave adventurer!\n\n")
    def failure(why):
        print(why, f"\nYou lost {player} GAME OVER!")
        exit(0)
    def win(message):
        print(message,f'\nCongrats! You get the legendary artifact of Green elf.\n You win the game.')


    def typewriting_effect(sentence, type_delay,color):
        for char in sentence:
            sys.stdout.write(f"\033[38;5;{color}m{char}\033[0m")
            sys.stdout.flush()
            time.sleep(type_delay)
        
    # Typing speed (in seconds)
    type_delay = 0.1  
    # Blue, green, gray
    colors = [12, 10, 14] 

    sentences = [
    '------------------\nThe Lost Relic\n------------------\n'
    'Game Instructions:\n',
    'Actions: The player can perform choices.According to his/her choice , she/he can gain victory.\n'
    'Victory: Defeat the Goblin King and get the legendary relic of green elf.\n',
    '------------------\n'
    '------------------\n'
    '       Start\n'
    '------------------\n'
    '------------------\n',
    'You are a brave adventurer who has heard tales of a legendary relic hidden deep within the treacherous Goblin Caverns. This relic is said to grant immense power to its holder. Armed with only your wits and a trusty sword, you will venture into the darkness, facing hordes of goblins and their fearsome leader, the Goblin King.\n',
    '-----------------\n'
    'A goblin is standing in front of you .Now your time to choose warrior what will you do .\n '
    ]

    for i, sentence in enumerate(sentences):
        typewriting_effect(sentence, type_delay, colors[i % len(colors)])
        time.sleep(1) 

    Choice = int(input('What is your choice?\n 1)Stab on the neck straight.\n 2) Make a faint on stomach first and then diverse the way of attack towards neck.\n'))
    if Choice == 1:
        failure('You have stabbed on the neck straight.You lose your life because of your meager strength.')
    else:
        print('You have made a faint on stomach first and then diverse the way of attack towards neck.You have killed the goblin using your brain.')

    def solve_puzzle():
        code = "1234"  
        attempts = 0
        while attempts < 8:
            user_code = input("Enter the code to unlock the door: ")
            attempts += 1
            if user_code == code:
                print("Congratulations! You entered the correct code and unlocked the door.")
                break
            else:
                print("Incorrect code. Try again.")
        else:
            failure("You have entered too many incorrect codes. The door remains locked.")

    def defend_yourself():
        choice = int(input("An unknown attacker approaches! What do you do?\n 1) Run away. \n 2) Try to use a self-defense technique.\n 3) Other chances.\n"))

        if choice == 1:
            failure("You run away.")
        elif choice == 2:
            print("You use a self-defense technique to deter the attacker (assuming you're trained). It's always best to avoid violence if possible. Be a fisherman. ")
        else:
            failure("You don't have more choices.")

    def typewriting_effect(sentence, type_delay,color):
        for char in sentence:
            sys.stdout.write(f"\033[38;5;{color}m{char}\033[0m")
            sys.stdout.flush()
            time.sleep(type_delay)
    colors = [12, 10, 14]  
    # Typing speed (in seconds)
    type_delay = 0.1  
    # Blue, green, gray
    sentences = [
    '------------------\nAfter a long fighting, you have become more and more stronger. Now you have stumbled upon a strange looking door inside a dungeon.You are puzzled about how to open the door.Now the time for choice has come.\n------------------\n'
    ]
    for i, sentence in enumerate(sentences):
        typewriting_effect(sentence, type_delay, colors[i % len(colors)])
        time.sleep(1) 
    solve_puzzle()

    def typewriting_effect(sentence, type_delay,color):
        for char in sentence:
            sys.stdout.write(f"\033[38;5;{color}m{char}\033[0m")
            sys.stdout.flush()
            time.sleep(type_delay)
    colors = [12, 10, 14]  
    # Typing speed (in seconds)
    type_delay = 0.1  
    # Blue, green, gray



    sentences = [
    '------------------\n After opening the door, there is a total silence. Everything is dark. You have used a illuminator to see the way in front you.  ------------------\n'

    '------------------\n'
    'After a long interval, you hear some noise and feel a terrifying oppression.Someone is coming.What will you do?\n'
    ]
    for i, sentence in enumerate(sentences):
        typewriting_effect(sentence, type_delay, colors[i % len(colors)])
        time.sleep(1) 

    defend_yourself()
    def typewriting_effect(sentence, type_delay,color):
        for char in sentence:
            sys.stdout.write(f"\033[38;5;{color}m{char}\033[0m")
            sys.stdout.flush()
            time.sleep(type_delay)
    colors = [12, 10, 14]  
    # Typing speed (in seconds)
    type_delay = 0.1  
    # Blue, green, gray

    sentences = ["Now you have already made your first attack. You have not lose your composure.But you have already understood that this is the goblin king.The goblin king's gnarled fingers curled around the hilt of his rusty sword, his eyes glinting with a malicious intelligence. He is not mindless brute, a fact you have learned the hard way. Your initial charge had been met with a counterattack that was swift and precise.\n----------------\n Slowly a long time passed. You have  studied him, searching for weaknesses, for any chink in his armor. His form is hunched, his movements deliberate, but there was an underlying restlessness, a caged energy. Perhaps it was arrogance, a belief in his invincibility. Or maybe, just maybe, fear. The fear of a challenger who wasn't afraid to die.\n"

    "With a renewed sense of purpose, you grip your own weapon tighter. This is a game, a deadly chess match where every move is counted. And you are far from checkmate.\n "

    "The goblin king movement looks like a deadly ballet of shadows. Each step is deliberate, each gesture a threat.You are trying to find for a opening. All of a sudden, you found a way for attack. A wound on his chest is opened. Now it's time for you to make a choice....\n"]
    for i, sentence in enumerate(sentences):
        typewriting_effect(sentence, type_delay, colors[i % len(colors)])
        time.sleep(1) 
    decision = int(input("What is your choice?\n 1)Stab on the wound straight.\n 2) Make a faint on neck first and then diverse the way of attack towards chest.\n"))
    if decision == 1:
        failure("You have stabbed on the wound straight.But that is a ambush. You lose your life because of your meager strength.")
    else:
        win("You have made a faint on neck first and then diverse the way of attack towards chest.You have slain the goblin king.")
    # Set the time limit in seconds
    time_limit = 5
    # Wait for the specified time
    time.sleep(time_limit)
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    def typewriting_effect(sentence, type_delay,color):
        for char in sentence:
            sys.stdout.write(f"\033[38;5;{color}m{char}\033[0m")
            sys.stdout.flush()
            time.sleep(type_delay)
    # Blue, green, gray
    colors = [12, 10, 14]  
    # Typing speed (in seconds)
    type_delay = 0.1  

    sentences = ["                                 The End..."]

    for i, sentence in enumerate(sentences):
        typewriting_effect(sentence, type_delay, colors[i % len(colors)])
        time.sleep(1) 

    # Set the time limit in seconds
    time_limit = 5
    # Wait for the specified time
    time.sleep(time_limit)
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main_menu()













