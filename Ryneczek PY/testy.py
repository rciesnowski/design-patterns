from symulacja import Kupujacy, Sprzedawca, Produkt, BankCentralny
from odwiedzajacy import Wyplata, Dostawa
import unittest


class testy(unittest.TestCase):
    # obliczanie cen
    def test1(self):
        s = Sprzedawca("s1", Produkt("p1", 100), 1)
        s.inflacja = 0.1
        s.marza = 0.1
        # 1.1 * 1.1 * 100
        self.assertAlmostEqual(s.cena, 121)

    # sprawdzanie magazynu
    def test2(self):
        s = Sprzedawca("s2", Produkt("p2", 100), 1)
        self.assertTrue(s.czy_na_stanie)

    # brak na stanie
    def test3(self):
        s = Sprzedawca("s3", Produkt("p3", 100), 0)
        self.assertFalse(s.czy_na_stanie)

    # pieniadze znikaja z konta sprzedajacego
    def test4(self):
        s = Sprzedawca("s4", Produkt("p4", 1000), 1)
        s.marza = 0
        k = Kupujacy("k4", "p4")
        k.pieniadze = 1000
        k.sprawdz_cene(s)
        self.assertEqual(k.pieniadze, 0)

    # klient nie kupuje jesli cena jest zbyt wysoka
    def test5(self):
        s = Sprzedawca("s5", Produkt("p5", 1000), 1)
        s.marza = 0.5
        k = Kupujacy("k5", "p5")
        k.zasada = 40
        k.sprawdz_cene(s)
        k.pieniadze = 1500
        self.assertEqual(k.pieniadze, 1500)

    # bank dostaje informacje o wplywach
    def test6(self):
        b = BankCentralny()
        s = Sprzedawca("s6", Produkt("p6", 100), 1)
        s.marza = 0.1
        b.inflacja = 0.2
        s.dodaj_obserwatora(b)
        b.dodaj_obserwatora(s)
        self.assertAlmostEqual(b.wplywy_podatkowe, 22)

    # wyplata zwieksza saldo konta kupujacego
    def test7(self):
        k = Kupujacy("k7", "p7")
        k.pieniadze = 1
        k.otrzymaj_wyplate(Wyplata())
        self.assertEqual(k.pieniadze, 5001)

    # dostawa napełnia magazyn
    def test8(self):
        s = Sprzedawca("s8", Produkt("p8", 0), 1)
        s.na_stanie = 0
        s.przyjmij_dostawe(Dostawa())
        self.assertTrue(s.czy_na_stanie)
