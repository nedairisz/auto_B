import jelszo
import oszthato
import autom

"""
print("Első feladat:")
jelszo.bekeres()

print("Második feladat:")
lista=oszthato.sorozat()
print(lista)
szamlalo=oszthato.ottel_oszthato(lista)
print(f"\tA listában {szamlalo} darab osztható szám van.")"""

print("III/Tabla:")
kocsi=autom.beolvas()
autom.tabla(kocsi[5])
print("III/Flotta:")
autom.flotta(kocsi)
print("III/Értékes:")
lf_index=autom.ertekes(kocsi)
print(f"\tA legfiatalabb autó: {kocsi[lf_index].nev} ({kocsi[lf_index].gyd})")
autom.kiiras(kocsi[5])
