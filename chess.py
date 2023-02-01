def oyun_alani_olusturma():
    oyun_alani = []

    for satir in range(8):
        satir_liste = []
        oyun_alani.append(satir_liste)
        for sutun in range(8):
            satir_liste.append(" ")

    return oyun_alani


def karakter_yerlestirme(oyun_alani):
    for buyuk_piyon in range(8):
        oyun_alani[6][buyuk_piyon] = "P"

    diger_karakterler_buyuk = ["K", "A", "F", "V", "Ş", "F", "A", "K"]

    for karakter_index in range(8):
        oyun_alani[7][karakter_index] = diger_karakterler_buyuk[karakter_index]

    for kucuk_piyon in range(8):
        oyun_alani[1][kucuk_piyon] = "p"

    diger_karakterler_kucuk = ["k", "a", "f", "v", "ş", "f", "a", "k"]

    for karakter_index_2 in range(8):
        oyun_alani[0][karakter_index_2] = diger_karakterler_kucuk[karakter_index_2]


def oyun_alani_yazdirma(oyun_alani):
    print("    A", "  B", "  C", "  D", "  E", "  F", "  G", "  H")

    for satir_index in range(8):
        print("  ---------------------------------")

        for sutun_index in range(8):
            if sutun_index == 0:
                print(f"{8 - satir_index}", end="")
            if sutun_index == 7:
                print(f" |", oyun_alani[satir_index][sutun_index], f"| {8 - satir_index}")
            else:
                print(" |", oyun_alani[satir_index][sutun_index], end="")

    print("  ---------------------------------")
    print("    A", "  B", "  C", "  D", "  E", "  F", "  G", "  H")


def hareket_dogrultusu_alma():
    mevcut_konum = input("mevcut konumu giriniz: ")
    gidilecek_konum = input("gidilecek konumu giriniz: ")

    return mevcut_konum, gidilecek_konum


def hareket_yeme_algoritmasi(oyun_alani, mevcut_konum, gidilecek_konum, konum_sozlugu):
    mevcut_satir_index = 8 - int(mevcut_konum[0])
    mevcut_sutun_index = konum_sozlugu[mevcut_konum[1]]

    gidilecek_satir_index = 8 - int(gidilecek_konum[0])
    gidilecek_sutun_index = konum_sozlugu[gidilecek_konum[1]]

    if oyun_alani[gidilecek_satir_index][gidilecek_sutun_index] != " ":
        oyun_alani[gidilecek_satir_index][gidilecek_sutun_index] = " "

    oynanan_tas = oyun_alani[mevcut_satir_index][mevcut_sutun_index]
    oyun_alani[mevcut_satir_index][mevcut_sutun_index] = " "
    oyun_alani[gidilecek_satir_index][gidilecek_sutun_index] = oynanan_tas


def main():
    konum_sozlugu = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    a = oyun_alani_olusturma()
    karakter_yerlestirme(a)
    c = True
    while c == True:
        oyun_alani_yazdirma(a)
        print()
        b = list(hareket_dogrultusu_alma())
        hareket_yeme_algoritmasi(a, b[0], b[1], konum_sozlugu)


main()
