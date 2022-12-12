import cProfile
from abstractSmyk import AbstractMenu
from methodSmyk import MethodMenu
from regSmyk import RegSmyk, RegMenu
from refSmyk import RefSmyk, RefMenu
from simpleSmyk import SimpleMenu

produkty = ['mis', 'samochod', 'stempelki', 'pralka', 'klocki', 'lizak', 'toblerone', 'landrynki', 'krowki', 'kukulki',
            'koszulka', 'spodnie', 'buty', 'bluza', 'czapka']


def simple_run(iteracje, isprint):
    for i in range(iteracje):
        for p in produkty:
            if isprint:
                print(SimpleMenu.call(p))
            else:
                SimpleMenu.call(p)


def method_run(iteracje, isprint):
    for i in range(iteracje):
        for p in MethodMenu.wszystkie.value:
            if isprint:
                print(p().operacja())
            else:
                p().operacja()


def abstract_run(iteracje, isprint):
    for i in range(iteracje):
        for p in produkty:
            if isprint:
                print(AbstractMenu.call(p))
            else:
                AbstractMenu.call(p)


def rejestracja():
    for item in RegMenu.wszystkie.value:
        RegSmyk().register(item[0], item[1])
    for item in RefMenu.wszystkie.value:
        RefSmyk().register(item)


def reg_run(iteracje, isprint):
    for i in range(iteracje):
        for prod in RegSmyk().zarejestrowane:
            if isprint:
                print(RegSmyk.zbuduj(RegSmyk(), prod))
            else:
                RegSmyk.zbuduj(RegSmyk(), prod)


def ref_run(iteracje, isprint):
    for i in range(iteracje):
        for p in RefSmyk().zarejestrowane:
            if isprint:
                print(RefSmyk.zbuduj(RefSmyk(), p))
            else:
                RefSmyk.zbuduj(RefSmyk(), p)


# simple_run(1, True)
# bstract_run(1, True)
# method_run(1, True)
# rejestracja()
# reg_run(1, True)
# ref_run(1, True)

print(">fabryka prosta")
cProfile.runctx('simple_run(10000, False)', globals(), locals())
print(">fabryka z metodą wytwórczą")
cProfile.runctx('method_run(10000, False)', globals(), locals())
print(">fabryka abstrakcyjna")
cProfile.runctx('abstract_run(10000, False)', globals(), locals())
print(">rejestracja")
cProfile.runctx('rejestracja()', globals(), locals())
print(">rejestracja klas bez refleksji")
cProfile.runctx('reg_run(10000, False)', globals(), locals())
print(">rejestracja klas z wykorzystaniem refleksji")
cProfile.runctx('ref_run(10000, False)', globals(), locals())
