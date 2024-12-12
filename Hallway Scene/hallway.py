def hallway(name):
    print(f"{name} enters the hallway a bit confused but he sees five doors with five different names on them")
    room_choice = int(input("What room do you want to enter? "))
    if room_choice == 1:
        print("welcome to Finn's room")
    elif room_choice == 2:
        print("welcome Rhea's room")
    elif room_choice == 3:
        print("welcome Zara's room")
    elif room_choice == 4:
        print("welcome Luna's room")
    elif room_choice == 5:
        print("welcome Mia's room")
    else:
        print("wrong answere")

username = "Arsalan"
hallo = hallway(username)