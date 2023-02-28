from pkg_Jiva.modul1 import *
from pkg_Jiva.modul2 import *

def main():
    # memanggil funsi" dalam modul hiji
    f1()
    f2()
    # memanggil gunfsi modlu 2
    f3()
    f4()

main()
print("\n","="*15, " \n")
from pkg_Jiva.hitungNilai import *

NH = int(input("Nilai Harian:  "))
NU = int(input("Nilai Ulangan:  "))
nilai = hitung_nilai(NH, NU)
print(nilai)

from pkg_Jiva.myMODUL import *

print("="*15, " \n")

JenisMartabak(martabak1)
JenisMartabak(martabak2)