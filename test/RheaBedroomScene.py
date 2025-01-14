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
if current_room == 2:
    Rheapointtally = 2
username = "Arsalan"
def Rheascene1 (name):
    global Rheapointtally
    print(f"\n*{name} enters Rhea's room, you quickly scan the room and catch Rhea doing her morning routine.*")
   
    while True:
        choice1 = input('''\nWhat do you do? 
1. Join in 
2. Stare 
3. Smash
''')
        if choice1 == "1":
            print(f"\n*{name} asks to join Rhea's yoga session, she nods and you join in*")
            Rheapointtally += 2
            break
        elif choice1 == "2":
            print(f"\n*{name} stands and creeps on Rhea, she notices you staring and mutters to herself* \n-What a wierdo.")
            Rheapointtally -= 2
            break
        elif choice1 == "3":
            print(f"\n*{name} runs up and hit Rhea across the head causing her to get a headache, she rubs her head in confusion* \n-WTH HELL IS WRONG WITH YOU? \n*She yells at you. {name} decides to apolegize, she forgives you but will not forget your actions*")
            Rheapointtally -= 3
            break
        else:
            print("\nPlese enter one of the available numbers!")

def Rheascene2 (name):
    global Rheapointtally
    print(f"\nSo whats your favorite position in yoga {name}? *Rhea asks trying to strike conversation*")

    while True:
        choice2 = input('''\nWhats your response?
1. Downward dog 
2. Doggystyle
3. I prefer dancing
''')
        if choice2 == "1":
            print(f"\nReally, what a coincedence thats my favorite too. *Time passes and you decide to leave her room*")
            Rheapointtally += 3
            break
        if choice2 == "2":
            print(f"\n*Rhea gives {name} a look of disgust, and asks you to leave her room*")
            Rheapointtally -= 5
            break
        if choice2 == "3":
            print(f"\nReally i didnt take you for a dancer. I challange you to a dance battle!")
            Rheapointtally += 4
            
            while True:
                choice3 = input(f'''\nRhea challanges {name} to a dance battle she begins to floss, what is your next move?
        1. Lose intentionally
        2. Win and embarres her
        3. Have a fun battle
        ''')
                if choice3 == "1":
                    print(f"\n*Rhea notices {name} going easy on her and gets dissapointed. {name} leaves her room*")
                    Rheapointtally -= 2
                    break
                if choice3 == "2":
                    print(f"\n*{name} goes crazy and get sturdy on her ass, she smiles as you defeat her and blows {name} a kiss as you leave her room*")
                    Rheapointtally += 4
                    break
                if choice3 == "3":
                    print(f"\n*{name} start dancing matching her tempo creating a fun and flirty atmopshere, she kisses {name}'s cheek before you leave her room*")
                    break
                else: 
                     print("\nPlese enter one of the available numbers!")
            break
        else:
            print("\nPlese enter one of the available numbers!")     
Rheascene1(username)
print(f"Rhea's point tally {Rheapointtally}")
Rheascene2 (username)
print(f"Rhea's point tally {Rheapointtally}")
