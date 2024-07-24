print('Soal1')

list1 = input('Masukkan 5 film kesukaan anda (dipisahkan dengan koma): ').split(sep = ',')
yourFav = set(list1)

list2 = input('Masukkan 5 film kesukaan teman anda (dipisahkan dengan koma): ').split(sep = ',')
otherFav = set(list2)

percentage = len(yourFav.intersection(otherFav))*2/(len(yourFav) + len(otherFav)) * 100
print(f'Kesukaan film kalian yang sama sebesar {percentage}%')

print('\n')


print('Soal 2')

# Dictionary utama
header = ['Index', 'Nama', 'Stock', 'Harga']
motherDict = {'nama' : ['Apel', 'Jeruk', 'Anggur', 'Pepaya'],
              'stock' : [20, 15, 25, 30], 
              'harga' : [ 10000, 15000, 20000, 5000]}

def menu():
    return input('''
Selamat Datang di Pasar Buah

List Menu:
1. Menampilkan Daftar Buah 
2. Menambah Buah 
3. Menghapus Buah 
4. Membeli Buah 
5. Exit Program

Masukkan Angka Menu Yang Ingin Dijalankan: ''')

def program1():
    # Print Daftar Buah
    print('\nDaftar Buah\n')
    # Print Header
    print(' | '.join(item.ljust(15, ' ') for item in header))
    # Print Buah
    index = 0
    for i in range(len(motherDict['nama'])):
        row = [str(i)]
        for key in motherDict.keys():
            row.append(str(motherDict[key][index]))
        print(' | '.join(item.ljust(15, ' ') for item in row))
        index += 1

def program2():
    # Menambah Buah
    a0 = input('Masukkan Nama Buah     : ')
    a1 = int(input('Masukkan stock Buah    : '))
    a2 = int(input('Masukkan Harga Buah    : '))
    motherDict['nama'].append(a0)
    motherDict['stock'].append(a1)
    motherDict['harga'].append(a2)

def program3():
    # Menghapus Buah
    program1()
    id = int(input('Masukkan Index buah yang inging dihapus: '))
    for k, v in motherDict.items():
        motherDict[k].pop(id)

def program4():
    # Membeli Buah
    cart = [[],[],[],[]]
    total = 0
    while True:
        program1()
        b0 = input('Masukkan Index buah yang ingin dibeli: ')
        b0 = inputChecker(b0)
        if b0 == 'continue': continue
        if b0 not in range(len(motherDict['nama'])):
            print('Index diluar dari buah yang tersedia')
            continue

        b1 = input('Masukkan jumlah yang ingin dibeli: ')
        b1 = inputChecker(b1)
        if b1 == 'continue': continue

        if motherDict['stock'][b0] < int(b1):
            print(f'Stock tidak cukup, stock {motherDict['nama'][b0]} tinggal {motherDict['stock'][b0]}')
        else:
            harga = b1 * motherDict['harga'][b0]
            cart[0].append(motherDict['nama'][b0])
            cart[1].append(b1)
            cart[2].append(motherDict['harga'][b0])
            cart[3].append(harga)
            motherDict['stock'][b0] = motherDict['stock'][b0] - b1
            total += harga
        
        print('Isi Cart:')
        atas = ['Index', 'Nama', 'Belanjaan', 'Harga Satuan', 'Harga Total']
        print(' | '.join(item.ljust(15, ' ') for item in atas))
        for i in range(len(cart[0])):
            row = [str(i)]
            for j in range(len(cart)):
                row.append(str(cart[j][i]))
            print(' | '.join(item.ljust(15, ' ') for item in row))
        userInput = input('Mau beli yang lain (ya/tidak) = ')
        if userInput.lower() == 'tidak':
            break
        elif userInput.lower() == 'ya':
            continue
        else:
            print('Input tidak sesuai. Hanya menerima (ya/tidak)')

    print(f'Total yang harus dibayar = {total}')
    if total != 0:
        bayar = int(input('Masukkan Jumlah Uang: '))

        while bayar < total:
            print(f'Uang Anda Kurang Sebesar {total-bayar}')
            bayar = int(input('Masukkan Jumlah Uang: '))
        if bayar > total:
            print(f'Terima Kasih \n \nUang Kembali Anda {bayar-total}')
        else:
            print('Terima Kasih')

def inputChecker(x):
    if x.isnumeric():
        return int(x)
    else:
        print('Input hanya menerima angka')
        return 'continue'

programMap = {'1' : program1, '2' : program2, '3' : program3, '4' : program4}

while True:
    program = menu()

    if program == '5':
        print('Exiting Program....\nExit')
        break

    if program in programMap:
        programMap[program]()
    else:
        print('Input Invalid, Tidak Sesuai Dengan Menu Yang Tersedia')

import math
print('Soal 1')
def circle(r):
    return math.pi * r**2
# x = lambda input('Masukkan Radius: ') : math.pi*a**2
print(circle(5))


print('Soal 1')
# def change(*x):
#     for i in x:
#         if i % 2 == 0:
#             print(i)
# change = lambda *z : 'Genap' if z%2 == 0 else 'Ganjil'
num = input('Masukkan Angka dipisah dengan koma: ')
numberSplitter = num.split(sep = ',')
print(list(map(lambda z : 'Genap' if int(z) % 2 == 0 else 'Ganjil', numberSplitter)))