from Utilitati.domain import citireInt,afisareLista,copiereLista
from UIandFunctionalitati.business import  *

def meniu_Adunari_si_Stergeri(cont:list,undo):
    '''
    Meniul utilizatorului pentru functiile de adaugare si stergere
    :param cont: lista de tranzactii
    :return: cerintele respective
    '''

    while True:
        temp = []
        temp = copiereLista(cont, temp)
        undo.insert(0, temp)
        print("Alege una dintre urmatoarele cerinte: \n"
                          "1. Adaugare tranzactie noua \n"
                          "2. Actualizeaza o tranzactie existenta \n"
                          "3. Sterge tranzactiile dintr-o zi \n"
                          "4. Sterge tranzactiile dintr-o perioada anume \n"
                          "5. Sterge tranzactiile de un anumit tip \n"
                          "6. Revenire la meniul principal (urmeaza sa fie realizat in I3) \n")
        cerinta=citireInt("Introdu cerinta: ")
        match cerinta:
            case 1:
                cont=cerinta1_AdaugareTranzactie(cont)
                afisareLista(cont,"Contul meu este:")
            case 2:
                cont=cerinta2_ActualizareTranzactie(cont)
                afisareLista(cont,"Contul meu este:")
            case 3:
                cont=cerinta3_StergeTranzactieZi(cont)
                afisareLista(cont,"Contul meu este:")
            case 4:
                cont=cerinta4_StergeTranzactiePerioada(cont)
                afisareLista(cont,"Contul meu este:")
            case 5:
                cont=cerinta5_StergeTranzactiiTip(cont)
                afisareLista(cont,"Contul meu este:")
            case 6:
                meniuPrincipal(cont,undo)
            case _:
                print("Index incorect")
                undo.pop(0)

def meniu_Cautare(cont,undo):
    '''
    Functia principala care rezolva iteratia 1: Cautarea in contul curent a a numitor tyranzactii, in functie de cerinta
    :param cont:
    :return:-
    Modifica contul curent si afiseaza listele cerute, in functie de cerinta
    '''
    mesaj="Tranzactiile cerute sunt: "
    while True:
        temp = []
        temp = copiereLista(cont, temp)
        undo.insert(0, temp)
        print("Cauta in functie de:\n"
              "1. Suma \n"
              "2. Suma si perioada \n"
              "3. Tip \n"
              "4. Revenire la meniul principal (urmeaza in interatia 2) \n "
              )
        index = citireInt("Introdu cerinta: ")
        if index == 1:
            afisareLista(cautare1(cont), mesaj)
        elif index == 2:
            afisareLista(cautare2(cont), mesaj)
        elif index == 3:
            afisareLista(cautare3(cont), mesaj)
        elif index == 4:
            meniuPrincipal(cont, undo)
        else:
            print("Cerinta invalida. Reincercati")


def meniuRapoarte(cont,undo):
    '''
    Meniul pentru Rapoarte
    :param cont:
    :return: -
    Afiseaza listele sau sumele cerute, in functie de cerinta
    '''
    while True:
        print("Rapoarte: \n"
              "1. Suma totală a tranzacțiilor de un anumit tip \n"
              "2. Soldul contului la o dată specificată \n"
              "3. Tipărește toate tranzacțiile de un anumit tip ordonat după sumă \n"
              "4. Revenire la meniul principal \n")
        index=citireInt("Introduceti cerinta: ")
        match index:
            case 1:
                cerintaRaport1(cont)
            case 2:
                cerintaRaport2(cont)
            case 3:
                cerintaRaport3(cont)
            case 4:
                meniuPrincipal(cont,undo)
            case _:
                print("Index gresit. Reincercati! ")



def meniuFiltrari(cont,undo):
    '''
    Meniul pentru filtrari
    :param cont:  contul curent
    :return:
    Eliminea din contul curent tranzactii in functie de cerinta
    '''

    while True:
        temp = []
        temp = copiereLista(cont, temp)
        undo.insert(0, temp)
        print("Alegeti Filtrarile \n"
              "1. Elimină toate tranzacțiile de un anumit tip \n"
              "2. Elimină toate tranzacțiile mai mici decât o sumă dată care au tipul specificat \n"
              "3. Inapoi la meniu \n"
            )
        index = citireInt("Introdu cerinta: ")
        match index:
            case 1:
                cerintaFiltrare1(cont)
            case 2:
                cerintaFiltrare2(cont)
            case 3:
                meniuPrincipal(cont,undo)
            case _:
                print("Index incorect. Reincercati")
                undo.pop(0)

def meniuPrincipal(cont,undo):
    '''
    meniup principal. Inglobeaza toate functionalitatile problemei
    :param cont:
    :return:
    Aplica o functionalitate unui cont
    '''

    afisareLista(undo,"DA")
    while True:
        print("Contul Dumneavoastra Bancar \n"
              "1. Adaugari si Stergeri \n"
              "2. Cautari \n"
              "3. Rapoarte \n"
              "4. Filtrari \n"
              "5. Undo ultima operatie \n"
              "6. Exit \n ")
        index = citireInt("Introdu cerinta: ")
        match index:
            case 1:
                meniu_Adunari_si_Stergeri(cont,undo)
            case 2:
                meniu_Cautare(cont,undo)
            case 3:
                meniuRapoarte(cont,undo)
            case 4:
                meniuFiltrari(cont,undo)
            case 5:
                if undo == []:
                    print("Nu avem unde sa ne intoarcem! ")
                else:
                    undo.pop(0)
                    cont = undo[0]
                    afisareLista(undo, "Stiva:")
                    afisareLista(cont, "Contul")
            case 6:
                exit()


def meniuNou(cont,undo):
    '''
    meniu nou cu urmatoarele comenzi: Adauga o tranzactie, sterge o tranzactie, afiseaza suma tranzactiilor de un anumit tip
    :param cont:
    :param undo:
    :return:
    '''
    while True:
        comenzi=[]
        comenzi = input(">>> ")
        comenzi = comenzi.split("; ")
        #print(comenzi)
        for i in comenzi:
            com = i.split(" ")
            #print(com)
            match com[0]:
                case "adauga":
                    if com[1].count("/")==2:
                        trz = com[1].split("/")
                        trz = transferListaToDict(trz)
                        if not verifTranzactieValida(trz) or (
                                len(cont) != 0 and not verifAdaugareTranzactie(cont, trz)):
                            print("Tranzactie Incorecta. Reincercati")
                        else:
                            cont = adaugaTranzactie(cont, trz)
                    else:
                        print("Tranzactie Invalida")
                case "sterge":
                    a=transferStrToNumber(com[1])
                    if a!= None:
                        cont=stergereTranzacitePerZi(cont,a)
                    else:
                        print("Zi Invalida. Reincercati")
                case "raportTip":
                    tip=com[1]
                    if not verifTip(tip):
                        print("Tip invalid!")
                    else:
                        suma=raportSumaTip(cont,tip)
                        afisareInt(suma,"Suma mea este")
                case _:
                    print("Comanda invalida!")
        afisareLista(cont, "Lista mea este: ")
def run():
    cont=[]
    undo=[]
    #meniuPrincipal(cont, undo)
    meniuNou(cont, undo)


