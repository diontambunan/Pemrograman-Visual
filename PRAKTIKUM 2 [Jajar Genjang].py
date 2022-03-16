#Dion Sandy Ara Tambunan
#20051397056
#2020MIB

class jawaban :
    def rumus (angka): 
        print (' ')
        print ('Panjang alas : ', angka.bil1)
        print ('Panjang tinggi : ', angka.bil2)
        print (' ')
        print ('Luas jajar genjang adalah :', angka.bil1*angka.bil2)
        print ('Keliling jajar genjang adalah :', 2*(angka.bil1+angka.bil2))
class nilai(jawaban) :
    def __init__(self):
        self.bil1 = int(input('Masukan panjang alasnya : '))
        self.bil2 = int(input('Masukan panjang tingginya : '))

confirm = ("y")
while confirm == ("y") :
    print ("Mencari Luas Jajar Genjang")
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