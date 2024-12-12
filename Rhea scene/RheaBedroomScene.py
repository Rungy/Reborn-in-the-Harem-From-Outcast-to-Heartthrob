Rheapointtally = 2
username = 1
def enterrhearoom (name):
    return f"{name} enter Rhea's room, you quickly scan the room and catch Rhea doing her morning routine."
    
    
Text1 = enterrhearoom (username)
print(Text1)
choice1 = input('''What do you do? 
        1. Join in 
        2. Stare 
        3. Smash''')
while True:
    if choice1 == "1":
        Rheapointtally += 2
        break
    elif choice1 == "2":
        Rheapointtally -= 2
        break
    elif choice1 == "3":
        Rheapointtally -= 3
        break
    else:
        print("Plese enter one of the available numbers!")
print(f"Rhea's point tally {Rheapointtally}")
