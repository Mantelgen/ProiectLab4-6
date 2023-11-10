from Utilitati.domain import *
from TesteSiValidari.validation import  *
from Utilitati.infrastructure import *
def citireTranzactie():
    '''
    Citirea valida sub forma de lista a unei tranzactii introduse ca string
    :return:
    '''
    rez=[]
    tranzactie = citireTranzactieUI("Introdu Tranzactia: ")
    tranzactie=tranzactie.split("/")
    tranzactie=transferListaToDict(tranzactie)
    while not verifTranzactieValida(tranzactie):
        print("Tranzactie invalida:")
        tranzactie = citireTranzactieUI("Introdu Tranzactia: ")
        tranzactie = tranzactie.split("/")
        tranzactie = transferListaToDict(tranzactie)
    return tranzactie
def citireDateActualizare(cont:list):
    '''
    citirea indexului si datelor unei tranzactii pe care vrem sa o modificam
    :param cont: lista cu tranzactii
    :return: tranzactia noua cat si indexul tranzactiei pe care o inlocuim
    '''
    index=citireInt("Introduceti indexul tranzactiei pe care vreti sa o modificati: ")
    while index>=len(cont):
        print("Tranzactia nu exista. Reincercati")
        index=citireInt("Introduceti indexul tranzactiei pe care vreti sa o modificati:")
    trz = citireTranzactie()
    trz=transferStrToInt(trz)
    return trz,index

def cerinta1_AdaugareTranzactie(cont:list):
    '''
    Rezolva prima cerinta de la adaugare
    :param cont: lista de tranzactii
    :return: lista in care s-a adaugat o noua tranzactie valida
    '''

    trz = citireTranzactie()
    trz = transferStrToInt(trz)
    return adaugaTranzactie(cont,trz)

def cerinta2_ActualizareTranzactie(cont:list):
    '''
    Rezolvam cerinta de actualizare a unei tranzactii
    :param cont: lista de tranzactii
    :return: lista in care s-a modificat o tranzactie de pe un anumit index
    '''
    rez=[]
    rez,index=citireDateActualizare(cont)
    return actualizeazaTranzactie(cont,rez,index)

def cerinta3_StergeTranzactieZi(cont:list):
    '''
    Stergerea tranzactiilor dintr-o zi
    :param cont: lista de tranzactii
    :return: lista fara tranzactiile din ziua introdusa de la tastatura
    '''
    zi=citireInt("Citeste ziua din care vrei sa stergi")
    return stergereTranzacitePerZi(cont,zi)

def cerinta4_StergeTranzactiePerioada(cont:list):
    '''
    Stergerea tranzactiilor dintr-o perioada
    :param cont: lista de tranzactii
    :return: lista fara tranzactiile dintr-o anumita perioada
    '''
    ziStart=citireInt("Citeste ziua de start: ")
    ziStop=citireInt("Citeste ziua de stop: ")
    return stergeTranzactiiPerioada(cont,ziStart,ziStop)

def cerinta5_StergeTranzactiiTip(cont:list):
    '''
    Stergerea tranzactiilor de un anumit tip
    :param cont: lista de tranzactii
    :return: lista fara tranzactiile de un anumit tip
    '''
    tip=input("Introdu tipul tranzactiei: ")
    while not verifTip(tip):
        print("Input incorect. Reincercati")
        tip=input("Introdu tipul tranzactiei: ")
    return stergeTranzactiiTip(cont,tip)

def cautare1(cont:list):
    '''
    realizeaza prima cautare a tranzactiilor mai mari decat o suma citita de la tastatura
    :param cont: contul de tranzactii in caqre facem cautarea
    :return: lista de tranzactii cerute
    '''
    suma=citireInt("Introdu suma: ")
    return cautaTranzactieSuma(cont,suma)
def cautare2(cont:list):
    '''
        realizeaza prima cautare a tranzactiilor mai mari decat o suma si o zi , citite de la tastatura
        :param cont: contul de tranzactii in caqre facem cautarea
        :return: lista de tranzactii cerute
        '''
    suma=citireInt("Introdu suma: ")
    zi=citireInt("Introdu ziua: ")
    return cautaTranzactieSumaSiZi(cont,suma,zi)
def cautare3(cont:list):
    '''
        realizeaza prima cautare a tranzactiilor de un anumit tip citit de la tastatura
        :param cont: contul de tranzactii in caqre facem cautarea
        :return: lista de tranzactii cerute
        '''
    tip=citireTip("Introdu tipul de tranzactie(+/-): ")
    return cautaTranzactieTip(cont,tip)
def cerintaFiltrare1(cont:list):
    '''
    prima cerinta de filtrare dupa un anumit tip
    :param cont: tcontul curent
    :return: contul modificat dupa eliminare
    '''
    tip=citireTip("Introduceti tipul pe care vreti sa il filtrati: ")
    cont = filtrareTip(cont, tip)
    afisareLista(cont,"Lista modificata este: ")
    return cont

def cerintaFiltrare2(cont:list):
    '''
    a doua cerinta de filtrare, dupa o suma si un tip
    :param cont: contul curent
    :return: contul modificat dupa eliminare
    '''
    suma = citireInt("Introduceti suma: ")
    tip=citireTip("Introduceti tipul: ")
    cont=filtrareMaiMicCaOSuma(cont,suma,tip)
    afisareLista(cont,"Lista modificata este: ")
    return cont
def cerintaRaport1(cont:list):
    '''
    primul raport: suma tranzactiilor de un tip
    :param cont:
    :return:
    afiseaza suma tranzactiilor de tip
    '''
    tip=citireTip("Introduceti tipul: ")
    suma=raportSumaTip(cont,tip)
    afisareInt(suma,"Suma ceruta este: ")

def cerintaRaport2(cont:list):
    '''
    al doilea raport: soldul la o anumita data
    :param cont: contul curent
    :return: -
    afiseaza soldul la o anumita data
    '''
    zi=citireInt("Introdu ziua la care vrei sa aflii soldul:")
    sold= raportSoldData(cont,zi)
    afisareInt(sold,"Soldul la ziua data este: ")

def cerintaRaport3(cont:list):
    '''
    rezolvam raportul 3: tranzactiile de un anumit tip, ordonata dupa suma
    :param cont:
    :return:
    tranzactiile de tipul dat, ordonate crescator dupa suma
    '''
    tip=citireTip("Introduceti tipul dorit:")
    rez=raportDupaSumaSiTip(cont,tip)
    afisareLista(rez,"Tranzactiile mele sunt: ")

def undoOperatie(cont,undo):

    return cont,undo