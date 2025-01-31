Miapointtally = 0
username = "Player"

def mia_room(name):
    global Miapointtally
    print(f"\n*{name} enters the room, Mia looks up.*")

    while True:
        choice = input('''\nHow do you greet her?
1. Greet politely
2. Greet aggressively
''')
        if choice == "1":
            print(f"\n*{name} greets Mia politely, but she does not respond.*")
            Miapointtally += 0
            break
        elif choice == "2":
            print(f"\n*{name} greets Mia aggressively, she frowns and suddenly knocks you out.*")
            Miapointtally += 2
            print("\nYou gain +2 points but get kicked out.")
            break
        else:
            print("\nPlease enter one of the available numbers!")
    
    if Miapointtally > 1:
        print("\nCongratulations! You gained some points, but at a cost.")
    elif Miapointtally == 0:
        print("\nZara is indifferent to your presence.")
    else:
        print("\nYou might need to rethink your approach!")

# Start of the game
print("Welcome to the Mia interaction game!")
enter_room(username)
print(f"Mia's point tally: {Miapointtally}")

if Miapointtally > 1:
    print("\nCongratulations! You gained some points, but at a cost.")
elif Miapointtally == 0:
    print("\nZara is indifferent to your presence.")
else:
    print("\nYou might need to rethink your approach!")
