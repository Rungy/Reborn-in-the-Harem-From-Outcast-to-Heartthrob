username = "Arsalan"
Rheatalk = False
Finntalk = False
Zaratalk = False
Lunatalk = False
Miatalk = False
def bedroomscenewakeup (name):
    global Rheatalk
    global Finntalk
    global Zaratalk
    global Lunatalk
    global Miatalk
    print(f"\n*{name} feels their life slowly fading until it's total darkness")
    input("\nPress Enter..")
    print(f"\nBut {name} concioussnes remains and he feels an odd sensation down there as he waits for what feels like an eternity in slience.")
    input("\nPress Enter..")
    print(f"\n*Then suddenly {name} hears a voice and the darkness is no more*")
    input("\nPress Enter..")
    print("\nMister wake up mister!")
    input("\nPress Enter..")
    print(f"\n{name} slowly starts to open their eyes, {name} sees 5 foreign figures with nice curves.")
    input("\nPress Enter..")
    print("\nDen första figuren har isblå ögon som genomborrar sin omgivning med skarp intelligens. Hennes tjocka, mörka hår faller elegant runt hennes ansikte och förstärker hennes kraftfulla utstrålning. Hennes drag är skarpa, med höga kindben och en stark käklinje. Hennes kropp är smidig och ståtlig, med en rak och självsäker hållning.")
    input("\nPress Enter..")
    print("\nDen andra figuren  har livliga, ljusgröna ögon som gnistrar av nyfikenhet och lekfullhet. Hans mjuka, vågiga hår är ljusbrunt och faller nonchalant runt ansiktet. Hans drag är androgyna och harmoniska, med höga kindben och en uttrycksfull mun. Hans kropp är smidig och graciös, med en avslappnad men självsäker hållning. ")
    input("\nPress Enter..")
    print("\nDen Tredje figuren har djupvioletta ögon som tycks rymma hela universum, alltid drömska men skarpa. Hennes långa, mörkblå hår faller i mjuka vågor runt hennes bleka ansikte. Hennes drag är fina och eteriska, med höga kindben och en smal, elegant näsa. Hennes kropp är smal och smidig, med en lugn och nästan svävande närvaro.")
    input("\nPress Enter..")
    print("\nhar mjuka, ljusbruna ögon som glittrar av värme och drömmar. Hennes långa, gyllene hår faller i lösa vågor runt hennes ansikte. Hennes drag är mjuka och harmoniska, med rosiga kinder och ett varmt leende. Hennes kropp är smal och graciös, med en avslappnad och nästan svävande närvaro.")
    input("\nPress Enter..")
    print("\nhar skarpa, grå ögon som blixtrar av intelligens och attityd. Hennes korta, svartfärgade hår är rufsigt och nonchalant stylat. Hennes drag är distinkta, med höga kindben och en markerad käklinje. Hennes kropp är smidig och stark, med en självsäker och avslappnad hållning.")
    input("\nPress Enter..")

    while True:
        introduction = input(f"""\nWho do you decide to talk to first?
1. Figur 1
2. Figur 2
3. Figur 3
4. Figur 4
5. Figur 5
6. Säg till dom att lämna rummet
""")
        input("\nPress Enter..")
        if introduction == "1":
            if Rheatalk == False:
                print(f"\nVem är du, var e jag? *Frågar {name}*")
                input("\nPress Enter..")
                print(f"\nVar it orolig, du är säker här. *Svarar figuren*")
                input("\nPress Enter..")
                print(f"\nMitt namn är Rhea, vi hittade dig medvetslös på marken och valde att ta in dig i vårat hem")
                input("\nPress Enter..")
                print(f"\nTack... *{name} svarar svagt*")
                input("\nPress Enter..")
                Rheatalk = True
            else:
                print("\nDu har redan pratat med denna person")

            
        elif introduction == "2":
            if Finntalk == False:
                print(f"\nVem är du då? *Frågar {name}*")
                input("\nPress Enter..")
                print("\nMitt namn är Finn sötnos. *Säger figuren flörtsamt och blåser en puss*")
                input("\nPress Enter..")
                Finntalk = True
            else: 
                print("\nDu har redan pratat med denna person")
        elif introduction == "3":
            if Zaratalk == False:
                print(f"\noch vem är du? *Frågar {name}*")
                input("\nPress Enter..")
                print("\nJag heter Zara. *muttrar figuren utan att kolla upp från sin bok*")
                input("\nPress Enter..")
                Zaratalk = True
            else:
                print("\nDu har redan pratat med denna person")
        elif introduction == "4":
            if Lunatalk == False:
                print(f"\ndu då? *Frågar {name}*")
                input("\nPress Enter..")
                print("\nNamnet är Luna, trevligt att råkas hjärtat *Säger figuren medans hon leker med sitt långa mörka hår*")
                input("\nPress Enter..")
                Lunatalk = True
            else:
                print("\nDu har redan pratat med denna person")
        elif introduction == "5":
            if Miatalk == False:
                print(f"\n Ditt namn? *Frågar {name}*")
                input("\nPress Enter..")
                print(f"Mia, säger det bara en gång. *Säger figuren medans hon suckar*")
                input("\nPress Enter..")
                Miatalk = True
            else:
                print("\nDu har redan pratat med denna person")
        elif introduction == "6":
            print(f"Kan jag få lite ensam tid? *Frågar {name}*")
            input("\nPress Enter..")
            print(f"*Figurenerna lyssnar på dig och lämnar ditt rum*")
            input("\nPress Enter..")
            break
bedroomscenewakeup(username)

