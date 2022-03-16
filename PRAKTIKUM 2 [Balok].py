#Dion Sandy Ara Tambunan
#20051397056
#2020MIB

class jawaban :
    def rumus (angka): 
        print (' ')
        print ('Ukuran panjang : ', angka.bil1)
        print ('Ukuran lebar : ', angka.bil2)
        print ('Ukuran tinggi : ', angka.bil3)
        print (' ')
        print ('Volume balok adalah :', angka.bil1*angka.bil2*angka.bil3)
class nilai(jawaban) :
    def __init__(self) :
        self.bil1 = int(input('Masukan ukuran panjangnya : '))
        self.bil2 = int(input('Masukan ukuran lebarnya : '))
        self.bil3 = int(input('Masukan ukuran tingginya : '))

confirm = ("y")
while confirm == ("y") :
    print ("Mencari Volume Balok")
    objek = nilai()
    objek.rumus()
    print(" ")
    confirm = input("Apakah anda ingin memulai lagi? : ")
    if confirm == ("y") :
        print (" ")
        continue
    elif confirm == ("n") :
        break
    else :
        print ("Pilihan yang Anda inputkan salah!")
        break