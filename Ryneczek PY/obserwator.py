from __future__ import annotations
from typing import Dict, Type, Callable


class Obserwator:
    def __init__(self):
        super().__init__()
        self._zaktualizuj_metody: Dict[Type[Subject], Callable] = {}

    def zaktualizuj(self, subject: Subject) -> None:
        self._zaktualizuj_metody[type(subject)](subject)


class Subject:
    def __init__(self):
        super().__init__()
        self._obserwatorzy = []

    def dodaj_obserwatora(self, obserwator: Obserwator) -> None:
        self._obserwatorzy.append(obserwator)
        obserwator.zaktualizuj(self)

    def usun_obserwatora(self, obserwator: Obserwator) -> None:
        self._obserwatorzy.remove(obserwator)

    def powiadom_obserwatorow(self) -> None:
        for obserwator in self._obserwatorzy:
            obserwator.zaktualizuj(self)
