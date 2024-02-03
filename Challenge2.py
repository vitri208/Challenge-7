print('<<<    Identifikasi Bilangan   >>>')
print('Identifikasi nilai jika nilai 10-15 atau nilai 20-25 atau 35-40')
print('-'*20)

while True:
    Bilangan = int(input("Masukkan bilangan: "))

    if (10 < Bilangan < 15) or (20 < Bilangan < 25) or (35 < Bilangan < 40):
        print("Bilangan Benar!")
        break
    else:
        print("Bilangan Salah")