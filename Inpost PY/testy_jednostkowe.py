import unittest
from fabryka import Fabryka
from pelnomocnik import Pelnomocnik
from kupujacy import Kupujacy
from sortownia import Sortownia
from paczkomat import Paczkomat


class testy(unittest.TestCase):
    # proba zamowienia produktu bezposrednio od fabryki, zamiast przez posrednika
    def test1(self):
        fabryka = Fabryka()
        kupujacy1 = Kupujacy("kupujacy_1")
        wynik = kupujacy1.zamow(fabryka)
        self.assertEqual("przyjmujemy zamowienia tylko przez pelnomocnika", wynik)

    # proba zamowienia nieistniejacego produktu przez pelnomocnika
    def test2(self):
        fabryka = Fabryka()
        sortownia = Sortownia()
        proxy = Pelnomocnik(fabryka, sortownia)
        wynik = proxy._fabryka.zbuduj("maslo", proxy)
        self.assertEqual('nie znaleziono fabryki dla produktu', wynik)

    # proba zamowienia nieistniejacego produktu przez klienta
    def test3(self):
        fabryka = Fabryka()
        sortownia = Sortownia()
        proxy = Pelnomocnik(fabryka, sortownia)
        kupujacy3 = Kupujacy("kupujacy_3")
        kupujacy3.potrzeba = "maslo"
        self.assertEqual('nie znaleziono fabryki dla produktu', kupujacy3.zamow(proxy))

    # proba zamowienia z zamknietej fabryki
    def test4(self):
        fabryka = Fabryka()
        sortownia = Sortownia()
        proxy = Pelnomocnik(fabryka, sortownia)
        fabryka.otwarta = False
        kupujacy4 = Kupujacy("kupujacy_4")
        wynik = kupujacy4.zamow(proxy)
        self.assertEqual("zamknieta", wynik)
        fabryka.otwarta = True

    # test singleton fabryka
    def test5(self):
        fabryka = Fabryka()
        czy_otwarta_fabryka1 = fabryka.otwarta
        fabryka2 = Fabryka()
        fabryka2.otwarta = not (czy_otwarta_fabryka1)
        self.assertEqual(fabryka2.otwarta, fabryka.otwarta)

    # test singleton kupujacy
    def test6(self):
        kupujacy6a = Kupujacy("kupujacy_6")
        kupujacy6b = Kupujacy("kupujacy_6")
        kupujacy6b.potrzeba = "test"
        kupujacy6a.potrzeba = "test"
        self.assertNotEqual(kupujacy6b, kupujacy6a)

    # test singleton pelnomocnik
    def test7(self):
        for i in range(100):
            fabryka = Fabryka()
            sortownia = Sortownia()
            proxy1 = Pelnomocnik(fabryka, sortownia)
            proxy2 = Pelnomocnik(fabryka, sortownia)
            self.assertEqual(proxy2, proxy1)

    # do pelnego paczkomatu nie da rady przywiezc paczki
    def test9(self):
        for i in range(100):
            fabryka = Fabryka()
            sortownia = Sortownia()
            paczkomat = Paczkomat("jeden", 10)
            proxy = Pelnomocnik(fabryka, sortownia)
            kupujacy = Kupujacy("kupujacy_9")
            # paczkomat.dodaj_obserwatora(kupujacy)
            paczkomat.paczki = ["obiekt" for i in range(10)]
            ile_przed = len(paczkomat.paczki)
            kupujacy.zamow(proxy)
            paczkomat.przyjmij_dostawe(sortownia)
            ile_po = len(paczkomat.paczki)
            paczkomat.paczki = []
            self.assertTrue(ile_po == ile_przed)

    # paczka ktora trafia do kupujacego zawiera dokladnie to co zamowil
    def test10(self):
        for i in range(100):
            fabryka = Fabryka()
            sortownia = Sortownia()
            paczkomat = Paczkomat("jeden", 10)
            proxy = Pelnomocnik(fabryka, sortownia)
            kupujacy = Kupujacy("kupujacy_10")
            paczkomat.dodaj_obserwatora(kupujacy)
            kupujacy.zamow(proxy)
            paczkomat.przyjmij_dostawe(sortownia)
            self.assertRegex(kupujacy.w_paczce, kupujacy.potrzeba)

"""
    # zamowiony produkt pojawia sie w paczkomacie
    def test8(self):
        fabryka = Fabryka()
        sortownia = Sortownia()
        paczkomat = Paczkomat("jeden", 10)
        sortownia.nowepaczki = []
        paczkomat.paczki = []
        proxy = Pelnomocnik(fabryka, sortownia)
        kupujacy = Kupujacy("kupujacy_8")
        kupujacy.potrzeba = "krowki"
        # paczkomat.dodaj_obserwatora(kupujacy)
        ile_przed = len(paczkomat.paczki)
        kupujacy.zamow(proxy)
        paczkomat.przyjmij_dostawe(sortownia)
        ile_po = len(paczkomat.paczki)
        self.assertTrue(ile_po > ile_przed)
"""