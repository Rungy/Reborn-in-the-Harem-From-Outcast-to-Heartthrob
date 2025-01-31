#Importerar time modulen för våra animationer
import time 

#Sparar användarens namn för dialoger
username = input("Vad heter du? ") 

#Start poäng för karaktär relationer
Finnpointtally = 4
Rheapointtally = 4
Zarapointtally = 0
Lunapointtally = 0 
Miapointtally = 0 

#Variabel för om användare vill ha tutorial guide
tot = False

#Variabler som gör så att man bara kan prata med karaktärerna en gång vid Bedroomscene
Rheatalk = False
Finntalk = False
Zaratalk = False
Lunatalk = False
Miatalk = False

#Funktion om man vill ha guide eller inte
def guide(name):
    global tot
    while True:
        answere = input("\nVill du ha en handledning? Svara med ja eller nej ")
        if answere == "Ja":
            tot = True
            break
        elif answere == "ja":
            tot = True
            break
        elif answere == "yes":
            tot = True
            break
        elif answere == "Yes":
            tot = True
            break
        elif answere == "Nej":
            tot = False
            break
        elif answere == "nej":
            tot = False
            break
        elif answere == "no":
            tot = False
            break
        elif answere == "No":
            tot = False
            break
        else:
            print("\nDu svarade inte tydligt.")
    while True:
        if tot == True:
            print("\nAllt du behöver göra är att svara rätt på frågor... alla handlingar har konsekvenser!")
            input("\nTryck på Enter..")
            print("\nDu måste göra vissa rum flera gånger för att få det sanna slutet av spelet, annars slutar spelet aldrig.")
            input("\nTryck på Enter..")
            print("\nSom du kanske är medveten om var detta ett gruppprojekt, så vissa rum är lite underutvecklade.")
            input("\nTryck på Enter..")
            print("\nVi rekommenderar starkt Rhea och Finn, men alla rum är lite spännande.")

            tot = False
            #Start animation
        else:
            input("\nTryck på Enter..")
            print("██████╗ ███████╗██████╗  ██████╗ ██████╗ ███╗   ██╗    ██╗███╗   ██╗    ██╗  ██╗ █████╗ ██████╗ ███████╗███╗   ███╗")
            time.sleep(0.07)
            print("██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗████╗  ██║    ██║████╗  ██║    ██║  ██║██╔══██╗██╔══██╗██╔════╝████╗ ████║")
            time.sleep(0.07)
            print("██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝██╔██╗ ██║    ██║██╔██╗ ██║    ███████║███████║██████╔╝█████╗  ██╔████╔██║")
            time.sleep(0.07)
            print("██╔══██╗██╔══╝  ██╔══██╗██║   ██║██╔══██╗██║╚██╗██║    ██║██║╚██╗██║    ██╔══██║██╔══██║██╔══██╗██╔══╝  ██║╚██╔╝██║")
            time.sleep(0.07)
            print("██║  ██║███████╗██████╔╝╚██████╔╝██║  ██║██║ ╚████║    ██║██║ ╚████║    ██║  ██║██║  ██║██║  ██║███████╗██║ ╚═╝ ██║")
            time.sleep(0.07)
            print("╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝")
            input("\nTryck på Enter..")
            intro(name)
            break
#Funktion till introduktion av spelet
def intro(name):
    print("Du är en 50-årig man. Just nu tittar och dansar du intensivt till den nya poopkai-musiken.\n Ovetandes om att du är en väldigt tung man, väger du 300 pund.")
    input("\nTryck på Enter..")
    print(f"\n{name}-kun ÄLSKAR DETTA!!!, *plötsligt vrider {name}-kun sin fot och faller till sin död*")
    input("\nTryck på Enter..")
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

    input("\nTryck på Enter..") 
    bedroomscenewakeup(name)
