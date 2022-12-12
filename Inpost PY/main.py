from matplotlib import pyplot as plt
from fabryka import Fabryka
from pelnomocnik import Pelnomocnik
from kupujacy import Kupujacy
from sortownia import Sortownia
from paczkomat import Paczkomat

fabryka = Fabryka()
sortownia = Sortownia()
paczkomat = Paczkomat("jeden", 10)
proxy = Pelnomocnik(fabryka, sortownia)
kupujacy = [Kupujacy("klient_"+str(i)) for i in range(20)]
# dodanie obserwatorów do paczkomatu
for k in kupujacy:
    paczkomat.dodaj_obserwatora(k)

historia_nadmiaru = []
historia_zamowien = []
for day in range(28):
    print("\n>dzien " + str(day+1))
    ile_przed = len(sortownia.nowepaczki)

    for k in kupujacy:
        k.zamow(proxy)

    historia_zamowien.append(len(sortownia.nowepaczki) - ile_przed)
    paczkomat.przyjmij_dostawe(sortownia)
    historia_nadmiaru.append(paczkomat.ile_w_magazynie)

fig, ax = plt.subplots()
X = list(range(len(historia_zamowien)))
ax.plot(X, historia_zamowien, color='g', label="zlozone zamowienia")
ax.plot(X, historia_nadmiaru, color='r', label="spoznione paczki")
ax.legend()
plt.show()
