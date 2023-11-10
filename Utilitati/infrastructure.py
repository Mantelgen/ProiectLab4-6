from Utilitati.domain import dupaSuma,getSuma,getZi,getTip,setSuma,setTip,setZi
def adaugaTranzactie(cont:list,trz:dict):
    '''
    aduagarea unei tranzactii in cont a unei tranzactii valide
    :param cont: lista cu tranzactii
    :param trz: tranzactia dorita
    :return: contul cu noua tranzactie introdusa
    '''
    cont.insert(0,trz)
    return cont

def transferListaToDict(lista:list):
    nou={}
    nou = {}
    nou["zi"] = lista[0]
    nou["suma"] = lista[1]
    nou["tip"] = lista[2]
    return nou
def actualizeazaTranzactie(cont:list,trz:dict,index):
    '''
    actualizarea unei tranzactii existente cu o tranzactie valita
    :param cont: lista de tranzactii
    :param trz: tranzactia pe care vrem sa o introducem
    :param index: indexul tranzactiei pe care vrem sa o inlocuim
    :return: lista de tranzactii modificata
    '''
    cont[index]=trz
    return cont

def stergereTranzacitePerZi(listaTranzactii:list,zi:int):
    '''
    Stergerea tranzactiilor dintr-o zi speficiata
    :param listaTranzactii: lista de tranzactii din cont
    :param zi: ziua a caror tranzactii vrem sa le eliminam
    :return: contul modificat
    '''
    i=0
    deSters=[]
    if listaTranzactii == []:
        print("Nu avem ce sterge")
    else:
        while i<len(listaTranzactii) and int(getZi(listaTranzactii[i]))!=zi:
            i += 1
    while i<len(listaTranzactii) and int(getZi(listaTranzactii[i]))==zi:
        deSters.append(listaTranzactii[i])
        listaTranzactii.pop(i)
    return listaTranzactii

def stergeTranzactiiPerioada(listaTranzactii:list,ziStart:int,ziStop:int):
    '''
    sterge anumite tranzactii dintr-o anumita perioada din luna
    :param listaTranzactii: lista de tranzactii din cont
    :param ziStart: ziua de inceput a perioadei
    :param ziStop: ziua de stop a perioadei
    :return: lista modificata, lista cu ce am sters(folosita in undo) si indexul de stop al secventei de unde am sters elementele
    '''
    i = 0
    if listaTranzactii == []:
        print("Nu avem ce sterge")
    else:
        while i < len(listaTranzactii) and int(getZi(listaTranzactii[i])) > ziStop:
            i += 1
        while i < len(listaTranzactii) and int(getZi(listaTranzactii[i])) >= ziStart and int(getZi(listaTranzactii[i])) <= ziStop:
            listaTranzactii.pop(i)
    return listaTranzactii

def stergeTranzactiiTip(listaTranzactii:list,tip:str):
    '''
    Sterge o tranzactiile de un anumit tip (-/+)
    :param listaTranzactii: lista de tranzactii
    :param tip: tipul tranzactiei
    :return: lista modificata
    '''
    i = 0
    deSters = []
    if listaTranzactii == []:
        print("Nu avem ce sterge")
    else:
        while i < len(listaTranzactii) and getTip(listaTranzactii[i])!=tip:
            i += 1
        while i < len(listaTranzactii) and getTip(listaTranzactii[i]) == tip:
            listaTranzactii.pop(i)
    return (listaTranzactii)
def transferStrToInt(tranzactie:dict):
    '''
    Transforma o lista de stringuri intr-o lista de tipul [int, int,str]
    :param tranzactie: tranzactia pe care vreau sa o transform
    :return: tranzactia scrisa sub forma specificata
    '''
    rez= {}
    rez["zi"]=int(getZi(tranzactie))
    rez["suma"]=int(getSuma(tranzactie))
    rez["tip"]=getTip(tranzactie)
    return rez

def adaugaTranzactie(cont:list,trz:dict):
    '''
    aduagarea unei tranzactii in cont a unei tranzactii valide
    :param cont: lista cu tranzactii
    :param trz: tranzactia dorita
    :return: contul cu noua tranzactie introdusa
    '''
    cont.insert(0, trz)
    return cont

