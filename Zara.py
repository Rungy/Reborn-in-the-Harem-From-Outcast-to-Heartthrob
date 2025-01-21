Rheapointtally = 0
username = "Player"

def enter_room(name):
    global Rheapointtally
    print(f"\n*{name} enters the room, Rhea looks up and greets you.*")

    while True:
        choice = input('''\nHow do you greet her?
1. Hug
2. Nod head
3. Shake hands
''')
        if choice == "1":
            print(f"\n*{name} hugs Rhea, she smiles warmly.*")
            Rheapointtally += 3
            break
        elif choice == "2":
            print(f"\n*{name} nods at Rhea, she nods back with a polite smile.*")
            Rheapointtally += 2
            break
        elif choice == "3":
            print(f"\n*{name} shakes Rhea's hand, she looks a bit confused but goes along with it.*")
            Rheapointtally -= 2
            break
        else:
            print("\nPlease enter one of the available numbers!")

def join_her(name):
    global Rheapointtally
    print(f"\n*Rhea sits down and invites {name} to join her.*")

    while True:
        choice = input('''\nWhat do you do?
1. Act indifferent
2. Act interested
''')
        if choice == "1":
            print(f"\n*{name} acts indifferent, Rhea feels offended and asks you to leave.*")
            print("You got kicked out of the room.")
            Rheapointtally -= 5
            break
        elif choice == "2":
            print(f"\n*{name} shows interest in what Rhea is doing. She smiles and suggests watching a movie together.*")
            watch_movie(name)
            break
        else:
            print("\nPlease enter one of the available numbers!")

def watch_movie(name):
    global Rheapointtally
    print(f"\n*{name} and Rhea watch a movie together, creating a warm and friendly atmosphere.*")
    print(f"\n*Rhea seems impressed by your company.*")
    Rheapointtally += 3

# Start of the game
print("Welcome to the Rhea interaction game!")
enter_room(username)
print(f"Rhea's point tally: {Rheapointtally}")
join_her(username)
print(f"Rhea's point tally: {Rheapointtally}")

if Rheapointtally > 5:
    print("\nCongratulations! You won Rhea's love.")
elif Rheapointtally > 0:
    print("\nYou left a positive impression on Rhea.")
else:
    print("\nYou might need to work on your social skills!")
