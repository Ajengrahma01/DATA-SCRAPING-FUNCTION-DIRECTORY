jawab = 'lanjut'
while(True):
    Nama = input("Nama\t: ")
    Kelas = input("Kelas\t: ")
    NIM = input("NIM\t: ")
    print("==================")
    print("Nama\t: "+str(Nama))
    print("Kelas\t: "+str(Kelas))
    print("NIM\t: "+str(NIM))
    print("==================")
    jawab = input("Apakah lanjut input Data? ")
    if jawab == 'tidak':
        break