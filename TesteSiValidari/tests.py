from TesteSiValidari.validation import *
from Utilitati.infrastructure import *
def testVerifData():
    '''
    Cazurile de testare pentru functia verifData()
    :return:
    '''
    assert verifData('31')==True
    assert verifData('a')==False
    assert verifData('0')==False

def testVerifTip():
    '''
    Cazuri de testare pentru functia verifTip()
    :return:
    '''
    assert verifTip('-')==True
    assert verifTip('+')==True
    assert verifTip('0')==False
    assert  verifTip('sdsd')==False

def testverifTranzactieValida():
    '''
    Testeaa functia verifTranzactieValida()
    :return:
    '''
    assert verifTranzactieValida({'zi': '1','suma':'2',"tip":'+'})==True
    assert verifTranzactieValida({'zi':'a','suma':'2',"tip":'-'})==False
    assert verifTranzactieValida({'zi':'1','suma':'b',"tip":'+'})==False
    assert verifTranzactieValida({'zi':'1','suma':'2',"tip":'b'})==False

def testverifAdaugareTranzactie():
    '''
    Testam functia verifAdaugareTranzactie()
    :return: -
    '''
    assert verifAdaugareTranzactie([{"zi":1,"suma": 2,"tip":'+'}],{"zi":1,"suma":3,"tip":'+'})==True
    assert verifAdaugareTranzactie([{"zi":4,"suma":2,"tip":'-'},{"zi":3,"suma":3,"tip":'-'}],{"zi":1,"suma":2,"tip":'+'})==False

def testTransferStrToInt():
    '''
    testarea finctiei transferStrToInt()
    :return:
    '''
    assert  transferStrToInt({"zi":'1',"suma":'2',"tip":'+'})=={"zi":1,"suma":2,"tip":'+'}
    assert  transferStrToInt({"zi":'3',"suma":'23',"tip":'-'})=={"zi":3,"suma":23,"tip":'-'}
def testadaugaTranzacite():
    '''
    testarea functiei adaugareTranzactie
    :return:
    '''
    assert adaugaTranzactie([],{"zi":1,"suma":2,"tip":'+'})==[{"zi":1,"suma":2,"tip":'+'}]
    assert adaugaTranzactie([{"zi":1,"suma":2,"tip":'+'}],{"zi":4,"suma":200,"tip":'+'})==[{"zi":4,"suma":200,"tip":'+'},{"zi":1,"suma":2,"tip":'+'}]
def testactualizeazaTranzactie():
    '''
    testarea functiei actualizeazaTranzactie()
    :return:
    '''
    assert actualizeazaTranzactie([{"zi":1,"suma":2,"tip":'+'}],{"zi":2,"suma":3,"tip":'+'},0)==[{"zi":2,"suma":3,"tip":'+'}]
    assert actualizeazaTranzactie([{"zi":2,"suma":2,"tip":'+'},{"zi":5,"suma":6,"tip":'+'}],{"zi":2,"suma":3,"tip":'+'},1)==[{"zi":2,"suma":2,"tip":'+'},{"zi":2,"suma":3,"tip":'+'}]

def testStergeTranzactiiPerZi():
    '''
    testarea functiei stergereTranzacitePerZi()
    :return:
    '''
    assert  stergereTranzacitePerZi([{"zi":3,"suma":2,"tip":'+'},{"zi":3,"suma":3,"tip":'-'},{"zi":3,"suma":4,"tip":'-'}],3)== []
    assert  stergereTranzacitePerZi([{"zi":3,"suma":2,"tip":'+'},{"zi":3,"suma":3,"tip":'-'},{"zi":2,"suma":4,"tip":'-'}],3)== [{"zi":2,"suma":4,"tip":'-'}]

def teststergeTranzactiiPerioada():
    '''
    testeaza functia stergeTranzactiiPerioada()
    :return:
    '''
    assert  stergeTranzactiiPerioada([{"zi":2,"suma":2,"tip":'+'},{"zi":2,"suma":3,"tip":'-'},{"zi":1,"suma":4,"tip":'-'}],1,2)== []
    #assert  stergeTranzactiiPerioada([[4,2,'+'],[3,3,'-'],[2,4,'-']],3,3)== [[4,2,'+'],[2,4,'-']]
    #assert  stergeTranzactiiPerioada([[4,2,'+'],[3,3,'-'],[2,4,'-']],2,2)== [[4,2,'+'],[3,3,'-']]

