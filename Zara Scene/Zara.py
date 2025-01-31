Zarapointtally = 0
username = "Player"

def zara_room(name):
    global Zarapointtally
    print(f"\n*{name} enters the room, Zara looks up and greets you.*")

    while True:
        choice = input('''\nHow do you greet her?
1. Hug
2. Nod head
3. Shake hands
''')
        if choice == "1":
            print(f"\n*{name} hugs Zara, she smiles warmly.*")
            Zarapointtally += 3
            break
        elif choice == "2":
            print(f"\n*{name} nods at Zara, she nods back with a polite smile.*")
            Zarapointtally += 2
            break
        elif choice == "3":
            print(f"\n*{name} shakes Zara's hand, she looks a bit confused but goes along with it.*")
            Zarapointtally -= 2
            break
        else:
            print("\nPlease enter one of the available numbers!")

def join_her(name):
    global Zarapointtally
    print(f"\n*Zara sits down and invites {name} to join her.*")

    while True:
        choice = input('''\nWhat do you do?
1. Act indifferent
2. Act interested
''')
        if choice == "1":
            print(f"\n*{name} acts indifferent, Zara feels offended and asks you to leave.*")
            print("You got kicked out of the room.")
            Zarapointtally -= 5
            break
        elif choice == "2":
            print(f"\n*{name} shows interest in what Zara is doing. She smiles and suggests watching a movie together.*")
            watch_movie(name)
            break
        else:
            print("\nPlease enter one of the available numbers!")

def watch_movie(name):
    global Zarapointtally
    print(f"\n*{name} and Zara watch a movie together, creating a warm and friendly atmosphere.*")
    print(f"\n*Zara seems impressed by your company.*")
    Zarapointtally += 3
    if Zarapointtally > 5:
        print("\nCongratulations! You won Zara's love.")
    elif Zarapointtally > 0:
        print("\nYou left a positive impression on Zara.")
    else:
        print("\nYou might need to work on your social skills!")

# Start of the game
print("Welcome to the Zara interaction game!")
enter_room(username)
print(f"Zara's point tally: {Zarapointtally}")
join_her(username)
print(f"Zara's point tally: {Zarapointtally}")

if Zarapointtally > 5:
    print("\nCongratulations! You won Zara's love.")
elif Zarapointtally > 0:
    print("\nYou left a positive impression on Zara.")
else:
    print("\nYou might need to work on your social skills!")