#Funktion till bedroomscene
def bedroomscenewakeup (name):
    #Använder alla "talk" variabler för att bara kunna prata med karaktärerna en gång
    global Rheatalk
    global Finntalk
    global Zaratalk
    global Lunatalk
    global Miatalk
    print(f"\n*{name} känner hur livet långsamt försvinner tills det blir totalt mörker*")
    input("\nTryck på Enter..") 
    print(f"\nMen {name}s medvetande kvarstår och han känner en underlig känsla där nere medan han väntar i vad som känns som en evighet i tystnad.")
    input("\nTryck på Enter..") 
    print(f"\n*Plötsligt hör {name} en röst och mörkret försvinner*")
    input("\nTryck på Enter..") 
    print("\nHerrn, vakna herrn!")
    input("\nTryck på Enter..") 
    print(f"\n{name} börjar långsamt öppna sina ögon och ser 5 främmande figurer med vackra kurvor.")
    input("\nTryck på Enter..") 
    print("\nDen första figuren har isblå ögon som genomborrar sin omgivning med skarp intelligens. Hennes tjocka, mörka hår faller elegant runt hennes ansikte och förstärker hennes kraftfulla utstrålning. Hennes drag är skarpa, med höga kindben och en stark käklinje. Hennes kropp är smidig och ståtlig, med en rak och självsäker hållning.")
    input("\nTryck på Enter..") 
    print("\nDen andra figuren har livliga, ljusgröna ögon som gnistrar av nyfikenhet och lekfullhet. Hans mjuka, vågiga hår är ljusbrunt och faller nonchalant runt ansiktet. Hans drag är androgyna och harmoniska, med höga kindben och en uttrycksfull mun. Hans kropp är smidig och graciös, med en avslappnad men självsäker hållning.")
    input("\nTryck på Enter..") 
    print("\nDen tredje figuren har djupvioletta ögon som tycks rymma hela universum, alltid drömska men skarpa. Hennes långa, mörkblå hår faller i mjuka vågor runt hennes bleka ansikte. Hennes drag är fina och eteriska, med höga kindben och en smal, elegant näsa. Hennes kropp är smal och smidig, med en lugn och nästan svävande närvaro.")
    input("\nTryck på Enter..") 
    print("\nDen fjärde figuren har mjuka, ljusbruna ögon som glittrar av värme och drömmar. Hennes långa, gyllene hår faller i lösa vågor runt hennes ansikte. Hennes drag är mjuka och harmoniska, med rosiga kinder och ett varmt leende. Hennes kropp är smal och graciös, med en avslappnad och nästan svävande närvaro.")
    input("\nTryck på Enter..") 
    print("\nDen femte figuren har skarpa, grå ögon som blixtrar av intelligens och attityd. Hennes korta, svartfärgade hår är rufsigt och nonchalant stylat. Hennes drag är distinkta, med höga kindben och en markerad käklinje. Hennes kropp är smidig och stark, med en självsäker och avslappnad hållning.")
    input("\nTryck på Enter..") 

    while True:
        introduction = input(f"""\nWho do you decide to talk to first?
1. Figur 1
2. Figur 2
3. Figur 3
4. Figur 4
5. Figur 5
6. Säg till dom att lämna rummet
""")
        input("\nTryck på Enter..")
        #Snabb och kort introduktion av karaktärer
        if introduction == "1":
            if Rheatalk == False:
                print(f"\nVem är du, var e jag? *Frågar {name}*")
                input("\nTryck på Enter..")
                print(f"\nVar it orolig, du är säker här. *Svarar figuren*")
                input("\nTryck på Enter..")
                print(f"\nMitt namn är Rhea, vi hittade dig medvetslös på marken och valde att ta in dig i vårat hem")
                input("\nTryck på Enter..")
                print(f"\nTack... *{name} svarar svagt*")
                input("\nTryck på Enter..")
                Rheatalk = True
            else:
                print("\nDu har redan pratat med denna person")

            
        elif introduction == "2":
            if Finntalk == False:
                print(f"\nVem är du då? *Frågar {name}*")
                input("\nTryck på Enter..")
                print("\nMitt namn är Finn sötnos. *Säger figuren flörtsamt och blåser en puss*")
                input("\nTryck på Enter..")
                Finntalk = True
            else: 
                print("\nDu har redan pratat med denna person")
        elif introduction == "3":
            if Zaratalk == False:
                print(f"\noch vem är du? *Frågar {name}*")
                input("\nTryck på Enter..")
                print("\nJag heter Zara. *muttrar figuren utan att kolla upp från sin bok*")
                input("\nTryck på Enter..")
                Zaratalk = True
            else:
                print("\nDu har redan pratat med denna person")
        elif introduction == "4":
            if Lunatalk == False:
                print(f"\ndu då? *Frågar {name}*")
                input("\nTryck på Enter..")
                print("\nNamnet är Luna, trevligt att råkas hjärtat *Säger figuren medans hon leker med sitt långa mörka hår*")
                input("\nTryck på Enter..")
                Lunatalk = True
            else:
                print("\nDu har redan pratat med denna person")
        elif introduction == "5":
            if Miatalk == False:
                print(f"\n Ditt namn? *Frågar {name}*")
                input("\nTryck på Enter..")
                print(f"\nMia, säger det bara en gång. *Säger figuren medans hon suckar*")
                input("\nTryck på Enter..")
                Miatalk = True
            else:
                print("\nDu har redan pratat med denna person")
        elif introduction == "6":
            print(f"Kan jag få lite ensam tid? *Frågar {name}*")
            input("\nTryck på Enter..")
            print(f"*\nFigurenerna lyssnar på dig och lämnar ditt rum*")
            input("\nTryck på Enter..")
            print(f"\n*Tid har passerat och du väljer att utforska ditt nya hem*")
            input("\nTryck på Enter..")
            print(f"\n{name} går in i hallen, lite stimulerad")
            hallway(name)
            break
