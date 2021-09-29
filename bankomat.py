import datetime

# Print huvudmeny


def mainMeny():
    print('---------------------')
    print('------HUVUDMENY------')
    print('1. Skapa konto')
    print('2. Administrera konto')
    print('3. Avsluta')

# Skapar nytt konto ifall det inte finns i listan alreadyExistingAccount


def createAccount(accountDictionary):

    account = input('Ange kontonummer->')
    try:
        f = open(f'{account}.txt', 'r')
        f.read()
        f.close()
        print('\nKontot finns redan\n')
    
    except:

        if account.isdigit() and account not in accountDictionary:
            accountDictionary[account] = 0
            print('\nKontot tillagt\n')
            f = open(f'{account}.txt', 'w')
            f.write(
                f'{time.strftime("%x") + " " + time.strftime("%X")} - Account created.\n')
            f.close()
    
        else:
            print('\nEndast siffror!\n')
        


# Loggar in på angivna kontot ifall det finns i alreadyExistingAccount
def logInAccount(accountDictionary):

    logIn = input('Ange kontonummer->')
    if logIn in accountDictionary:
        accountMeny(logIn, accountDictionary)
    else:
        print('\nKontot finns inte..\n')

# Tar ut pengar från alreadyExistingAccount ifall kontot har det beloppet & skapar/lägger till i kvitto dokumentet


def moneyTakeOut(bankAccount, accountDictionary):
    amount = input('Ange belopp att ta ut->')
    if amount.isdigit() and int(amount) > 0:
        if int(amount) <= accountDictionary[bankAccount]:
            print(f'\nTar ut {amount}kr')
            accountDictionary[bankAccount] -= int(amount)
            #kvitto = open(f'{bankAccount}.txt', 'a')
            #kvitto.write(
            #    f'{time.strftime("%x") + " " + time.strftime("%X")} - utdrag : {amount}kr\n')
            #kvitto.close()
        else:
            print(
                f'\nBelopp finns inte att ta ut, saldo är: {accountDictionary[bankAccount]}kr ')

    else:
        print('\nEndast siffror!\n')

# Sätter in pengar i moneyOnAccount som har samma index som alreadyExistingAccount & skapar/lägger till i kvitto dokumentet


def moneyPutIn(bankAccount, accountDictionary):
    amount = input('Ange belopp att sätta in->')
    if amount.isdigit() and int(amount) > 0:
        print(f'\nSätter in {amount}kr')
        accountDictionary[bankAccount] += int(amount)
        #kvitto = open(f'{BankAccount}.txt', 'a')
        #kvitto.write(
        #    f'{time.strftime("%x") + " " + time.strftime("%X")} - insättning : {belopp}kr\n')
        #kvitto.close()
    elif amount[0] == "-":
        print("Tar inte emot negativa belopp")
    else:
        print('Endast siffror!')

# Läser kvittodokumentet som tillhör angivna kontonummer & visar nuvarande saldo


def moneySaldo(bankAccount, accountDictionary):
    #kvitto = open(f'{BankAccount}.txt', 'r')
    #print('\nTidigare transaktioner:')
    #print(kvitto.read())
    #kvitto.close()
    print(f'\nDitt saldo är : {accountDictionary[bankAccount]}kr \n')


# Kontomeny loop
def accountMeny(bankAccount, accountDictionary):
    loop = True
    while loop:
        print(f'\n------KONTOMENY------| konto:{bankAccount}')
        print('1. Ta ut pengar')
        print('2. Sätt in pengar')
        print('3. Visa saldo')
        print('4. Logga ut')
        changeAlt = input('Ange menyval->')
        if changeAlt.isdigit():
            if int(changeAlt) == 1:
                moneyTakeOut(bankAccount, accountDictionary)
            elif int(changeAlt) == 2:
                moneyPutIn(bankAccount, accountDictionary)
            elif int(changeAlt) == 3:
                moneySaldo(bankAccount, accountDictionary)
            elif int(changeAlt) == 4:
                loop = False
            else:
                print('\nMenyval finns inte\n')
        else:
            print('\nEndast siffror\n')
    print('\nKontot utloggat.\n')


# Huvudmeny loop

accountDictionary = {}
time = datetime.datetime.now()
active = True
while active:
    mainMeny()
    choise = input('Ange menyval->')
    if choise.isdigit():
        if int(choise) == 1:
            createAccount(accountDictionary)
        elif int(choise) == 2:
            logInAccount(accountDictionary)
        elif int(choise) == 3:
            active = False
        else:
            print('\nMenyval finns inte..\n')
    else:
        print('\nEndast siffror\n')


