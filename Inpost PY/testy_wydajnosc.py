import cProfile

from fabryka import Fabryka
from pelnomocnik import Pelnomocnik
from sortownia import Sortownia
from paczkomat import Paczkomat
from kupujacy import Kupujacy

fabryka = Fabryka()
sortownia = Sortownia()
paczkomat = Paczkomat("jeden", 10)
proxy = Pelnomocnik(fabryka, sortownia)
kupujacy = [Kupujacy("klient_" + str(i)) for i in range(20)]


def testy_fabryka(iteracje):
    for i in range(iteracje):
        for p in ['mis', 'samochod', 'stempelki', 'pralka', 'klocki',
                  'lizak', 'toblerone', 'landrynki', 'krowki', 'kukulki',
                  'koszulka', 'spodnie', 'buty', 'bluza', 'czapka']:
            fabryka.zbuduj(p, proxy)


def run_testy_fabryka():
    cProfile.runctx('testy_fabryka(10000)', globals(), locals())


def test_ogolny(iteracje):
    for k in kupujacy:
        paczkomat.dodaj_obserwatora(k)
    for day in range(iteracje):
        print(">dzien", day)
        for k in kupujacy:
            k.zamow(proxy)
        paczkomat.przyjmij_dostawe(sortownia)


def run_test_ogolny():
    cProfile.runctx('test_ogolny(1000)', globals(), locals())


run_test_ogolny()
