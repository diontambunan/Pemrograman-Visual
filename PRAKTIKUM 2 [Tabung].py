#Dion Sandy Ara Tambunan
#20051397056
#2020MIB

class jawaban :
    def rumus (angka): 
        print (' ')
        print ('Ukuran jari-jari : ', angka.bil1)
        print ('Ukuran tinggi : ', angka.bil2)
        print (' ')
        print ('Volume tabung adalah :', 22/7*angka.bil1*angka.bil1*angka.bil2)
class nilai(jawaban) :
    def __init__(self):
        self.bil1 = int(input('Masukan ukuran jari-jari : '))
        self.bil2 = int(input('Masukan ukuran tingginya : '))

confirm = ("y")
while confirm == ("y") :
    print ("Mencari Volume Tabung")
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