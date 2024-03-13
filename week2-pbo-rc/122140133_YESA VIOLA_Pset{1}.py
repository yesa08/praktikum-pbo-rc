import random

class OrangTua:
    def __init__(self, tipe_darah):
        self.tipe_darah = tipe_darah

class Anak:
    def __init__(self, ayah, ibu):
        if 'AB' in ayah.tipe_darah and 'B' in ibu.tipe_darah and 'O' in ibu.tipe_darah:
            self.alel_ayah = 'B'
            self.alel_ibu = 'O'
        else:
            self.alel_ayah = random.choice(ayah.tipe_darah)
            self.alel_ibu = random.choice(ibu.tipe_darah)

    def tentukan_tipe_darah(self):
        alel_anak = [self.alel_ayah, self.alel_ibu]

        if 'AB' in alel_anak:
            return 'AB'
        elif 'A' in alel_anak and 'B' in alel_anak:
            return 'AB'
        elif 'A' in alel_anak and 'O' in alel_anak:
            return 'A'
        elif 'B' in alel_anak and 'O' in alel_anak:
            return 'B'
        elif 'O' in alel_anak:
            return 'O'
        else:
            return 'Alel tidak valid'

def validasi_tipe_darah(tipe_darah):
    if tipe_darah.upper() not in ['A', 'B', 'AB', 'O']:
        return False
    return True


tipe_darah_ayah = input("Masukkan tipe darah ayah (A, B, AB, atau O): ")
while not validasi_tipe_darah(tipe_darah_ayah):
    print("Tipe darah tidak valid!")
    tipe_darah_ayah = input("Masukkan tipe darah ayah (A, B, AB, atau O): ")

tipe_darah_ibu = input("Masukkan tipe darah ibu (A, B, AB, atau O): ")
while not validasi_tipe_darah(tipe_darah_ibu):
    print("Tipe darah tidak valid!")
    tipe_darah_ibu = input("Masukkan tipe darah ibu (A, B, AB, atau O): ")

ayah = OrangTua(tipe_darah_ayah)
ibu = OrangTua(tipe_darah_ibu)
anak = Anak(ayah, ibu)
tipe_darah_anak = anak.tentukan_tipe_darah()

print("Alel anak:", anak.alel_ayah + anak.alel_ibu)
print("Tipe darah anak:", tipe_darah_anak)
