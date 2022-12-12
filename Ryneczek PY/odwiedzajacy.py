from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractOdwiedzajacyWyplata(ABC):
    @abstractmethod
    def odwiedziny(self, kupujacy):
        pass


class AbstractOdwiedzajacyDostawa(ABC):
    @abstractmethod
    def odwiedziny(self, seller):
        pass


class Wyplata(AbstractOdwiedzajacyWyplata):
    def odwiedziny(self, kupujacy):
        kupujacy.pieniadze += 5000


class Dostawa(AbstractOdwiedzajacyDostawa):
    def odwiedziny(self, sprzedawca):
        sprzedawca.na_stanie = sprzedawca.wielkosc_dostaw