def cautaTranzactieSuma(cont:list,suma:int):
    '''
    printeaza tranzactiile care au o anumita suma
    :param cont: contul cu tranzactiile
    :param suma: suma pe care o cautam
    :return:-
    printeaza tranzactia in consola
    '''
    cautat=[]
    for i in cont:
        if getSuma(i)>suma:
            cautat.append(i)
    return cautat

def cautaTranzactieSumaSiZi(cont:list,suma:int,zi:int):
    '''
    Cauta in contul curent tranzactia mai mare decat o anumita suma si o anumita zi, date ca parametrii
    :param cont: contul cu tranzactii
    :param suma: suma dorita
    :param zi: ziua dorita
    :return: lista nou cu tranzactiile specificate
    '''
    cautat=[]
    for i in cont:
        if getZi(i)>zi and getSuma(i)>suma:
            cautat.append(i)
    return cautat

def cautaTranzactieTip(cont:list,tip:str):
    '''
    Cauta in contul curent tranzactiile de un anumit tip, trimis ca parametru de intrare
    :param cont: lista de tranzactii
    :param tip: tipul cerut
    :return: lista cu tranzactiile cerute
    '''
    cautat=[]
    for i in cont:
        if getTip(i)==tip:
            cautat.append(i)
    return cautat

def filtrareTip(cont:dict,tip:str):
    '''
    elimina tranzactiile de un anumit Tip
    :param cont: lista cu tranzactii
    :param tip: tipul de tranzactie pe care vrem sa o stergem
    :return: lista de tranzactii, din care s-au elminiat tranzactiile de un anumit tip
    '''
    deSters=[]
    i=0
    while i<len(cont):
        if getTip(cont[i])==tip:
            cont.pop(i)
        else:
            i+=1

    return cont

def filtrareMaiMicCaOSuma(cont:dict,suma:int,tip:int):
    '''
    filtreaza din cont tranzactiile de un anumit tip, cu suma mai mica decat o suma data
    :param cont: contul curent
    :param suma: suma ceruta
    :param tip: tipul specificat
    :return: lista de tranzactii, din care s-au eliminat tranzactiile de un anumit tip cu o suma mai mica decat o suma data
    '''
    deSters = []
    i = 0
    while i < len(cont):
        if getSuma(cont[i])<suma and getTip(cont[i])== tip:
            cont.pop(i)
        else:
            i += 1

    return cont
    pass

def raportSumaTip(cont:list,tip:int):
    '''
    tipareste suma totala a tranzactiilor de un naumit tip
    :param cont: contul curent
    :param tip: tipul tranzactiilor
    :return: suma tranzactiilor de tipul precizat
    '''
    suma = 0
    for tranzactie in cont:
        if getTip(tranzactie)==tip:
            suma+=int(getSuma(tranzactie))
    return suma

def raportSoldData(cont:list,zi:int):
    '''
    tipareste suma din contul curent la o anumita data
    :param cont: contul curent
    :param zi: data specificata
    :return: suma la tata specificata
    '''
    nrTranzactie=0
    sold=0
    while nrTranzactie<len(cont) and getZi(cont[nrTranzactie])>zi:
        nrTranzactie+=1
    while nrTranzactie<len(cont):
        if getTip(cont[nrTranzactie])=='-':
            sold-=getSuma(cont[nrTranzactie])
        else:
            sold+=getSuma(cont[nrTranzactie])
        nrTranzactie += 1

    return sold

def raportDupaSumaSiTip(cont:list,tip:str):
    '''
    tipareste tranzactiile de tipul precizat, in ordine crescatoare in functie de suma
    :param cont: contul curent
    :param tip: tipul de tranzactie
    :return: tranzactiile de tipul specificat, sortate crescator dupa suma
    '''
    rez=[]
    for tranzactie in cont:
        if getTip(tranzactie)==tip:
            rez.append(tranzactie)
    rez.sort(key=dupaSuma)
    return rez