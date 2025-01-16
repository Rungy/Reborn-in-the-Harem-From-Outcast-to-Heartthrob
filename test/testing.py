username = input("Name? ")

Finnpointtally = 0
Rheapointtally = 2
Zarapointtally = 0
Lunapointtally = 0 
Miapointtally = 0 


def intro(name):
    print("You a 50 year old man. Currently watching and dacing heavily to the new poopkai musik.\n Unkown to you, you are a very heavy man, weighting at 300 pounds")
    input("")
    print(f"\n{name}-kun LOOVVESSS THIS!!!, *suddenly {name}-kuns ankel twists and he falls to his death*")
    input("")
    print("""

 ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓███████▓▒░▒▓████████▓▒░      
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░             
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░             
░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓██████▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░             
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░             
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░      
                                                                 
                                                                 
""")
    hallway(username)

def hallway(name):
    print(f"\n{name} enters the hallway a bit stimulated")
    while True:
        room_choice = input("""\nWhat room do you want to enter? 
(following rooms are:)
1-Finn
2-Rhea
3-Zara
4-Luna
5-Mia
(Write the number of the chosen room!): """)
        if room_choice == "1":
            if Finnpointtally >= 0:
                print(f"\n*{name} sneaks in Finn's room*")
            else:
                print("\nThe door is locked")
        elif room_choice == "2":
            if Rheapointtally >= 0:
                print(f"\n*{name} sneaks in Rhea's room*")
                Rheascene1(name)
                if Rheapointtally>=0:
                    Rheascene2(name)
            else:
                print("\nThe door is locked")
        elif room_choice == "3":
            if Zarapointtally >= 0:
                print(f"\n*{name} sneaks in Zara's room*")
            else:
                print("\nThe door is locked")
        elif room_choice == "4":
            if Lunapointtally >= 0:
                print(f"\n*{name} sneaks in Luna's room*")
            else:
                print("\nThe door is locked")
        elif room_choice == "5":
            if Miapointtally >= 0:
                print(f"\n*{name} sneaks in Mia's room*")
            else:
                print("\nThe door is locked")
        else:
            print(f"\nNot an available room {name} you stupid fuck")

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
            print(f"\n{Rheapointtally}")
            break
        elif choice1 == "2":
            print(f"\n*{name} stands and creeps on Rhea, she notices you staring and mutters to herself* \n-What a wierdo.")
            Rheapointtally -= 2
            print(f"\n{Rheapointtally}")
            break
        elif choice1 == "3":
            print(f"\n*{name} runs up and hit Rhea across the head causing her to get a headache, she rubs her head in confusion* \n-WTH HELL IS WRONG WITH YOU? \n*She yells at you. {name} decides to apolegize, she forgives you but will not forget your actions*")
            Rheapointtally -= 3
            print(f"\n{Rheapointtally}")
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
            print(f"\nReally, what a coincedence thats my favorite too. *Time passes and {name} decides to leave her room*")
            Rheapointtally += 3
            print(f"\n{Rheapointtally}")
            hallway(username)
            break
        if choice2 == "2":
            print(f"\n*Rhea gives {name} a look of disgust, and asks you to leave her room*")
            Rheapointtally -= 5
            print(f"\n{Rheapointtally}")
            hallway(username)
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
                    print(f"\n{Rheapointtally}")
                    hallway(username)
                    break
                if choice3 == "2":
                    print(f"\n*{name} goes crazy and get sturdy on her ass, she smiles as you defeat her and blows {name} a kiss as you leave her room*")
                    Rheapointtally += 4
                    print(f"\n{Rheapointtally}")
                    hallway(username)
                    break
                if choice3 == "3":
                    print(f"\n*{name} start dancing matching her tempo creating a fun and flirty atmopshere, she kisses {name}'s cheek before you leave her room*")
                    print(f"\n{Rheapointtally}")
                    hallway(username)
                    break
                else: 
                     print("\nPlese enter one of the available numbers!")
            break
        else:
            print("\nPlese enter one of the available numbers!")    

hallo = intro(username) 
