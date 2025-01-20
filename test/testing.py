import time
username = input("Name? ")

Finnpointtally = 4
Rheapointtally = 2
Zarapointtally = 0
Lunapointtally = 0 
Miapointtally = 0 


def intro(name):
    print("You a 50 year old man. Currently watching and dacing heavily to the new poopkai musik.\n Unkown to you, you are a very heavy man, weighting at 300 pounds")
    input("Enter to continue")
    print(f"\n{name}-kun LOOVVESSS THIS!!!, *suddenly {name}-kuns ankel twists and he falls to his death*")
    input("Enter to continue")
    print("  ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓███████▓▒░▒▓████████▓▒░")
    time.sleep(0.07)
    print(" ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░")
    time.sleep(0.07)
    print(" ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░")
    time.sleep(0.07)
    print(" ░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓██████▓▒░")
    time.sleep(0.07)
    print(" ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░")
    time.sleep(0.07)
    print(" ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░")
    time.sleep(0.07)
    print(" ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░")

    input("\nPress Enter..")    
    hallway(name)

def hallway(name):
    print(f"\n{name} enters the hallway a bit stimulated")
    while Finnpointtally <= 23 and Rheapointtally <= 23 and Zarapointtally <= 23 and Lunapointtally <= 23 and Miapointtally <= 23:
        room_choice = input("""\nWhat room do you want to enter? 
(following rooms are:)
1-Finn
2-Rhea
3-Zara
4-Luna
5-Mia
(Write the number of the chosen room!): """)
        if room_choice == "1":
            if Finnpointtally >= -19:
                print(f"\n*{name} sneaks in Finn's room*")
                input("\nPress Enter..")
                Finn(name)
            else:
                print("\nThe door is locked")
                input("\nPress Enter..")
        elif room_choice == "2":
            if Rheapointtally >= 0:
                print(f"\n*{name} sneaks in Rhea's room*")
                input("\nPress Enter..")
                Rheascene1(name)
                if Rheapointtally>=0:
                    input("\nPress Enter..")
                    Rheascene2(name)
                else:
                    print("\nThe door is locked")
                    input("\nPress Enter..")
            else:
                print("\nThe door is locked")
                input("\nPress Enter..")
        elif room_choice == "3":
            if Zarapointtally >= 0:
                print(f"\n*{name} knocks on Zara' door but no one answeres*")
                input("\nPress Enter..")
            else:
                print("\nThe door is locked")
                input("\nPress Enter..")
        elif room_choice == "4":
            if Lunapointtally >= 0:
                print(f"\n*{name} knocks on Luna' door but no one answeres*")
                input("\nPress Enter..")
            else:
                print("\nThe door is locked")
                input("\nPress Enter..")
        elif room_choice == "5":
            if Miapointtally >= 0:
                print(f"\n*{name} knocks on Mia's door but no one answeres*")
                input("\nPress Enter..")
            else:
                print("\nThe door is locked")
                input("\nPress Enter..")
        else:
            print(f"\nNot an available room {name} you stupid fuck")
            input("\nPress Enter..")
    print("wait... is that a light?")
    input("")
    print("""
▄▄▄█████▓ ██░ ██ ▓█████    ▓█████  ███▄    █ ▓█████▄ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒███   ▓██  ▀█ ██▒░██   █▌
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░▒████▒▒██░   ▓██░░▒████▓ 
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ 
    ░     ▒ ░▒░ ░ ░ ░  ░    ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒ 
  ░       ░  ░░ ░   ░         ░      ░   ░ ░  ░ ░  ░ 
          ░  ░  ░   ░  ░      ░  ░         ░    ░    
                                              ░      
""")

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
            input("\nPress Enter..")
            break
        elif choice1 == "2":
            print(f"\n*{name} stands and creeps on Rhea, she notices you staring and mutters to herself* \n-What a wierdo.")
            Rheapointtally -= 2
            print(f"\n{Rheapointtally}")
            input("\nPress Enter..")
            break
        elif choice1 == "3":
            print(f"\n*{name} runs up and hit Rhea across the head causing her to get a headache, she rubs her head in confusion* \n-WTH HELL IS WRONG WITH YOU? \n*She yells at you. {name} decides to apolegize, she forgives you but will not forget your actions*")
            Rheapointtally -= 3
            print(f"\n{Rheapointtally}")
            input("\nPress Enter..")
            break
        else:
            print("\nPlese enter one of the available numbers!")
            input("\nPress Enter..")

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
            input("\nPress Enter..")
            hallway(name)
            break
        if choice2 == "2":
            print(f"\n*Rhea gives {name} a look of disgust, and asks you to leave her room*")
            Rheapointtally -= 5
            print(f"\n{Rheapointtally}")
            input("\nPress Enter..")
            hallway(name)
            break
        if choice2 == "3":
            print(f"\nReally i didnt take you for a dancer. I challange you to a dance battle!")
            input("\nPress Enter..")
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
                    input("\nPress Enter..")
                    hallway(name)
                    break
                if choice3 == "2":
                    print(f"\n*{name} goes crazy and get sturdy on her ass, she smiles as you defeat her and blows {name} a kiss as you leave her room*")
                    Rheapointtally += 4
                    print(f"\n{Rheapointtally}")
                    input("\nPress Enter..")
                    hallway(name)
                    break
                if choice3 == "3":
                    print(f"\n*{name} start dancing matching her tempo creating a fun and flirty atmopshere, she kisses {name}'s cheek before you leave her room*")
                    print(f"\n{Rheapointtally}")
                    input("\nPress Enter..")
                    hallway(name)
                    break
                else: 
                     print("\nPlese enter one of the available numbers!")
                     input("\nPress Enter..")
            break
        else:
            print("\nPlese enter one of the available numbers!")
            input("\nPress Enter..")  

