from fabryka import AbstractABCMeta

# wzorzec dekorator - paczka jest nakładką na produkt, rozszerza go o pola adresat i możliwość współpracy z paczkomatem

class Decorator(AbstractABCMeta):
    _component: AbstractABCMeta = None

    def __init__(self, component: AbstractABCMeta) -> None:
        self._component = component

    @property
    def component(self) -> AbstractABCMeta:
        return self._component

    def zbuduj(self) -> str:
        return self._component.zbuduj()


class Paczka(Decorator):
    def __init__(self, component: AbstractABCMeta, adresat) -> None:
        super().__init__(component)
        self._component = component
        self.adresat = adresat
    def zbuduj(self) -> str:
        return f"Paczka({self.component}) do {self.adresat}"