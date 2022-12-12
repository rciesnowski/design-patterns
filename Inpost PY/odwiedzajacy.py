from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractOdwiedzajacyDostawa(ABC):
    @abstractmethod
    def odwiedziny(self, paczkomat):
        pass