def Finn(name):
    global Finnpointtally
    print(f"\nFinn runs at {name} at full speed overwhelming him with love")
    input("\nPress Enter..")
    
    while True:
        while True:
            choice1=input(f"""\n{name} is greeted with the following choices:
1-Pet him
2-Pounce on him
3-Push him away

""")
            if choice1 == "1":
                print("\n*Han lutar sig närmare med ett lekfullt leende, kisar nöjt med ögonen och suckar mjukt* \nÅh, fortsätt så där, du vet verkligen hur man behandlar en stjärna!")
                Finnpointtally += 2
                input("\nPress Enter..")
                break
            elif choice1 == "2":
                print("\n*Han tjuter till av glädje när du pouncar på honom, fångar dig i en dramatisk omfamning och skrattar varmt* \nOoooh! Vilken entré! Jag älskar det  \nGör om det, gör det igen!")
                Finnpointtally += 3
                input("\nPress Enter..")
                break
            elif choice1 == "3":
                print("\n*Han kippar efter andan, tar ett dramatiskt steg bakåt och lägger handen över hjärtat som om du just förolämpat hans själ* \nVA?! Hur vågar du?! Jag är ömtålig, du kan ju ha förstört min aura!")
                Finnpointtally -= 10
                input("\nPress Enter..")
                hallway(name)
                break
            else:
                print("\nstupid is there anything other than 1 2 3 here?")
                input("\nPress Enter..")
    
        if Finnpointtally >= 6:
            print(f"\nFinn's love towards {name} is {Finnpointtally} points")
            input("\nPress Enter..")
            break
        elif 5 <= Finnpointtally <= 0:
            print(f"\nFinn is neutral towards {name}")
            input("\nPress Enter..")
            break
        else:
            print(f"\nFinn's dislike towards {name} is {Finnpointtally} points")
            input("\nPress Enter..")
            break
    
    print("\nYou spend a little time in finns room")
    input("\nPress enter to continue")
    print("\n*Han ler lekfullt, gör en dramatisk bugning*\n Hur må jag servera dig, min stjärna?")
    
    while True:
        choice2=input(f"""\n{name} is very lost between these choices
1-Vissa min tumma och säga sug på den
2-Jag hellre servera dig älskling
""")
        if choice2 == "1":
            print("\n*Han höjer ett ögonbryn, ler förföriskt och tar försiktigt din finger mellan läpparna* \nMmm… farligt frestande")
            Finnpointtally += 4
            input("\nPress Enter..")
            break
        elif choice2 == "2":
            print("\n*Han kippar efter andan, lägger en hand dramatiskt över hjärtat* \nUrsäkta?! Jag är den som serverar glamour här!")
            Finnpointtally -= 5
            input("\nPress Enter..")
            break
        else:
            print(f"\n{name} they said you were the king of dumbtowm")
            input("\nPress Enter..")

    if 23 >= Finnpointtally >= 8:
        print(f"\n*Han ler varmt, lutar sig bekvämt tillbaka och sträcker ut en hand mot dig* \nMmm, det här var mysigt. Kom snart tillbaka, okej? Jag gillar att ha dig här")
        input("\nPress Enter..")
    elif 7 >= Finnpointtally >= 0:
        print(f"\n*Han ser på dig med en sned blick, spelar med en ring på fingret och suckar* \nHmpf… jag antar att det kunde ha varit värre. Men du har en lång väg att gå, älskling")
        input("\nPress Enter..")
    elif Finnpointtally <= -1:
        print(f"\n*Han vänder demonstrativt ryggen till, armarna i kors, och suckar dramatiskt* \nUgh! Jag trodde du förstod mig, men tydligen inte. Gå. Innan jag blir ännu mer besviken")
        input("\nPress Enter..")
    elif Finnpointtally >= 24:
        print("*Han stirrar på dig ett ögonblick, som om han just insett något otroligt*")
        input("\nPress Enter..")
        print("*Sedan spricker han upp i ett leende, ett äkta, mjukt leende som är annorlunda från hans vanliga lekfulla smil*")
        input("\nPress Enter..")
        print("Så det är så här det känns… att verkligen hitta någon...")
        input("\nPress Enter..")
        print("*Han tar din hand, smeker den försiktigt med tummen och ser dig djupt i ögonen*")
        input("\nPress Enter..")
        print("Ingen mer lek, ingen mer fasad. Bara du och jag… för alltid.")

hallo = intro(username) 
