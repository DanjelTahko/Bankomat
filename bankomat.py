import datetime

# Print huvudmeny


def mainMeny():
    print('---------------------')
    print('------HUVUDMENY------')
    print('1. Skapa konto')
    print('2. Administrera konto')
    print('3. Avsluta')

# Skapar nytt konto ifall det inte redan finns en fil av samma kontonummer eller om det finns i dictionary


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
            #Transaktions fil
            f_create = open(f'{account}.txt', 'w')
            f_create.write(
                f'{time.strftime("%x") + " " + time.strftime("%X")} - Account created.\n')
            f_create.close()
            #Saldo fil
            f_saldo = open(f'{account}Saldo.txt', 'w')
            f_saldo.write(f'{accountDictionary[account]}')
            f_saldo.close()
    
        else:
            print('\nEndast siffror!\n')

#Kollar så att kontofilerna finns tidigare        
def accountExists(logIn):
    try:
        #Kollar så det finns ett konto
        f = open(f'{logIn}.txt', 'r')
        f.read()
        f.close()
        # Återställer saldo
        f_saldo = open(f'{logIn}Saldo.txt', 'r')
        accountDictionary[logIn] = int(f_saldo.read())
        f_saldo.close()
        #Öppnar menyn
        return True

    except:
        return False


# Loggar in på angivna kontot ifall det finns i alreadyExistingAccount
def logInAccount(accountDictionary):

    logIn = input('Ange kontonummer->')
    #Funktion som returnerar True om kontot finns
    existingAccount = accountExists(logIn)
    if existingAccount:
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
            #Fyller på transaktion
            f_withdraw = open(f'{bankAccount}.txt', 'a')
            f_withdraw.write(
                f'{time.strftime("%x") + " " + time.strftime("%X")} - utdrag : {amount}kr\n')
            f_withdraw.close()
            #Saldo fil
            f_saldo = open(f'{bankAccount}Saldo.txt', 'w')
            f_saldo.write(f'{accountDictionary[bankAccount]}')
            f_saldo.close()
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
        #Fyller på transaktion
        f_deposit = open(f'{bankAccount}.txt', 'a')
        f_deposit.write(
            f'{time.strftime("%x") + " " + time.strftime("%X")} - insättning : {amount}kr\n')
        f_deposit.close()
        #Saldo fil
        f_saldo = open(f'{bankAccount}Saldo.txt', 'w')
        f_saldo.write(f'{accountDictionary[bankAccount]}')
        f_saldo.close()
    elif amount[0] == "-":
        print("Tar inte emot negativa belopp")
    else:
        print('Endast siffror!')

# Läser kvittodokumentet som tillhör angivna kontonummer & visar nuvarande saldo


def moneySaldo(bankAccount, accountDictionary):
    
    f_transactions = open(f'{bankAccount}.txt', 'r')
    print('\nTidigare transaktioner:')
    print(f_transactions.read())
    f_transactions.close()
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


