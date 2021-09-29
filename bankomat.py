import datetime

# Print huvudmeny


def mainMeny():
    print('---------------------')
    print('------HUVUDMENY------')
    print('1. Skapa konto')
    print('2. Administrera konto')
    print('3. Avsluta')

# Skapar nytt konto ifall det inte finns i listan alreadyExistingAccount


def createAccount():

    account = input('Ange kontonummer->')

    if account.isdigit():

        if account not in alreadyExistingAccount:
            alreadyExistingAccount.append(account)
            moneyOnAccount.append(0)
            print('\nKontot tillagt\n')
        else:
            print('\nKontot finns redan\n')

    else:
        print('\nEndast siffror!\n')


# Loggar in på angivna kontot ifall det finns i alreadyExistingAccount
def logInAccount():

    logIn = input('Ange kontonummer->')
    if logIn in alreadyExistingAccount:
        accountMeny(logIn)
    else:
        print('\nKontot finns inte..\n')

# Tar ut pengar från alreadyExistingAccount ifall kontot har det beloppet & skapar/lägger till i kvitto dokumentet


def moneyTakeOut(BankAccount):
    index = alreadyExistingAccount.index(BankAccount)
    belopp = input('Ange belopp att ta ut->')
    if belopp.isdigit() and int(belopp) > 0:
        if int(belopp) <= moneyOnAccount[index]:
            print(f'\nTar ut {belopp}kr')
            moneyOnAccount[index] -= int(belopp)
            kvitto = open(f'{BankAccount}.txt', 'a')
            kvitto.write(
                f'{time.strftime("%x") + " " + time.strftime("%X")} - utdrag : {belopp}kr\n')
            kvitto.close()
        else:
            print(
                f'\nBelopp finns inte att ta ut, saldo är: {moneyOnAccount[index]}kr ')

    else:
        print('\nEndast siffror!\n')

# Sätter in pengar i moneyOnAccount som har samma index som alreadyExistingAccount & skapar/lägger till i kvitto dokumentet


def moneyPutIn(BankAccount):
    index = alreadyExistingAccount.index(BankAccount)
    belopp = input('Ange belopp att sätta in->')
    if belopp.isdigit() and int(belopp) > 0:
        print(f'\nSätter in {belopp}kr')
        moneyOnAccount[index] += int(belopp)
        kvitto = open(f'{BankAccount}.txt', 'a')
        kvitto.write(
            f'{time.strftime("%x") + " " + time.strftime("%X")} - insättning : {belopp}kr\n')
        kvitto.close()

    else:
        print('Endast siffror!')

# Läser kvittodokumentet som tillhör angivna kontonummer & visar nuvarande saldo


def moneySaldo(BankAccount):
    index = alreadyExistingAccount.index(BankAccount)
    kvitto = open(f'{BankAccount}.txt', 'r')
    print('\nTidigare transaktioner:')
    print(kvitto.read())
    kvitto.close()
    print(f'\nDitt saldo är : {moneyOnAccount[index]}kr \n')


# Kontomeny loop
def accountMeny(logIn):
    loop = True
    while loop:
        print(f'\n------KONTOMENY------| konto:{logIn}')
        print('1. Ta ut pengar')
        print('2. Sätt in pengar')
        print('3. Visa saldo')
        print('4. Logga ut')
        changeAlt = input('Ange menyval->')
        if changeAlt.isdigit():
            if int(changeAlt) == 1:
                moneyTakeOut(logIn)
            elif int(changeAlt) == 2:
                moneyPutIn(logIn)
            elif int(changeAlt) == 3:
                moneySaldo(logIn)
            elif int(changeAlt) == 4:
                loop = False
            else:
                print('\nMenyval finns inte\n')
        else:
            print('\nEndast siffror\n')
    print('\nKontot utloggat.\n')


# Huvudmeny loop
alreadyExistingAccount = []
moneyOnAccount = []
time = datetime.datetime.now()
active = True
while active:
    mainMeny()
    choise = input('Ange menyval->')
    if choise.isdigit():
        if int(choise) == 1:
            createAccount()
        elif int(choise) == 2:
            logInAccount()
        elif int(choise) == 3:
            active = False
        else:
            print('\nMenyval finns inte..\n')
    else:
        print('\nEndast siffror\n')

"""Det som inte funkar är ifall man stänger ner programet
och startar upp det igen och skapar samma banknummer en gång till.
saldot/kvittot kommer visa tidigare utdrag/insättningar men programmet
skapar ett nytt konto men inga pengar i.
 - MEN jag tänker att skulle det vara en riktig bankomat så skulle man inte 
stänga av den? dock dålig säkerhet ifall tex strömavbrott skulle inträffa.."""
