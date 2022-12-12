from fabryka import Fabryka, AbstractSingleton
from kupujacy import Kupujacy
from dekorator import Paczka
from sortownia import Sortownia

# pełnomocnik oddziela fabrykę od obowiązków komunikacji z sortownią i klientem

class Pelnomocnik(AbstractSingleton):
    def __init__(self, fabryka: Fabryka, sortownia: Sortownia) -> None:
        super().__init__()
        self._fabryka = fabryka
        self.sortownia = sortownia
        self.name = "pelnomocnik"

    def check_access(self) -> bool:
        return self._fabryka.otwarta

    def zbuduj(self, produkt: str, adresat: Kupujacy):
        if self.check_access():
            print("\tpelnomocnik:\totrzymalem zamowienie na " + produkt + " od " + str(adresat.nazwa))
            wyrob = self._fabryka.zbuduj(produkt, self)
            if wyrob != 'nie znaleziono fabryki dla produktu':
                print("\tpelnomocnik:\totrzymalem " + wyrob.name + " z fabryki")
                self.sortownia.przychodzace(Paczka(wyrob, adresat))
                return "ok"
            else:
                return wyrob
        else:
            return "zamknieta"
