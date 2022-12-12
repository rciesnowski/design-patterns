from obserwator import Subject
from sortownia import Sortownia

# paczkomat jest obserwowany przez klientów - wysyła im powiadomienia, gdy nadchodzi dostawa

class Paczkomat(Subject):
    def __init__(self, nazwa: str, liczba_skrytek: int):
        super().__init__()
        self.nazwa = nazwa
        self.liczba_skrytek = liczba_skrytek
        self.paczki = []
        self.ile_w_magazynie = 0

    def ile_pustych(self):
        return self.liczba_skrytek - len(self.paczki)

    def przyjmij_dostawe(self, sortownia: Sortownia):
        print("\tpaczkomat:\t\tprzyjmuje dostawe")
        sortownia.odwiedziny(self)
        self.powiadom_obserwatorow()
