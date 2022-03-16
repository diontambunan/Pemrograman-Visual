#Dion Sandy Ara Tambunan
#20051397056
#2020MIB

class jawaban :
    def rumus (angka): 
        print (' ')
        print ('Panjang alas : ', angka.bil1) 
        print ('Panjang tinggi : ', angka.bil2)
        print ('Panjang sisi A : ', angka.bil3)
        print ('Panjang sisi B : ', angka.bil4)
        print ('Panjang sisi C : ', angka.bil5)
        print (' ')
        print ('Luas segitiga adalah :', 1/2*angka.bil1*angka.bil2)
        print ('Keliling segitiga adalah :', angka.bil3+angka.bil4+angka.bil5)
class nilai(jawaban) :
    def __init__(self):
        self.bil1 = int(input('Masukan panjang alasnya : '))
        self.bil2 = int(input('Masukan panjang tingginya : '))
        self.bil3 = int(input('Masukan panjang sisi A : '))
        self.bil4 = int(input('Masukan panjang sisi B : '))
        self.bil5 = int(input('Masukan panjang sisi C : '))

confirm = ("y")
while confirm == ("y") :
    print ("Mencari Luas dan Keliling Segitiga")
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