#Funktion för Hallway 
def hallway(name):
    #Om "point tally variabler"
    while Finnpointtally <= 23 and Rheapointtally <= 23 and Zarapointtally <= 23 and Lunapointtally <= 23 and Miapointtally <= 23:
        #Val av rum
        room_choice = input("""\nVilket rum vill du gå in i? 
(följande rum finns:)
1-Finn
2-Rhea
3-Zara
4-Luna
5-Mia
(Skriv numret på det valda rummet!): """)
        if room_choice == "1":
            #Om Variabler faller under 19 blir användare utlåst av rum
            if Finnpointtally >= -19:
                print(f"\n*{name} smyger in i Finns rum*")
                input("\nTryck på Enter..")
                Finn(name)
            else:
                print("\nDörren är låst")
                input("\nTryck på Enter..")
        elif room_choice == "2":
            #Om Variabler faller under 0 blir användare utlåst av rum
            if Rheapointtally >= 0:
                print(f"\n*{name} smyger in i Rheas rum*")
                input("\nTryck på Enter..")
                Rheascene1(name)
            else:
                print("\nDörren är låst")
                input("\nTryck på Enter..")
        elif room_choice == "3":
            #Om Variabler faller under 0 blir användare utlåst av rum
            if Zarapointtally >= 0:
                print(f"\n*{name} smyger in i Zaras rum*")
                input("\nTryck på Enter..")
                zara_room(name)
                if Zarapointtally >= 0:
                    zara_join(name)
                    if Zarapointtally >= 0:
                        zara_movie(name)
                    else:
                        print("\nDet verkar som att du blev utkastad")
                        input("\nTryck på Enter..")
                else:
                    print("\nDet verkar som att du blev utkastad")
                    input("\nTryck på Enter..")
            else:
                print("\nDörren är låst")
                input("\nTryck på Enter..")

        elif room_choice == "4":
            #Om Variabler faller under 0 blir användare utlåst av rum
            if Lunapointtally >= 0:
                print(f"\n*{name} knackar på Lunas dörr men ingen svarar*")
                input("\nTryck på Enter..")
            else:
                print("\nDörren är låst")
                input("\nTryck på Enter..")
        elif room_choice == "5":
            if Miapointtally >= 0:
                print(f"\n*{name} smyger in i Mias rum*")
                input("\nTryck på Enter..")
                mia_room(name)
            else:
                print("\nDörren är låst")
                input("\nTryck på Enter..")
        else:
            print(f"\nInte ett tillgängligt rum, {name}, din dumma jävel")
    #Om karaktär poängvariable stiger över eller lika med 24 så avslutas spelet
    print("\nVänta...Vad är de..för ljus")
    input("\nTryck på Enter..")
    print("▄▄▄█████▓ ██░ ██ ▓█████    ▓█████  ███▄    █ ▓█████▄ ")
    time.sleep(0.07)
    print("▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌")
    time.sleep(0.07)
    print("▒ ▓██░ ▒░▒██▀▀██░▒███      ▒███   ▓██  ▀█ ██▒░██   █▌")
    time.sleep(0.07)
    print("░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌")
    time.sleep(0.07)
    print("  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░▒████▒▒██░   ▓██░░▒████▓ ")
    time.sleep(0.07)
    print("  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ ")
    time.sleep(0.07)
    print("    ░     ▒ ░▒░ ░ ░ ░  ░    ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒ ")
    time.sleep(0.07)
    print("  ░       ░  ░░ ░   ░         ░      ░   ░ ░  ░ ░  ░ ")
    time.sleep(0.07)
    print("          ░  ░  ░   ░  ░      ░  ░         ░    ░    ")
    time.sleep(0.07)
    print("                                              ░      ")
    input("\nTryck på Enter..")
    print("Oh father... forgive me..")
    
