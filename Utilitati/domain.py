def citireTranzactieUI(mesaj:str):
    '''
    citeste CORECT o tranzactie de la tastatura de tipul: data/suma/tip
    :param mesaj: mesajul de inceput
    :return: tranzactia corect citita de utilizator
    '''
    trz=input(mesaj)
    while not(trz.count("/")==2):
        print("Incorect")
        trz=input(mesaj)
    return trz
def citireInt(mesaj:str):
    while True:
        try:
            return int(input(mesaj))
        except ValueError:
            print("Valoare incorecta. Reincercati")

def citireTip(mesaj:str):
    tip=input(mesaj)
    while (tip!='-' and tip!='+'):
        print("Tip incorect")
        tip=input(mesaj)
    return tip

def getZi(cont:dict):
    return cont.get('zi')
def getSuma(cont:dict):
    return cont.get('suma')
def getTip(cont:dict):
    return cont.get('tip')

def setZi(cont:dict,zi:int):
    cont['zi']=zi
    return cont

def setSuma(cont:dict,suma:int):
    cont['suma']=suma
    return cont
def setTip(cont:dict,tip:str):
    cont['tip']=tip
    return cont
def afisareInt(numar:int,mesaj):
    print(mesaj)
    print(numar)

def afisareLista(cont:list,mesaj):
    print(mesaj)
    for i in cont:
        print(i, end=" ")
    print("\n")
def transferStrToNumber(text:str):
    try:
        return int(text)
    except ValueError:
        print("Textul nu este numar")
def copiereLista(sursa,destinatie):
    destinatie=[]
    for i in sursa:
        destinatie.append(i)
    return destinatie
def dupaSuma(trz1:list):
    return trz1["suma"]



