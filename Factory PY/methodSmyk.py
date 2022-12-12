from __future__ import annotations
from abc import abstractmethod, ABCMeta
from singleton import Singleton
from enum import Enum


class MethodABCMeta(metaclass=ABCMeta):
    @abstractmethod
    def operation(self) -> str:
        pass


class SmykCreator(metaclass=Singleton):
    @abstractmethod
    def metoda_wytw(self):
        pass

    def operacja(self) -> str:
        self.metoda_wytw()
        return str(self.__class__)


# produkty
# trzy kategorie po piec produktow
# zabawki: miś samochod stempelki pralka klocki
# ubranka: koszulka spodnie czapka buty bluza
# slodycze: lizak toblerone landrynki krowki kukulki

class ConcreteMis(MethodABCMeta):
    kolor = "brazowy"
    miekkosc = True

    def operation(self) -> str:
        return str(self.__class__)

    @staticmethod
    def przytul():
        print("jestem miekkim misiem tulisiem")


class ConcreteSamochod(MethodABCMeta):
    liczbaKol = 4

    def operation(self) -> str:
        return str(self.__class__)

    @staticmethod
    def jedz():
        print("wrum wrum")


class ConcreteStempelki(MethodABCMeta):
    kolor = "czerwony"

    def operation(self) -> str:
        return str(self.__class__)


class ConcretePralka(MethodABCMeta):
    def operation(self) -> str:
        return str(self.__class__)

    @staticmethod
    def wypierz():
        print("cykl prania rozpoczety")


class ConcreteKlocki(MethodABCMeta):
    def operation(self) -> str:
        return str(self.__class__)


class ConcreteKoszulka(MethodABCMeta):
    material = "bawelna"

    def operation(self) -> str:
        return str(self.__class__)


class ConcreteSpodnie(MethodABCMeta):
    material = "bawelna"
    rozmiar = 34

    def operation(self) -> str:
        return str(self.__class__)


class ConcreteButy(MethodABCMeta):
    podeszwa = "gruba"

    def operation(self) -> str:
        return str(self.__class__)


class ConcreteCzapka(MethodABCMeta):
    zdaszkiem = True

    def operation(self) -> str:
        return str(self.__class__)

class ConcreteBluza(MethodABCMeta):
    kieszenie = 2
    czysta = False

    def operation(self) -> str:
        return str(self.__class__)

    def wypierz(self):
        self.czysta = True


class ConcreteLizak(MethodABCMeta):
    smak = "truskawka"

    def operation(self) -> str:
        return str(self.__class__)


class ConcreteToblerone(MethodABCMeta):
    zawartosc_kakao = 0.7

    def operation(self) -> str:
        return str(self.__class__)

    @staticmethod
    def podziel():
        print("duzo kawalkow dla kazdego")


class ConcreteLandrynki(MethodABCMeta):
    def operation(self) -> str:
        return str(self.__class__)


class ConcreteKrowki(MethodABCMeta):
    def operation(self) -> str:
        return str(self.__class__)


class ConcreteKukulki(MethodABCMeta):
    def operation(self) -> str:
        return str(self.__class__)


class ConcreteCreatorMis(SmykCreator):
    def metoda_wytw(self) -> MethodABCMeta:
        return ConcreteMis()


class ConcreteCreatorSamochod(SmykCreator):
    def metoda_wytw(self) -> MethodABCMeta:
        return ConcreteSamochod()


class ConcreteCreatorStempelki(SmykCreator):
    def metoda_wytw(self) -> MethodABCMeta:
        return ConcreteStempelki()


class ConcreteCreatorKlocki(SmykCreator):
    def metoda_wytw(self) -> MethodABCMeta:
        return ConcreteKlocki()


class ConcreteCreatorPralka(SmykCreator):
    def metoda_wytw(self) -> MethodABCMeta:
        return ConcretePralka()


class ConcreteCreatorKoszulka(SmykCreator):
    def metoda_wytw(self) -> MethodABCMeta:
        return ConcreteKoszulka()


class ConcreteCreatorSpodnie(SmykCreator):
    def metoda_wytw(self) -> MethodABCMeta:
        return ConcreteSpodnie()


class ConcreteCreatorButy(SmykCreator):
    def metoda_wytw(self) -> MethodABCMeta:
        return ConcreteButy()


class ConcreteCreatorCzapka(SmykCreator):
    def metoda_wytw(self) -> MethodABCMeta:
        return ConcreteCzapka()


class ConcreteCreatorBluza(SmykCreator):
    def metoda_wytw(self) -> MethodABCMeta:
        return ConcreteBluza()


class ConcreteCreatorLizak(SmykCreator):
    def metoda_wytw(self) -> MethodABCMeta:
        return ConcreteLizak()


class ConcreteCreatorToblerone(SmykCreator):
    def metoda_wytw(self) -> MethodABCMeta:
        return ConcreteToblerone()


class ConcreteCreatorLandrynki(SmykCreator):
    def metoda_wytw(self) -> MethodABCMeta:
        return ConcreteLandrynki()


class ConcreteCreatorKrowki(SmykCreator):
    def metoda_wytw(self) -> MethodABCMeta:
        return ConcreteKrowki()


class ConcreteCreatorKukulki(SmykCreator):
    def metoda_wytw(self) -> MethodABCMeta:
        return ConcreteKukulki()


class MethodMenu(Enum):
    mis = ConcreteCreatorMis
    samochod = ConcreteCreatorSamochod
    klocki = ConcreteCreatorKlocki
    pralka = ConcreteCreatorPralka
    stempelki = ConcreteCreatorStempelki

    lizak = ConcreteCreatorLizak
    toblerone = ConcreteCreatorToblerone
    landrynki = ConcreteCreatorLandrynki
    krowki = ConcreteCreatorKrowki
    kukulki = ConcreteCreatorKukulki

    koszulka = ConcreteCreatorKoszulka
    spodnie = ConcreteCreatorSpodnie
    buty = ConcreteCreatorButy
    czapka = ConcreteCreatorCzapka
    bluza = ConcreteCreatorBluza

    wszystkie = [mis, samochod, klocki,
                 stempelki, pralka, lizak, toblerone,
                 landrynki, kukulki, krowki, koszulka,
                 spodnie, buty, czapka,
                 bluza]
