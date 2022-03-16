# Anggelina Kismasari 20051397034 2020MIB

class jawaban :
    def rumus (angka): 
        print (' ')
        print ('Panjang sisi : ', angka.bil1) 
        print (' ')
        print ('Luas persegi adalah :', angka.bil1*angka.bil1)
        print ('Keliling persegi adalah :', angka.bil1+angka.bil1+angka.bil1+angka.bil1)
class nilai(jawaban) :
    def __init__(self):
        self.bil1 = int(input('Masukan panjang sisinya : '))

confirm = ("y")
while confirm == ("y") :
    print ("Mencari Luas dan Keliling Persegi")
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