#Rheascene funktion
def Rheascene1(name):
    global Rheapointtally
    print(f"\n*{name} går in i Rheas rum, du snabbt scannar rummet och ser Rhea göra sin yoga morgonsrutin.*")
    
    while True:
        choice1 = input('''\nVad gör du? 
1. Gå med 
2. Stirra 
3. Slå till
''')
        if choice1 == "1":
            print(f"\n*{name} frågar om hen får gå med i Rheas yogapass, hon nickar och du går med*")
            Rheapointtally += 4 
            print(f"\n{Rheapointtally}")
            input("\nTryck på Enter..")
            break
        elif choice1 == "2":
            print(f"\n*{name} står och smygtittar på Rhea, hon märker att du stirrar och muttrar för sig själv* \n-Vilken konstig typ.")
            Rheapointtally -= 2
            print(f"\n{Rheapointtally}")
            input("\nTryck på Enter..")
            break
        elif choice1 == "3":
            print(f"\n*{name} springer fram och slår Rhea över huvudet, vilket ger henne huvudvärk, hon gnuggar sitt huvud i förvirring* \n-VAD FAN ÄR FEL PÅ DIG? \n*Hon skriker på dig. {name} bestämmer sig för att be om ursäkt, hon förlåter dig men kommer inte glömma dina handlingar*")
            Rheapointtally -= 3
            print(f"\n{Rheapointtally}")
            input("\nTryck på Enter..")
            break
        else:
            print("\nVänligen ange ett av de tillgängliga numren!")
            input("\nTryck på Enter..")
    
    print(f"\nSå vad är din favoritställning i yoga, {name}? *Rhea frågar och försöker starta en konversation*")
    
    while True:
        choice2 = input('''\nVad är ditt svar?
1. Nedåthund 
2. Doggystyle
3. Jag föredrar dans
''')

        if choice2 == "1":
            print(f"\nVerkligen, vilket sammanträffande, det är också min favorit. *Tiden går och {name} bestämmer sig för att lämna hennes rum*")
            Rheapointtally += 3
            print(f"\n{Rheapointtally}")
            input("\nTryck på Enter..")
            break
        if choice2 == "2":
            print(f"\n*Rhea ger {name} en avskyvärd blick*")
            Rheapointtally -= 5
            print(f"\n{Rheapointtally}")
            input("\nTryck på Enter..")
            break
        if choice2 == "3":
            print(f"\nVerkligen, jag tog dig inte för en dansare. Jag utmanar dig till en dansstrid!")
            input("\nTryck på Enter..")
            Rheapointtally += 4
            #En gömd väg
            while True:
                choice3 = input(f'''\nRhea utmanar {name} till en dansstrid, hon börjar flossa, vad är ditt nästa drag?
        1. Förlora med flit
        2. Vinn och gör henne generad
        3. Ha en rolig strid
        ''')
                if choice3 == "1":
                    print(f"\n*Rhea märker att {name} håller tillbaka och blir besviken*")
                    Rheapointtally -= 2
                    print(f"\nRheas kärlek nivå för dig är{Rheapointtally}")
                    input("\nTryck på Enter..")
                    break
                if choice3 == "2":
                    print(f"\n*{name} går loss och dansar hårt, hon ler när du besegrar henne och blåser {name} en kyss*")
                    Rheapointtally += 4
                    print(f"\nRheas kärlek nivå för dig är {Rheapointtally}")
                    input("\nTryck på Enter..")
                    break
                if choice3 == "3":
                    Rheapointtally += 5
                    print(f"\n*{name} börjar dansa och matchar hennes tempo, skapar en rolig och flörtig atmosfär*")
                    print(f"\nRheas kärlek nivå för dig är {Rheapointtally}")
                    input("\nTryck på Enter..")
                    break
                else: 
                     print("\nVänligen ange ett av de tillgängliga numren!")
                     input("\nTryck på Enter..")
            break
        else:
            print("\nVänligen ange ett av de tillgängliga numren!")
            input("\nTryck på Enter..")
    #Rhea slutscener
    if 23 >= Rheapointtally >= 8:
        print(f"\n*Hon lutar sig tillbaka med ett mjukt leende, sträcker ut en hand och snuddar vid din fingertopp som om hon inte riktigt vill släppa taget* \nDu vet… jag trivs verkligen med dig. Det känns tryggt, på något sätt. Så, lova mig att du kommer tillbaka snart, okej?")
        input("\nTryck på Enter..")
    elif 7 >= Rheapointtally >= 0:
        print(f"\n*Hon lutar huvudet åt sidan, studerar dig ett ögonblick med en eftertänksam min medan hon långsamt trummar med fingrarna mot bordet* \nTja… det kunde ha varit värre. Men du har en lång väg kvar att gå, älskling. Frågan är… har du vad som krävs?")
        input("\nTryck på Enter..")
    elif Rheapointtally <= -1:
        print(f"\n*Hon stelnar till, spänner käken och drar armarna om sig själv som för att skapa distans mellan er* \nÄr det verkligen så här du ser på mig? Jag… jag trodde att du förstod. Men tydligen hade jag fel. Gå. Innan jag bryr mig ännu mindre.")
        input("\nTryck på Enter..")
    elif Rheapointtally >= 24:
        print("*Hon fryser mitt i en rörelse, som om något inom henne precis fallit på plats.*")
        input("\nTryck på Enter..")
        print("*Långsamt andas hon ut, och när hon ser upp på dig är hennes blick annorlunda – klar, öppen, som om alla fasader har fallit bort.*")
        input("\nTryck på Enter..")
        print("Så… det är så här det känns? Att inte behöva låtsas?")
        input("\nTryck på Enter..")
        print("*Hon rör sig närmare, lyfter en hand och låter försiktigt fingertopparna spåra en linje över din kind, som om hon försöker memorera ögonblicket.*")
        input("\nTryck på Enter..")
        print("Inga fler masker. Ingen mer osäkerhet. Bara vi… tillsammans, på riktigt.")
        input("\nTryck på Enter..")    
