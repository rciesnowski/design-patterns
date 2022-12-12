from abc import ABCMeta, abstractmethod
from enum import Enum
from singleton import Singleton


class RegABCMeta(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def zbuduj():
        pass


# konkretne produkty
class ConcreteMis(RegABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.kolor = "brazowy"
        self.miekkosc = True

    def zbuduj(self):
        return self

    @staticmethod
    def przytul():
        print("jestem miekkim misiem tulisiem")


class ConcreteSamochod(RegABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.liczbaKol = 4

    def zbuduj(self):
        return self

    @staticmethod
    def jedz():
        print("wrum wrum")


class ConcreteStempelki(RegABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.kolor = "czerwony"

    def zbuduj(self):
        return self


class ConcretePralka(RegABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self

    @staticmethod
    def wypierz():
        print("cykl prania rozpoczety")


class ConcreteKlocki(RegABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self


class ConcreteKoszulka(RegABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.material = "bawelna"

    def zbuduj(self):
        return self


class ConcreteSpodnie(RegABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.material = "bawelna"
        self.rozmiar = 34

    def zbuduj(self):
        return self


class ConcreteButy(RegABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.podeszwa = "gruba"

    def zbuduj(self):
        return self


class ConcreteCzapka(RegABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.zdaszkiem = True

    def zbuduj(self):
        return self


class ConcreteBluza(RegABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self


class ConcreteLizak(RegABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.smak = "truskawka"

    def zbuduj(self):
        return self


class ConcreteToblerone(RegABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.czekolada = "mleczna"

    def zbuduj(self):
        return self

    @staticmethod
    def podziel():
        print("duzo kawalkow dla kazdego")


class ConcreteLandrynki(RegABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self


class ConcreteKrowki(RegABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self


class ConcreteKukulki(RegABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self


class RegSmyk(metaclass=Singleton):
    def __init__(self) -> None:
        self.zarejestrowane = {}

    def register(self, class_name, class_init):
        self.zarejestrowane[class_name] = class_init

    @classmethod
    def zbuduj(cls, self, factory):
        imp = self.zarejestrowane[factory]()
        return imp.zbuduj()


class RegMenu(Enum):
    mis = ['mis', ConcreteMis]
    samochod = ['samochod', ConcreteSamochod]
    klocki = ['klocki', ConcreteKlocki]
    pralka = ['pralka', ConcretePralka]
    stempelki = ['stempelki', ConcreteStempelki]

    lizak = ['lizak', ConcreteLizak]
    toblerone = ['toblerone', ConcreteToblerone]
    landrynki = ['landrynki', ConcreteLandrynki]
    krowki = ['krowki', ConcreteKrowki]
    kukulki = ['kukulki', ConcreteKukulki]

    koszulka = ['koszulka', ConcreteKoszulka]
    spodnie = ['spodnie', ConcreteSpodnie]
    buty = ['buty', ConcreteButy]
    czapka = ['czapka', ConcreteCzapka]
    bluza = ['bluza', ConcreteBluza]

    wszystkie = [mis, samochod, klocki,
                 stempelki, pralka, lizak, toblerone,
                 landrynki, kukulki, krowki, koszulka,
                 spodnie, buty, czapka,
                 bluza]
