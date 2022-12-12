from abc import ABCMeta, abstractmethod
from enum import Enum

from singleton import Singleton


# abstrakcyjny produkt
class RefABCMeta(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def zbuduj():
        pass


# konkretne produkty
class ConcreteMis(RefABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.kolor = "brazowy"
        self.miekkosc = True

    def zbuduj(self):
        return self

    @staticmethod
    def przytul():
        print("jestem miekkim misiem tulisiem")


class ConcreteSamochod(RefABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.liczbaKol = 4

    def zbuduj(self):
        return self

    @staticmethod
    def jedz():
        print("wrum wrum")


class ConcreteStempelki(RefABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.kolor = "czerwony"

    def zbuduj(self):
        return self


class ConcretePralka(RefABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self

    @staticmethod
    def wypierz():
        print("cykl prania rozpoczety")


class ConcreteKlocki(RefABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self


class ConcreteKoszulka(RefABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.material = "bawelna"

    def zbuduj(self):
        return self


class ConcreteSpodnie(RefABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.material = "bawelna"
        self.rozmiar = 34

    def zbuduj(self):
        return self


class ConcreteButy(RefABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.podeszwa = "gruba"

    def zbuduj(self):
        return self


class ConcreteCzapka(RefABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.zdaszkiem = True

    def zbuduj(self):
        return self


class ConcreteBluza(RefABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.kieszenie = 2
        self.czysta = False

    def zbuduj(self):
        return self

    def wypierz(self):
        self.czysta = True


class ConcreteLizak(RefABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.smak = "truskawka"

    def zbuduj(self):
        return self


class ConcreteToblerone(RefABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.czekolada = "mleczna"

    def zbuduj(self):
        return self

    @staticmethod
    def podziel():
        print("duzo kawalkow dla kazdego")


class ConcreteLandrynki(RefABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self


class ConcreteKrowki(RefABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self


class ConcreteKukulki(RefABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self


class RefSmyk(metaclass=Singleton):
    def __init__(self) -> None:
        self.zarejestrowane = {}

    def register(self, class_c):
        self.zarejestrowane[str(class_c)] = class_c

    @classmethod
    def zbuduj(cls, self, factory):
        imp = self.zarejestrowane[factory]()
        return imp.zbuduj()


class RefMenu(Enum):
    mis = ConcreteMis
    samochod = ConcreteSamochod
    klocki = ConcreteKlocki
    pralka = ConcretePralka
    stempelki = ConcreteStempelki
    lizak = ConcreteLizak
    toblerone = ConcreteToblerone
    landrynki = ConcreteLandrynki
    krowki = ConcreteKrowki
    kukulki = ConcreteKukulki
    koszulka = ConcreteKoszulka
    spodnie = ConcreteSpodnie
    buty = ConcreteButy
    czapka = ConcreteCzapka
    bluza = ConcreteBluza

    wszystkie = [mis, samochod, klocki,
                 stempelki, pralka, lizak, toblerone,
                 landrynki, kukulki, krowki, koszulka,
                 spodnie, buty, czapka,
                 bluza]
