current_room = 0
def hallway(name):
    global current_room
    print(f"{name} enters the hallway a bit confused but he sees five doors with five different names on them")
    while True:
        room_choice = int(input("What room do you want to enter? "))
        if room_choice == 1:
            print("welcome to Finn's room")
            current_room += 1
            break
        elif room_choice == 2:
            print("welcome Rhea's room")
            current_room += 2
            break
        elif room_choice == 3:
            print("welcome Zara's room")
            current_room += 3
            break
        elif room_choice == 4:
            print("welcome Luna's room")
            current_room += 4
            break
        elif room_choice == 5:
            print("welcome Mia's room")
            current_room += 5
            break
        else:
            print("Not a available room")

username = "Arsalan"
hallo = hallway(username)