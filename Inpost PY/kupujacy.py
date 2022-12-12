import random
from obserwator import Obserwator
from fabryka import AbstractSingleton
from dekorator import Paczka
from paczkomat import Paczkomat


class Kupujacy(Obserwator):
    def __init__(self, nazwa: str):
        super().__init__()
        self.czas_ocz = 1
        self.nazwa = nazwa
        self.w_paczce = ""
        self.potrzeba: str = random.choice(['mis', 'samochod', 'stempelki', 'pralka', 'klocki',
                                            'lizak', 'toblerone','landrynki', 'krowki', 'kukulki',
                                            'koszulka', 'spodnie', 'buty', 'bluza', 'czapka'])
        self._zaktualizuj_metody[Paczkomat] = self.sprawdz_czy_jest


    def zamow(self, fabryka: AbstractSingleton):
        if random.randint(0,self.czas_ocz) <= 1:
            return fabryka.zbuduj(self.potrzeba, self)

    def wysylka(self, paczka: Paczka):
        if paczka.adresat == self:
            print(paczka.component)

    def sprawdz_czy_jest(self, paczkomat: Paczkomat):
        for p in paczkomat.paczki:
            if p.adresat == self:
                print("\t" + self.nazwa + ":\t\tjest paczka dla mnie, a w srodku " + p.component.name)
                self.w_paczce = p.component.name.lower()
                paczkomat.paczki.remove(p)
        self.czas_ocz = paczkomat.ile_w_magazynie + 1