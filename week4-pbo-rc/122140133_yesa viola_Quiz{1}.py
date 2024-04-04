import random

class Minesweeper:
    def _init_(self, baris, kolom, jumlahBom):
        self.baris = baris
        self.kolom = kolom
        self.jumlahBom = jumlahBom
        self.papan = [['?' for _ in range(kolom)] for _ in range(baris)]
        self.lokasiBom = []
        self.menempatkanBom()

    def menempatkanBom(self):
        lokasiAwalBom = 0
        while lokasiAwalBom < self.jumlahBom:
            baris = random.randint(0, self.baris - 1)
            kolom = random.randint(0, self.kolom - 1)
            if (baris, kolom) not in self.lokasiBom:
                self.lokasiBom.append((baris, kolom))
                lokasiAwalBom += 1

    def cetakPapan(self):
        for baris in self.papan:
            print(" ".join(baris))

    def bukaKotak(self, baris, kolom):
        if (baris, kolom) in self.lokasiBom:
            self.papan[baris][kolom] = 'X'
            return False
        else:
            self.papan[baris][kolom] = 'O'
            return True

    def cekKemenangan(self):
        for baris in range(self.baris):
            for kolom in range(self.kolom):
                if self.papan[baris][kolom] == '?' and (baris, kolom) not in self.lokasiBom:
                    return False
        return True

def main():
    baris = 3
    kolom = 3
    jumlahBom = 3
    permainan = Minesweeper(baris, kolom, jumlahBom)

    while True:
        print("\nPapan saat ini:")
        permainan.cetakPapan()
        baris_input = int(input("Masukkan koordinat baris yang akan dibuka : "))
        kolom_input = int(input("Masukkan koordinat kolom yang akan  dibuka: "))

        if not (0 <= baris_input < permainan.baris) or not (0 <= kolom_input < permainan.kolom):
            print("Koordinat tidak valid. Coba lagi!!")
            continue

        if not permainan.bukaKotak(baris_input, kolom_input):
            print("Game Over! Anda telah menginjak bom!")
            break

        if permainan.cekKemenangan():
            print("Selamat! Anda menang permainan!")
            break

if _name_ == "_main_":
    main()
