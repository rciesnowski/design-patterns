from abc import abstractmethod, ABCMeta
from singleton import Singleton


class AbstractSingleton(metaclass=Singleton):
    name = ""
    @staticmethod
    @abstractmethod
    def zbuduj(produkt, adresat):
        pass


class Fabryka(AbstractSingleton):
    otwarta = True
    @staticmethod
    def zbuduj(produkt, adresat):
        if isinstance(adresat, AbstractSingleton):
            print("\tfabryka:\t\totrzymaliśmy zamowienie na " + produkt + " od " + str(adresat.name))
            try:
                if produkt in ['mis', 'samochod','klocki', 'stempelki','pralka']:
                    return ZabawkiFactory.zbuduj_zabawke(produkt)
                if produkt in ['koszulka', 'spodnie', 'buty','czapka', 'bluza']:
                    return UbrankaFactory.zbuduj_ubranko(produkt)
                if produkt in ['toblerone', 'lizak', 'landrynki', 'kukulki','krowki']:
                    return SlodyczeFactory.zbuduj_slodycze(produkt)
                raise Exception('nie znaleziono fabryki dla produktu')
            except Exception as _e:
                print(_e)
                return 'nie znaleziono fabryki dla produktu'
        else:
            print("\tfarbyka:\t\tprzyjmujemy zamowienia tylko przez pelnomocnika")
            return "przyjmujemy zamowienia tylko przez pelnomocnika"


class AbstractABCMeta(metaclass=ABCMeta):
    name = ""
    @staticmethod
    @abstractmethod
    def zbuduj():
        pass


class ConcreteMis(AbstractABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.kolor = "brazowy"
        self.miekkosc = True

    def zbuduj(self):
        return self

    @staticmethod
    def przytul():
        print("jestem miekkim misiem tulisiem")


class ConcreteSamochod(AbstractABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.liczbaKol = 4

    def zbuduj(self):
        return self

    @staticmethod
    def jedz():
        print("wrum wrum")


class ConcreteStempelki(AbstractABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.kolor = "czerwony"

    def zbuduj(self):
        return self


class ConcretePralka(AbstractABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self

    @staticmethod
    def wypierz():
        print("cykl prania rozpoczety")


class ConcreteKlocki(AbstractABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self


class ConcreteKoszulka(AbstractABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.material = "bawelna"

    def zbuduj(self):
        return self


class ConcreteSpodnie(AbstractABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.material = "bawelna"
        self.rozmiar = 34

    def zbuduj(self):
        return self


class ConcreteButy(AbstractABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.podeszwa = "gruba"

    def zbuduj(self):
        return self


class ConcreteCzapka(AbstractABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.zdaszkiem = True

    def zbuduj(self):
        return self


class ConcreteBluza(AbstractABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.kieszenie = 2
        self.czysta = False

    def zbuduj(self):
        return self

    def wypierz(self):
        self.czysta = True


class ConcreteLizak(AbstractABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.smak = "truskawka"

    def zbuduj(self):
        return self


class ConcreteToblerone(AbstractABCMeta):
    def __init__(self):
        self.name = str(self.__class__)
        self.czekolada = "mleczna"

    def zbuduj(self):
        return self

    @staticmethod
    def podziel():
        print("duzo kawalkow dla kazdego")


class ConcreteLandrynki(AbstractABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self


class ConcreteKrowki(AbstractABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self


class ConcreteKukulki(AbstractABCMeta):
    def __init__(self):
        self.name = str(self.__class__)

    def zbuduj(self):
        return self


class ZabawkiFactory(metaclass=Singleton):
    @staticmethod
    def zbuduj_zabawke(prod):
        try:
            if prod == 'mis':
                return ConcreteMis()
            if prod == 'samochod':
                return ConcreteSamochod()
            if prod == 'stempelki':
                return ConcreteStempelki()
            if prod == 'pralka':
                return ConcretePralka()
            if prod == 'klocki':
                return ConcreteKlocki()
            raise Exception('error: CLASS NOT FOUND')
        except Exception as _e:
            print(_e)
        return None


class UbrankaFactory(metaclass=Singleton):
    @staticmethod
    def zbuduj_ubranko(produkt):
        try:
            if produkt == 'koszulka':
                return ConcreteKoszulka()
            if produkt == 'spodnie':
                return ConcreteSpodnie()
            if produkt == 'czapka':
                return ConcreteCzapka()
            if produkt == 'buty':
                return ConcreteButy()
            if produkt == 'bluza':
                return ConcreteBluza()
            raise Exception('error: CLASS NOT FOUND')
        except Exception as _e:
            print(_e)
        return None


class SlodyczeFactory(metaclass=Singleton):
    @staticmethod
    def zbuduj_slodycze(produkt):
        try:
            if produkt == 'lizak':
                return ConcreteLizak()
            if produkt == 'toblerone':
                return ConcreteToblerone()
            if produkt == 'krowki':
                return ConcreteKrowki()
            if produkt == 'kukulki':
                return ConcreteKukulki()
            if produkt == 'landrynki':
                return ConcreteLandrynki()
            raise Exception('error: CLASS NOT FOUND')
        except Exception as _e:
            print(_e)
        return None
