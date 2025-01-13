Rheapointtally = 2
username = "Arsalan"
def Rheascene1 (name):
    global Rheapointtally
    print(f"*{name} enters Rhea's room, you quickly scan the room and catch Rhea doing her morning routine.*")
   
    while True:
        choice1 = input('''What do you do? 
1. Join in 
2. Stare 
3. Smash
''')
        if choice1 == "1":
            print(f"{name} \n*You ask to join Rhea's yoga session, she nods and you join in*")
            Rheapointtally += 2
            break
        elif choice1 == "2":
            print(f"\n*{name} stands and creeps on Rhea, she notices you staring and mutters to herself* \n-What a wierdo.")
            Rheapointtally -= 2
            break
        elif choice1 == "3":
            print(f"\n*You run up and hit Rhea across the head causing her to get a headache, she rubs her head in confusion* \n-WTH HELL IS WRONG WITH YOU? \n*She yells at you. {name} decides to apolegize, she forgives you but will not forget your actions*")
            Rheapointtally -= 3
            break
        else:
            print("\nPlese enter one of the available numbers!")

def Rheascene2 (name):
    global Rheapointtally
    print(f"So whats your favorite position in yoga? *Rhea asks trying to strike conversation*")

    while True:
        choice2 = input('''Whats your response?
1. Downward dog 
2. Doggystyle
3. I prefer dancing
''')
        
Rheascene1(username)
print(f"Rhea's point tally {Rheapointtally}")