def testStergeTranzactiiTip():
    '''
    testeaza functia tergeTranzactiiTip()
    :return:
    '''
    assert  stergeTranzactiiTip([{"zi":3,"suma":2,"tip":'+'},{"zi":3,"suma":3,"tip":'-'},{"zi":3,"suma":4,"tip":'-'}],'-')== [{"zi":3,"suma":2,"tip":'+'}]
    #assert  stergeTranzactiiTip([[3,2,'+'],[3,3,'-'],[3,4,'-']],'+')== [[3,3,'-'],[3,4,'-']]

def testareCautaTranzactieSuma():
    '''
    testeaza functia testareCautaTranzactieSuma() pe teste date
    '''
    cont=[{"zi":5,"suma":2,"tip":'+'},{"zi":3,"suma":2,"tip":'-'},{"zi":3,"suma":2,"tip":'+'},{"zi":2,"suma":1,"tip":'-'}]
    assert cautaTranzactieSuma(cont,1)==[{"zi":5,"suma":2,"tip":'+'},{"zi":3,"suma":2,"tip":'-'},{"zi":3,"suma":2,"tip":'+'}]
    cont = [{"zi":5, "suma":2, "tip":'+'}, {"zi":3, "suma":2, "tip":'-'}, {"zi":3, "suma":2, "tip":'+'}, {"zi":2, "suma":1, "tip":'-'}]
    assert cautaTranzactieSuma(cont, 6) == []
def testareCautaTranzactieSumaSiZi():
    '''
    testeaza functia CautaTranzactieSumaSiZi pe teste date
    '''
    cont=[{"zi":5,"suma":2,"tip":'+'},{"zi":3,"suma":2,"tip":'-'},{"zi":3,"suma":2,"tip":'+'},{"zi":2,"suma":1,"tip":'-'}]
    assert cautaTranzactieSumaSiZi(cont,2,3)==[]
    cont = [{"zi":5, "suma":2, "tip":'+'}, {"zi":3, "suma":2, "tip":'-'}, {"zi":3, "suma":2,"tip": '+'}, {"zi":2, "suma":1, "tip":'-'}]
    assert cautaTranzactieSumaSiZi(cont, 1,2) == [{"zi":5, "suma":2, "tip":'+'}, {"zi":3, "suma":2,"tip": '-'}, {"zi":3, "suma":2, "tip":'+'}]
    cont = [{"zi":6, "suma":7, "tip":'+'}, {"zi":3, "suma":2, "tip":'-'}, {"zi":3,"suma": 2, "tip":'+'}, {"zi":2,"suma": 1, "tip":'-'}]
    assert cautaTranzactieSumaSiZi(cont, 5, 2) == [{"zi":6, "suma":7, "tip":'+'}]


def testareCautaTranzactieTip():
    '''
    testeaza functia CautaTranzactieTip() pe teste date
    :return:
    '''
    cont = [{"zi":5, "suma":2, "tip":'+'}, {"zi":3, "suma":2, "tip":'-'}, {"zi":3, "suma":2, "tip":'+'}, {"zi":2, "suma":1, "tip":'-'}]
    assert cautaTranzactieTip(cont, '-') == [{"zi":3, "suma":2, "tip":'-'},{"zi":2, "suma":1, "tip":'-'}]
    cont = [{"zi":5, "suma":2, "tip":'+'}, {"zi":3, "suma":2, "tip":'-'}, {"zi":3, "suma":2, "tip":'+'}, {"zi":2,"suma": 1, "tip":'-'}]
    assert cautaTranzactieTip(cont, '+') == [{"zi":5, "suma":2, "tip":'+'}, {"zi":3, "suma":2, "tip":'+'}]
    cont = [{"zi":6, "suma":7, "tip":'+'}, {"zi":3, "suma":2, "tip":'+'}, {"zi":3, "suma":2, "tip":'+'}, {"zi":2, "suma":1, "tip":'+'}]
    assert cautaTranzactieTip(cont, '-') == []
def testareFiltrareTip():
    cont = [{"zi":5, "suma":2, "tip":'+'}, {"zi":3,"suma": 2, "tip":'-'}, {"zi":3, "suma":2, "tip":'+'}, {"zi":2, "suma":1, "tip":'-'}]
    assert filtrareTip(cont,'-')==[{"zi":5, "suma":2, "tip":'+'},{"zi":3, "suma":2, "tip":'+'}]
    cont = [{"zi": 5, "suma": 2, "tip": '+'}, {"zi": 3, "suma": 2, "tip": '-'}, {"zi": 3, "suma": 2, "tip": '+'},{"zi": 2, "suma": 1, "tip": '-'}]
    assert filtrareTip(cont, '+')==[{"zi":3,"suma": 2, "tip":'-'},{"zi":2, "suma":1, "tip":'-'}]

testareFiltrareTip()
def testareFiltrareSuma():
    pass

