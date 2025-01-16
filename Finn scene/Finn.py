Finnpointtally = 4
username = "Arsalan"
def Finngreeting(name):
    global Finnpointtally
    print(f"\nFinn runs at {name} at full speed overwhelming him with love")
    
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
                break
            elif choice1 == "2":
                print("\n*Han tjuter till av glädje när du pouncar på honom, fångar dig i en dramatisk omfamning och skrattar varmt* \nOoooh! Vilken entré! Jag älskar det  \nGör om det, gör det igen!")
                Finnpointtally += 3
                break
            elif choice1 == "3":
                print("\n*Han kippar efter andan, tar ett dramatiskt steg bakåt och lägger handen över hjärtat som om du just förolämpat hans själ* \nVA?! Hur vågar du?! Jag är ömtålig, du kan ju ha förstört min aura!")
                Finnpointtally -= 10
                break
            else:
                print("\nstupid is there anything other than 1 2 3 here?")
    
        if Finnpointtally >= 6:
            print(f"\nFinn's love towards {name} is {Finnpointtally} points")
            break
        elif 5 <= Finnpointtally <= 0:
            print(f"\nFinn is neutral towards {name}")
            break
        else:
            print(f"\nFinn's dislike towards {name} is {Finnpointtally} points")
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
            break
        elif choice2 == "2":
            print("\n*Han kippar efter andan, lägger en hand dramatiskt över hjärtat* \nUrsäkta?! Jag är den som serverar glamour här!")
            Finnpointtally -= 5
            break
        else:
            print(f"\n{name} they said you were the king of dumbtowm")

    if 23 >= Finnpointtally >= 8:
        print(f"\n*Han ler varmt, lutar sig bekvämt tillbaka och sträcker ut en hand mot dig* \nMmm, det här var mysigt. Kom snart tillbaka, okej? Jag gillar att ha dig här")
    elif 7 >= Finnpointtally >= 0:
        print(f"\n*Han ser på dig med en sned blick, spelar med en ring på fingret och suckar* \nHmpf… jag antar att det kunde ha varit värre. Men du har en lång väg att gå, älskling")
    elif Finnpointtally <= -1:
        print(f"\n*Han vänder demonstrativt ryggen till, armarna i kors, och suckar dramatiskt* \nUgh! Jag trodde du förstod mig, men tydligen inte. Gå. Innan jag blir ännu mer besviken")
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


Finngreeting(username)