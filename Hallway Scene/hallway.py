current_room = 0
def hallway(name):
    global current_room
    print(f"\n{name} enters the hallway a bit confused but he sees five doors with five different names on them")
    while True:
        room_choice = input("""What room do you want to enter? 
(following rooms are:)
1-Finn
2-Rhea
3-Zara
4-Luna
5-Mia
(Write the number of the chosen room!): """)
        current_room = 0
        if room_choice == "1":
            print(f"\n*{name} sneaks in Finn's room*")
            current_room += 1
            break
        elif room_choice == "2":
            print(f"\n*{name} sneaks in Rhea's room*")
            current_room += 2
            break
        elif room_choice == "3":
            print(f"\n*{name} sneaks in Zara's room*")
            current_room += 3
            break
        elif room_choice == "4":
            print(f"\n*{name} sneaks in Luna's room*")
            current_room += 4
            break
        elif room_choice == "5":
            print(f"\n*{name} sneaks in Mia's room*")
            current_room += 5
            break
        else:
            print(f"\nNot an available room {name} you stupid fuck")

username = "Arsalan"
hallo = hallway(username)