def testraportSumaTip():
    '''
    testeaza functia raportSumaTip() pe teste date
    :return: -
    '''
    cont = [{"zi":5, "suma":2, "tip":'+'}, {"zi":3,"suma": 2, "tip":'-'}, {"zi":3, "suma":2, "tip":'+'}, {"zi":2, "suma":1, "tip":'-'}]
    assert (raportSumaTip(cont,'-')==3)
    assert (raportSumaTip(cont,'+')==4)
    cont=[{"zi":6, "suma":7, "tip":'+'}, {"zi":3, "suma":2, "tip":'+'}, {"zi":3, "suma":2, "tip":'+'}, {"zi":2, "suma":1, "tip":'+'}]
    assert (raportSumaTip(cont, '-') == 0)
    assert (raportSumaTip(cont, '+') == 12)

def testraportSoldData():
    '''
        testeaza functia raportSoldData() pe teste date
        :return:
        '''
    cont = [{"zi":5, "suma":2, "tip":'+'}, {"zi":3, "suma":2, "tip":'-'}, {"zi":3, "suma":2, "tip":'+'}, {"zi":2, "suma":1, "tip":'-'}]
    assert (raportSoldData(cont,3)==-1)
    assert (raportSoldData(cont,5)==1)
    cont= [{"zi":6, "suma":7, "tip":'+'}, {"zi":3, "suma":2, "tip":'-'}, {"zi":3, "suma":2, "tip":'+'}, {"zi":2, "suma":1, "tip":'-'}]
    assert (raportSoldData(cont, 3) == -1)
    assert (raportSoldData(cont, 6) == 6)

def testraportDupaSumaSiTip():
    '''
        testeaza functia raportDupaSumaSiTip() pe teste date
        :return:
        '''
    cont = [{"zi":5, "suma":2, "tip":'+'}, {"zi":3, "suma":2, "tip":'-'}, {"zi":3,"suma": 5, "tip":'+'}, {"zi":2, "suma":2, "tip":'-'}]
    assert (raportDupaSumaSiTip(cont,'+')==[{"zi":5, "suma":2, "tip":'+'}, {"zi":3,"suma": 5, "tip":'+'}])
    assert (raportDupaSumaSiTip(cont,'-')==[{"zi":3, "suma":2, "tip":'-'}, {"zi":2, "suma":2, "tip":'-'}])

def testFiltrareDupaTip():
    '''
    testeaza functia filtrareTip()
    :return:
    '''
    cont = [{"zi": 5, "suma": 2, "tip": '+'}, {"zi": 3, "suma": 2, "tip": '-'}, {"zi": 3, "suma": 2, "tip": '+'},
            {"zi": 2, "suma": 1, "tip": '-'}]
    assert filtrareTip(cont,'+')==[{"zi": 3, "suma": 2, "tip": '-'},{"zi": 2, "suma": 1, "tip": '-'}]
    cont = [{"zi": 5, "suma": 2, "tip": '+'}, {"zi": 3, "suma": 2, "tip": '-'}, {"zi": 3, "suma": 2, "tip": '+'},
            {"zi": 2, "suma": 1, "tip": '-'}]
    assert filtrareTip(cont,'-')==[{"zi": 5, "suma": 2, "tip": '+'},{"zi": 3, "suma": 2, "tip": '+'}]

def testFiltrareDupaSumaSiTip():
    '''
    testeaza fuctia filtrareMaiMicCaOSuma()

    :return:
    '''
    cont = [{"zi": 5, "suma": 2, "tip": '+'}, {"zi": 3, "suma": 7, "tip": '+'}, {"zi": 3, "suma": 2, "tip": '+'},
            {"zi": 2, "suma": 1, "tip": '-'}]
    assert filtrareMaiMicCaOSuma(cont,5,'+')==[{"zi": 3, "suma": 7, "tip": '+'},{"zi": 2, "suma": 1, "tip": '-'}]

def run_teste():
    testVerifData()
    testVerifTip()
    testverifTranzactieValida()
    testverifAdaugareTranzactie()
    testTransferStrToInt()
    testadaugaTranzacite()
    testactualizeazaTranzactie()
    testStergeTranzactiiPerZi()
    teststergeTranzactiiPerioada()
    testStergeTranzactiiTip()
    testareCautaTranzactieSuma()
    testareCautaTranzactieSumaSiZi()
    testareCautaTranzactieTip()
    testareFiltrareTip()
    testraportSumaTip()
    testareFiltrareSuma()
    testraportSoldData()
    testraportDupaSumaSiTip()
    testFiltrareDupaTip()
    testFiltrareDupaSumaSiTip()