#Finn funktion
def Finn(name):
    global Finnpointtally
    print(f"\nFinn springer mot {name} i full fart och överväldigar honom med kärlek")
    input("\nTryck på Enter..")
    
    while True:
        while True:
            choice1=input(f"""\n{name} möts av följande val:
1-Klappa honom
2-Hoppa på honom
3-Pusha bort honom

""")
            if choice1 == "1":
                print("\n*Han lutar sig närmare med ett lekfullt leende, kisar nöjt med ögonen och suckar mjukt* \nÅh, fortsätt så där, du vet verkligen hur man behandlar en stjärna!")
                Finnpointtally += 2
                input("\nTryck på Enter..")
                break
            elif choice1 == "2":
                print("\n*Han tjuter till av glädje när du hoppar på honom, fångar dig i en dramatisk omfamning och skrattar varmt* \nOoooh! Vilken entré! Jag älskar det  \nGör om det, gör det igen!")
                Finnpointtally += 3
                input("\nTryck på Enter..")
                break
            elif choice1 == "3":
                print("\n*Han kippar efter andan, tar ett dramatiskt steg bakåt och lägger handen över hjärtat som om du just förolämpat hans själ* \nVA?! Hur vågar du?! Jag är ömtålig, du kan ju ha förstört min aura!")
                Finnpointtally -= 10
                input("\nTryck på Enter..")
                hallway(name)
                break
            else:
                print("\nÄr du dum eller? Finns det något annat än 1, 2, 3 här?")
                input("\nTryck på Enter..")
    
        if Finnpointtally >= 6:
            print(f"\nFinns kärlek mot {name} är {Finnpointtally} poäng")
            input("\nTryck på Enter..")
            break
        elif 5 <= Finnpointtally <= 0:
            print(f"\nFinn är neutral mot {name}")
            input("\nTryck på Enter..")
            break
        else:
            print(f"\nFinns ogillande mot {name} är {Finnpointtally} poäng")
            input("\nTryck på Enter..")
            break
    
    print("\nDu tillbringar lite tid i Finns rum")
    input("\nTryck på Enter för att fortsätta")
    print("\n*Han ler lekfullt, gör en dramatisk bugning*\n Hur kan jag stå till tjänst, min stjärna?")
    
    while True:
        choice2 = input(f"""\n{name} är väldigt förvirrad mellan dessa val:
1-Visa min tumme och säg sug på den
2-Jag föredrar att servera dig, älskling
""")
        if choice2 == "1":
            print("\n*Han höjer ett ögonbryn, ler förföriskt och tar försiktigt ditt finger mellan läpparna* \nMmm… farligt frestande")
            Finnpointtally += 4
            input("\nTryck på Enter..")
            break
        elif choice2 == "2":
            print("\n*Han kippar efter andan, lägger en hand dramatiskt över hjärtat* \nUrsäkta?! Jag är den som serverar glamour här!")
            Finnpointtally -= 5
            input("\nTryck på Enter..")
            break
        else:
            print(f"\n{name}, de sa att du var kungen av dumhet")
            input("\nTryck på Enter..")
    #Finn slutscener
    if 23 >= Finnpointtally >= 8:
        print(f"\n*Han ler varmt, lutar sig bekvämt tillbaka och sträcker ut en hand mot dig* \nMmm, det här var mysigt. Kom snart tillbaka, okej? Jag gillar att ha dig här")
        input("\nTryck på Enter..")    
    elif 7 >= Finnpointtally >= 0:
        print(f"\n*Han ser på dig med en sned blick, spelar med en ring på fingret och suckar* \nHmpf… jag antar att det kunde ha varit värre. Men du har en lång väg att gå, älskling")
        input("\nTryck på Enter..")
    elif Finnpointtally <= -1:
        print(f"\n*Han vänder demonstrativt ryggen till, armarna i kors, och suckar dramatiskt* \nUgh! Jag trodde du förstod mig, men tydligen inte. Gå. Innan jag blir ännu mer besviken")
        input("\nTryck på Enter..")
    elif Finnpointtally >= 24:
        print("*Han stirrar på dig ett ögonblick, som om han just insett något otroligt*")
        input("\nTryck på Enter..")
        print("*Sedan spricker han upp i ett leende, ett äkta, mjukt leende som är annorlunda från hans vanliga lekfulla smil*")
        input("\nTryck på Enter..")
        print("Så det är så här det känns… att verkligen hitta någon...")
        input("\nTryck på Enter..")
        print("*Han tar din hand, smeker den försiktigt med tummen och ser dig djupt i ögonen*")
        input("\nTryck på Enter..")
        print("Ingen mer lek, ingen mer fasad. Bara du och jag… för alltid.")
