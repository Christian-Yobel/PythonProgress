import math
print('Soal 1')
# cara 1
def circle(r):
    print(f'lingkaran dengan radius {r} memiliki luas sebesar {math.pi * r**2}')
circle(int(input('Masukkan radius lingkaran: ')))

#cara 2
radius = int(input('Masukkan radius lingkaran: '))
area = lambda r : print(f'lingkaran dengan radius {r} memiliki luas sebesar {math.pi * r**2}')
result = area(radius)

#cara 3
x = (lambda r:print(f'lingkaran dengan r: {r}\nluasnya = {math.pi*int(r)**2}'))(input('Masukkan Radius: '))

print('\n')


print('Soal 2')
#cara 1
def oscar(**x):
    print(f'Actor {x['actor']} mendapatkan Oscar dari film {x['film']} di tahun {x['tahun']}')

oscar(actor = 'Emma Stone', film = 'La La Land', tahun = '2016')

#cara 2
def oscar2(actor, film, tahun):
    print(f'Actor {actor} mendapatkan Oscar dari film {film} di tahun {tahun}')

#cara 3
oscars = lambda a,f,y : print(f'Actor {a} mendapatkan Oscar dari film {f} di tahun {y}')
oscars('Cillian Murphy', 'Oppenheimer', '2023')

oscar2(actor = 'Emma Stone', film = 'La La Land', tahun = '2016')

print('\n')


print('Soal 3')
#cara 1
distance = [1,2,3,4,5]
print(list(map(lambda a: a*5000 + 8000, distance)))

#cara 2
def price(p):
    bayar = []
    for i in p:
        i = i*5000 + 8000
        bayar.append(i)
    return bayar
print(price(distance))    

print('\n')


print('Soal 4')
# Salah Objective
def parse(x):
    newList = []
    newerList = []
    if len(x.split()) > 2:
        for i in x:
            newList.append(i)
        for i in range(len(newList)):
            num = newList.pop()
            newerList.append(num)
    print(''.join(newerList))
                      
parse('namaku bento rumah real') 

#Cara 1
def parse2(x):
    newList = x.split()
    newerList = []
    for word in newList:
        if len(word) > 3:
            newerList.append(word[::-1])
        else:
            newerList.append(word)
    print(' '.join(newerList))

parse2('namaku bento rumah real est') 

#Cara 2
def wordRev(x):
    return x[::-1]

def wordsRev(sentence):
    newSentence = sentence.split()
    newList = []
    for i in newSentence:
        if len(i) > 3:
            newList.append(wordRev(i))
        else:
            newList.append(i)
    print(' '.join(newList))

wordsRev('namaku bento rumah real est the') 


print('\n')

print('Soal 1')
num = input('Masukkan Angka dipisah dengan koma: ')
numberSplitter = num.split(sep = ',')
print(list(map(lambda z : 'Genap' if int(z) % 2 == 0 else 'Ganjil', numberSplitter)))

print('Soal 2')
def gaji(x):
    if x * 0.95 > 9000000:
        return x

listGaji = [9100000,9800000, 9500000, 10300000, 9300000]

print(list(filter(gaji, listGaji)))

print('Soal 3')
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