from __future__ import annotations
from odwiedzajacy import Wyplata, Dostawa
from obserwator import Subject, Obserwator
from odwiedzajacy import AbstractOdwiedzajacyDostawa, AbstractOdwiedzajacyWyplata
import random


class Produkt:
    def __init__(self, nazwa: str, koszt: float):
        self.nazwa = nazwa
        self.koszt = koszt


# do zadan banku centralnego nalezy kontrolowanie wplywow podatkowych i ustalanie wskaznika inflacji
class BankCentralny(Obserwator, Subject):
    def __init__(self):
        super().__init__()
        # startowa inflacja, będzie aktualizowana każdego miesiąca
        self.inflacja = 0.1
        self.wplywy_podatkowe = 0.0
        # 50k pozwoli wypłacić wypłaty wszystkim kupującym obywatelom
        self.cel_wplywow = 50000.0
        self._zaktualizuj_metody[Sprzedawca] = self.zaktualizuj_wplywy

    # bank obserwuje sprzedawcow
    def zaktualizuj_wplywy(self, subject: Sprzedawca):
        self.wplywy_podatkowe += subject.podatek

    # pod koniec miesiaca bedzie obliczany wskaznik inflacji na podstawie tego, ile wplynelo do budżetu
    def algorytm_inflacyjny(self):
        self.inflacja *= self.cel_wplywow / self.wplywy_podatkowe
        self.wplywy_podatkowe = 0.0
        self.powiadom_obserwatorow()


class Sprzedawca(Obserwator, Subject):
    def __init__(self, nazwa: str, produkt: Produkt, na_stanie: int):
        super().__init__()
        self.nazwa = nazwa
        # sprzedawcy maja rozne marże
        self.marza = random.randint(5,25)/100
        self.dochod = 0
        self.inflacja = 0
        self.produkt = produkt
        self.wielkosc_dostaw = na_stanie
        self.na_stanie = na_stanie
        self._zaktualizuj_metody[BankCentralny] = self.pobierz_inflacje_z_banku

    # sprzedawca pobiera informację o inflacji z banku centralnego (obserwator) i powiadamia o tym klientow
    def pobierz_inflacje_z_banku(self, subject: BankCentralny) -> None:
        self.inflacja = subject.inflacja
        self.powiadom_obserwatorow()

    @property
    def cena(self):
        return (1 + self.marza) * (1 + self.inflacja) * self.produkt.koszt

    # pyta o to kupujący
    @property
    def czy_na_stanie(self):
        return self.na_stanie > 0

    # pyta o to bank
    @property
    def podatek(self):
        return (1 + self.marza) * self.inflacja * self.produkt.koszt

    def sprzedaj(self):
        self.na_stanie -= 1
        self.dochod = self.produkt.koszt * self.marza
        self.powiadom_obserwatorow()

    # na poczatku miesiaca wypelniane sa magazyny
    def przyjmij_dostawe(self, visitor: AbstractOdwiedzajacyDostawa):
        visitor.odwiedziny(self)


# każdy sprzedawca sprzedaje okreslona ilosc produktu z okreslonym kosztem
nazwy_produktow = ["telewizor", "remont", "samochod", "drogie krzeslo", "fajny wazon", "traktor", "obraz", "dizajnerska skarpeta", "czołg", "helikopter"]
sprzedawcy = [Sprzedawca(
    "sprzedawca_" + str(i), # nazwa sprzedawcy
    Produkt(
        nazwy_produktow[i], # nazwa produktu
        random.randint(1000, 100000)), # koszt produktu
    random.randint(1, 5)) for i in range(10)] # rozmiar magazynu


class Kupujacy(Obserwator):
    def __init__(self, nazwa: str, potrzeba: str):
        super().__init__()
        self.memory_of_bygone_prices = 1000000
        self.nazwa = nazwa
        self.zasada = 42
        self.potrzeba: str = potrzeba
        self.pieniadze: float = 20000
        self._zaktualizuj_metody[Sprzedawca] = self.sprawdz_cene

    # kupujący jest tu w roli obserwatora sprzedawcy
    def sprawdz_cene(self, sprzedawca: Sprzedawca):
        if sprzedawca.cena <= self.pieniadze and sprzedawca.czy_na_stanie:
            # im wieksza rozbieznosc miedzy ceną a kosztem produktu, tym mniejsza szansa że klient się na niego zdecyduje
            # przykładowo jesli produkt jest 1.3 drozszy niz optymalna cena, istnieje tylko 25% szans że random.randint(0,40) będzie większy niż 30; dla 1.2 - 50%, itd.
            if sprzedawca.cena <= self.memory_of_bygone_prices:
                print("\t" + self.nazwa + ":\tkupuje od", sprzedawca.nazwa, self.potrzeba, "za", "%.2f" % sprzedawca.cena)
                self.memory_of_bygone_prices = sprzedawca.cena
                self.kup(sprzedawca)
            else:
                r = random.randint(0, self.zasada)
                if r > ((sprzedawca.cena * 100 / sprzedawca.produkt.koszt) - 100):
            # prostszy sposob, bez losowości:
            # if sprzedawca.cena / sprzedawca.produkt.koszt < 1.3:
                    print("\t" + self.nazwa + ":\tkupuje od", sprzedawca.nazwa, self.potrzeba, "za", "%.2f" % sprzedawca.cena)
                    self.memory_of_bygone_prices = sprzedawca.cena
                    self.kup(sprzedawca)
                else:
                    print("\t" + self.nazwa + ":\tnie podoba mi sie cena", "%.2f" % sprzedawca.cena, "za", self.potrzeba, "u", sprzedawca.nazwa)

    # metoda uruchamiana jeśli wszystkie warunki są spełnione
    def kup(self, sprzedawca: Sprzedawca):
        self.pieniadze -= sprzedawca.cena
        sprzedawca.sprzedaj()

    # metoda umożliwia odwiedzającemu zwiększenie salda konta
    def otrzymaj_wyplate(self, odwiedzajacy: AbstractOdwiedzajacyWyplata):
        odwiedzajacy.odwiedziny(self)


# wyposażamy kupujących w potrzeby
kupujacy = [Kupujacy("kupujacy_" + str(i), nazwy_produktow[i]) for i in range(10)]
bank = BankCentralny()

print(">miesiac 1\n\tbank centr:\tinflacja 10 %")
for s in sprzedawcy:
    bank.dodaj_obserwatora(s)
    s.dodaj_obserwatora(bank)
for s in sprzedawcy:
    for k in kupujacy:
        if k.potrzeba == s.produkt.nazwa: s.dodaj_obserwatora(k)
# obserwacja na przestrzeni 5 lat (60 miesiecy)
for miesiac in range(59):
    print(">miesiac", miesiac+2, "\n\tbank centr:\tinflacja", "%.2f" % (bank.inflacja*100), "%")
    for k in kupujacy: k.otrzymaj_wyplate(Wyplata())
    for s in sprzedawcy: s.przyjmij_dostawe(Dostawa())
    bank.algorytm_inflacyjny()