#Zaras funktion
def zara_room(name):
    global Zarapointtally
    print(f"\n*{name} går in i rummet, Zara tittar upp och hälsar på dig.*")

    while True:
        choice = input('''\nHur hälsar du på henne?
1. Kram
2. Nicka med huvudet
3. Skaka hand
''')
        if choice == "1":
            print(f"\n*{name} ger Zara en kram, hon ler varmt.*")
            Zarapointtally += 3
            break
        elif choice == "2":
            print(f"\n*{name} nickar mot Zara, hon nickar tillbaka med ett artigt leende.*")
            Zarapointtally += 2
            break
        elif choice == "3":
            print(f"\n*{name} skakar hand med Zara, hon ser lite förvirrad ut men går med på det.*")
            Zarapointtally -= 2
            break
        else:
            print("\nVänligen ange ett av de tillgängliga numren!")

def zara_join(name):
    global Zarapointtally
    print(f"\n*Zara sätter sig ner och bjuder in {name} att sitta med henne.*")

    while True:
        choice = input('''\nVad gör du?
1. Var likgiltig
2. Visa intresse
''')
        if choice == "1":
            print(f"\n*{name} beter sig likgiltigt, Zara känner sig förolämpad och ber dig lämna rummet.*")
            print("Du blev utkastad från rummet.")
            Zarapointtally -= 5
            break
        elif choice == "2":
            print(f"\n*{name} visar intresse för vad Zara gör. Hon ler och föreslår att ni ska titta på en film tillsammans.*")
            zara_movie(name)
            break
        else:
            print("\nVänligen ange ett av de tillgängliga numren!")
