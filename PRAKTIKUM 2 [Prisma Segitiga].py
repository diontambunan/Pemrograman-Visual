#Dion Sandy Ara Tambunan
#20051397056
#2020MIB

class jawaban :
    def rumus (angka): 
        print (' ')
        print ('Ukuran alas permukaan : ', angka.bil1)
        print ('Ukuran tinggi permukaan : ', angka.bil2)
        print ('Ukuran tinggi prisma : ', angka.bil3)
        print (' ')
        print ('Volume prisma segitiga adalah :', (1/2*angka.bil1*angka.bil2)*angka.bil3)

class nilai(jawaban) :
    def __init__(self):
      
        self.bil1 = int(input('Masukan ukuran alas permukaannya : '))
        self.bil2 = int(input('Masukan ukuran tinggi permukaannya : '))
        self.bil3 = int(input('Masukan ukuran tinggi prisma : '))

confirm = ("y")
while confirm == ("y") :
    print ("Mencari Volume Prisma Segitiga")
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