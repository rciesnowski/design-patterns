from enum import Enum
from singleton import Singleton
from abc import ABCMeta, abstractmethod


class SimpleABCMeta(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def zbuduj():
        pass


class ConcreteMis(SimpleABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.kolor = "brazowy"
        self.miekkosc = True

    def zbuduj(self):
        return self

    @staticmethod
    def przytul():
        print("jestem miekkim misiem tulisiem")


class ConcreteSamochod(SimpleABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.liczbaKol = 4

    def zbuduj(self):
        return self

    @staticmethod
    def jedz():
        print("wrum wrum")


class ConcreteStempelki(SimpleABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.kolor = "czerwony"

    def zbuduj(self):
        return self


class ConcretePralka(SimpleABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self

    @staticmethod
    def wypierz():
        print("cykl prania rozpoczety")


class ConcreteKlocki(SimpleABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self


class ConcreteKoszulka(SimpleABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.material = "bawelna"

    def zbuduj(self):
        return self


class ConcreteSpodnie(SimpleABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.material = "bawelna"
        self.rozmiar = 34

    def zbuduj(self):
        return self


class ConcreteButy(SimpleABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.podeszwa = "gruba"

    def zbuduj(self):
        return self


class ConcreteCzapka(SimpleABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.zdaszkiem = True

    def zbuduj(self):
        return self


class ConcreteBluza(SimpleABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.kieszenie = 2
        self.czysta = False

    def zbuduj(self):
        return self

    def wypierz(self):
        self.czysta = True


class ConcreteLizak(SimpleABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.smak = "truskawka"

    def zbuduj(self):
        return self


class ConcreteToblerone(SimpleABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.czekolada = "mleczna"

    def zbuduj(self):
        return self

    @staticmethod
    def podziel():
        print("duzo kawalkow dla kazdego")


class ConcreteLandrynki(SimpleABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self


class ConcreteKrowki(SimpleABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self


class ConcreteKukulki(SimpleABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self


class SimpleSmyk(metaclass=Singleton):
    @classmethod
    def zbuduj(cls, factory):
        try:
            if factory == 'mis':
                imp = ConcreteMis()
                return imp.zbuduj()
            if factory == 'samochod':
                imp = ConcreteSamochod()
                return imp.zbuduj()
            if factory == 'stempelki':
                imp = ConcreteStempelki()
                return imp.zbuduj()
            if factory == 'pralka':
                imp = ConcretePralka()
                return imp.zbuduj()
            if factory == 'klocki':
                imp = ConcreteKlocki()
                return imp.zbuduj()
            if factory == 'lizak':
                imp = ConcreteLizak()
                return imp.zbuduj()
            if factory == 'toblerone':
                imp = ConcreteToblerone()
                return imp.zbuduj()
            if factory == 'landrynki':
                imp = ConcreteLandrynki()
                return imp.zbuduj()
            if factory == 'krowki':
                imp = ConcreteKrowki()
                return imp.zbuduj()
            if factory == 'kukulki':
                imp = ConcreteKukulki()
                return imp.zbuduj()
            if factory == 'koszulka':
                imp = ConcreteKoszulka()
                return imp.zbuduj()
            if factory == 'spodnie':
                imp = ConcreteSpodnie()
                return imp.zbuduj()
            if factory == 'buty':
                imp = ConcreteButy()
                return imp.zbuduj()
            if factory == 'czapka':
                imp = ConcreteCzapka()
                return imp.zbuduj()
            if factory == 'bluza':
                imp = ConcreteBluza()
                return imp.zbuduj()
            raise Exception('error: FACTORY NOT FOUND')
        except Exception as _e:
            print(_e)
        return None


class SimpleMenu(Enum):
    call = SimpleSmyk().zbuduj