#En till funktion för Zara
def zara_movie(name):
    global Zarapointtally
    print(f"\n*{name} och Zara tittar på en film tillsammans, skapar en varm och vänlig atmosfär.*")
    print(f"\n*Zara verkar imponerad av ditt sällskap.*")
    Zarapointtally += 3
    if Zarapointtally > 5:
        print("\nGrattis! Du vann Zaras kärlek.")
    elif Zarapointtally > 0:
        print("\nDu gjorde ett positivt intryck på Zara.")
    else:
        print("\nDu kanske behöver jobba på dina sociala färdigheter!")
#Funktion för Mia (Kan ej få ett lyckligt slut :/ )
def mia_room(name):
    global Miapointtally
    print(f"\n*{name} går in i rummet, Mia tittar upp.*")

    while True:
        choice = input('''\nHur hälsar du på henne?
1. Hälsa artigt
2. Hälsa aggressivt
''')
        if choice == "1":
            print(f"\n*{name} hälsar artigt på Mia, men hon svarar inte.*")
            Miapointtally += 0
            break
        elif choice == "2":
            print(f"\n*{name} hälsar aggressivt på Mia, hon rynkar pannan och slår plötsligt ut dig.*")
            Miapointtally += 2
            print("\nDu får +2 poäng men blir utkastad.")
            break
        else:
            print("\nVänligen ange ett av de tillgängliga numren!")
    
    if Miapointtally > 1:
        print("\nGrattis! Du fick några poäng, men till ett pris.")
    elif Miapointtally == 0:
        print("\nZara är likgiltig inför din närvaro.")
    else:
        print("\nDu kanske behöver tänka om din strategi!")

guide(username)