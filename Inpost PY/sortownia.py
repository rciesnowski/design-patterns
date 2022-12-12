from odwiedzajacy import AbstractOdwiedzajacyDostawa
from dekorator import Paczka

# sortownia korzysta ze wzorca odwiedzający, aby wypełniać paczkomaty

class Sortownia(AbstractOdwiedzajacyDostawa):
    nowepaczki = []
    def __init__(self):
        super().__init__()

    def przychodzace(self, paczka: Paczka):
        print("\tsortownia:\t\totrzymalismy paczke dla " + str(paczka.adresat.nazwa))
        self.nowepaczki.append(paczka)

    def odwiedziny(self, paczkomat):
        if len(self.nowepaczki) < paczkomat.ile_pustych():
            paczkomat.paczki += self.nowepaczki
        else:
            ile_mniej = paczkomat.ile_pustych()
            paczkomat.paczki += self.nowepaczki[:paczkomat.ile_pustych()]
            del self.nowepaczki[0:ile_mniej]
            paczkomat.ile_w_magazynie = len(self.nowepaczki)
            print("\tsortownia:\t\t" + str(len(self.nowepaczki)) + " paczek wciaz czeka w sortowni")