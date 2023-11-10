from Utilitati.domain import getTip,getZi,getSuma,setTip,setSuma,setZi
def verifData(data:str):
    '''
    verifica daca stringul reprezinta sau nu o data valida
    :param data: data introdusa de utilizator
    :return: True daca stringul reprezinta o data valida, false in caz contrar
    '''
    return data.isdigit() and int(data)>=1 and int(data) <=31

def verifTip(tip:str):
    '''
    verifica daca stringul introdus este un tip de tranzactie(+/-) sau nu
    :param tip: tipul introdus de utilizator
    :return: True daca stringul reprezinta un tip valid, false in caz contrar
    '''
    return tip=='-' or tip == '+'

def verifTranzactieValida(tranzactie):
    '''
    verifica daca stringul introdus este o tranzactie valida sau nu
    :param tranzactie:tranzactie introdusa de utilizator, validata anterior in alta functie de citire, scrisa sub forma de lista
    :return: True daca lista introdus este o tranzactie valida, false in caz contrar
    '''
    return verifData(getZi(tranzactie)) and getSuma(tranzactie).isdigit() and verifTip(getTip(tranzactie))

def verifAdaugareTranzactie(cont:list,tranzacite):
    '''
    Verifica daca pot adauga o anumita tranzactie in lista
    :param cont: lista cu tranzactii
    :param tranzacite: tranzactia pe care vreau sa o introduc
    :return: True daca ziua tranzactiei noi este mai mare sau egala decat ultima tranzactie folosita, false in caz contrar
    '''
    return int(getZi(tranzacite))>=int(getZi(cont[0]))