import pandas as pd
import os
from tabulate import tabulate
import csv
import time
import datetime

fon = '''
░▒▓███████▓▒░ ░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░    ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     
░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     
░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░                                                                                              
'''

def utama():
    while True:
        os.system('cls')
        print(fon)
        print("\nPilih jenis akun untuk login:")
        print("[1] Admin")
        print("[2] User")
        print("-" * 40)
        try:
            akunUser = int(input("Masuk sebagai [1/2]: "))           
            if akunUser == 1:
                login_admin()
            elif akunUser == 2:
                login_user2()
            else:
                print("Input tidak sesuai, silakan coba lagi.")
                time.sleep(2)
                continue
        except ValueError:
            print('Pilihan harus berupa angka dan tidak boleh kosong')
            time.sleep(2)

def login_admin():
    os.system('cls')
    inputUser = input("Masukkan username Anda: ").rstrip().lower()
    inputPass = input('Masukkan password Anda: ').rstrip().lower()
    data = pd.read_csv('csv/dataAdmin.csv')
    user = data[(data['Username'] == inputUser) & (data['Password'] == inputPass)]
    if not user.empty:
        print("Selamat datang, Anda berhasil login sebagai Admin")
        time.sleep(2)
        halaman_admin()
    else:
        print("Username atau password salah, silakan coba lagi.")
        time.sleep(2)

def login_user2():
    os.system('cls')
    print('='*40)
    print('[1] Login User')
    print('[2] Daftar User')
    print('='*40)
    try:
        pilihan = int(input('Masukkan pilihan : '))
        if pilihan == 1:
            login_user()
        elif pilihan == 2:
            register()
        else:
            print('Pilihan tidak tersedia')
    except ValueError:
        print('Pilihan harus berupa angka & tidak boleh kosong')

def login_user():
    os.system('cls')
    global userInputh
    global userPassh
    print("=" *40)
    print(" LOGIN USER ".center(40))
    print("=" *40)
    userInputh = input("Masukkan username: ").rstrip().lower()
    userPassh = input("Masukkan password: ").rstrip().lower()
    print('='*40)
    data = pd.read_csv('csv/dataUser.csv')
    user = data[(data['Username'] == userInputh) & (data['Password'] == userPassh)]
    if not user.empty:
        print("Selamat datang, Anda berhasil login!")
        time.sleep(2)
        halaman_user()
    else:
        os.system('cls')
        print(f'Pengguna dengan username [{userInputh}], Password [{userPassh}] tidak ditemukan.')
        print("Ingin mendaftar atau mencoba lagi?")
        print('-'*40)
        print("[Enter] untuk mencoba lagi")
        print("[y] untuk mendaftar")           
        jawaban = input("Masukkan pilihan >>> ").strip().lower()
        if jawaban == 'y':
            register()
        elif jawaban == '':
            login_user()
        else:
            print("\nInput tidak sesuai, silakan coba lagi.")
            time.sleep(2)

def register():
    os.system('cls')
    print("=" * 40)
    print(" REGISTRASI AKUN ".center(40))
    print("=" * 40)
    username = input("Masukkan username: ").lower()
    password = input("Masukkan password: ").lower()
    data = pd.read_csv('csv/dataUser.csv')
    if username in data['Username'].values:
        print("Username sudah digunakan, silakan coba lagi.")
        time.sleep(2)
        register()
    else:
        saldo = 0
        hari = datetime.date.today()
        with open('csv/dataUser.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password, saldo, hari])
            print("\nSelamat, Anda telah berhasil terdaftar!")
            time.sleep(2)
        login_user()

def halaman_user():
    os.system('cls')
    data = pd.read_csv('csv/dataUser.csv')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    print('|| ^^^ 	     	   SELAMAT DATANG           ^^^  ||')
    print('||--------- Apa yang ingin anda lakukan?---------||')
    print('||                1. Lihat Profil                ||')
    print('||                2. Pemesanan                   ||')
    print('||                3. Cek Harga                   ||')
    print('||                4. Histori Pemesanan           ||')
    print('||                5. Keluhan                     ||')
    print('||                6. Log Out                     ||')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    pilihan = int(input("Masukan Pilihan Anda : "))
    if pilihan == 1:
        lihat_profil()

def lihat_profil():
    os.system('cls')
    print('='*40)
    print('LIHAT PROFIL'.center(40))
    print('='*40)
    data = pd.read_csv('csv/dataUser.csv')
    cek = data.loc[data['Username'] == userInputh]
    saldo = cek['Saldo'].values[0]
    print('BERIKUT INFORMASI ANDA')
    print(f'Username anda adalah = {userInputh}')
    print(f'Password anda adalah = {userPassh}')
    print(f'Sisa saldo anda adalah = Rp.{saldo}')
    print('='*40)
    input1 = input('Apakah Anda ingin mengubah password? (y/n) ')
    if input1 == 'y':
        a = input('Masukkan Password baru :')
        b = input('Masukkan Password baru lagi :')
        if a == b:
            data.loc[data['Username'] == userInputh, 'Password'] = b
            data.to_csv('csv/dataUser.csv', index=False)
            print('Password berhasil diubah')
            time.sleep(2)
            halaman_user()
        else:
            print('Password tidak sama')
            time.sleep(2)
            halaman_user()
    elif input1 == 'n':
        halaman_user()
    else:
        print('Mohon pilih pilihan yang valid')
        time.sleep(2)
    halaman_user()

def halaman_admin():
    os.system('cls')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    print('|| ^^^ 	     	   SELAMAT DATANG            ^^^ ||')
    print('||--------- Apa yang ingin anda lakukan?---------||')
    print('||                1. Kelola Mitra                ||')
    print('||                2. Kelola Barang               ||')
    print('||                3. Kelola kendaraan            ||')
    print('||                4. Kelola distribusi barang    ||')
    print('||                5. Kelola Pengguna             ||')
    print('||                6. Laporan                     ||')
    print('||                7. Log Out                     ||')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    try:
        pilihan = int(input("Masukan Pilihan Anda : "))
        if pilihan == 1:
            kelola_mitra()
        elif pilihan == 2:
            kelola_barang()
        elif pilihan == 5:
            kelola_user()
        elif pilihan == 6:
            utama()
        else:
            print('Pilihan tidak ada')
            time.sleep(2)
            halaman_admin()
    except ValueError:
        print('Pilihan harus angka & tidak boleh kosong!')

def kelola_barang():
    os.system('cls')
    global inputToko
    data = pd.read_csv('csv/dataMitra.csv')
    data.index = range(1, len(data)+1)
    print(tabulate(data,headers='keys', tablefmt='grid'))
    inputToko = input('Masukkan kode Toko : ').upper()
    if ((data['kode'] == inputToko) & (data['Status'] == 'Tersedia')).any():
        print('Toko terdeteksi, mengarahkan ke halaman...')
        time.sleep(2)
        menu_kelola_barang()
    else:
        print('Status tidak tersedia')
        time.sleep(2)

def menu_kelola_barang():
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    print('|| ^^^ 	     	   SELAMAT DATANG            ^^^ ||')
    print('||--------- Apa yang ingin anda lakukan?---------||')
    print('||                1. Tambah Barang               ||')
    print('||                2. Edit harga                  ||')
    print('||                3. Edit harga                  ||')
    print('||                4. Edit Stok                   ||')
    print('||                5. Keluar                      ||')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')


def kelola_mitra():
    os.system('cls')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    print('|| ^^^ 	     	   SELAMAT DATANG            ^^^ ||')
    print('||----- Berikut menu untuk mengelola mitra ------||')
    print('||                1. Cek Data mitra              ||')
    print('||                2. Tambah mitra                ||')
    print('||                3. Hapus mitra                 ||')
    print('||                4. Edit mitra                  ||')
    print('||                5. Kembali                     ||')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    pilihan = int(input("Masukan Pilihan Anda : "))
    if pilihan == 1:
        os.system('cls')
        data = pd.read_csv('csv/dataMitra.csv')
        data.index = range(1, len(data)+1)
        print(tabulate(data,headers='keys', tablefmt='grid'))
        input('Tekan enter untuk kembali>>>')
        kelola_mitra()
    elif pilihan == 2:
        kelola_mitra_Tambah()
    elif pilihan == 3:
        kelola_mitra_hapus()
    elif pilihan == 4:
        kelola_mitra_edit()
    elif pilihan == 5:
        halaman_admin()
    else:
        print('Tidak ada di pilihan')
        time.sleep(2)
        kelola_mitra()

def kelola_user():
    os.system('cls')    
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    print('|| ^^^ 	     	   SELAMAT DATANG            ^^^ ||')
    print('||----- Berikut menu untuk mengelola user ------||')
    print('||                1. Cek Data user              ||')
    print('||                2. Cek Data Admin             ||')
    print('||                3. Tambah user                ||')
    print('||                4. Tambah Admin               ||')
    print('||                5. Kembali                    ||')
    print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
    try:
        inputUser = int(input('Masukkan pilihan : '))
        if inputUser == 1:
            tampilkan_user()
        elif inputUser == 2:
            tampilkan_admin()
        elif inputUser == 3:
            tambah_user()
        elif inputUser == 4:
            tambah_admin()
        else:
            print('Pilihan tidak ada')
            time.sleep(1.5)
    except ValueError:
        print('Pilihan harus berupa angka & tidak boleh kosong')
        time.sleep(2)
        kelola_user()

def tampilkan_user():
    os.system('cls')
    df = pd.read_csv('csv/dataUser.csv')
    df.index = range(1, len(df)+1)
    print(tabulate(df.head(5),headers='keys', tablefmt='grid'))
    input('Tekan enter untuk kembali>>>')
    kelola_user()

def tampilkan_admin():
    os.system('cls')
    df = pd.read_csv('csv/dataAdmin.csv')
    df.index = range(1, len(df)+1)
    print(tabulate(df.head(5),headers='keys', tablefmt='grid'))
    input('Tekan enter untuk kembali>>>')
    kelola_user()
                    
def kelola_mitra_Tambah():
    os.system('cls')
    status = 'Tersedia'
    data = pd.read_csv('csv/dataMitra.csv')
    kodeMitra = input('Masukkan kode Mitra : ').upper()
    namaMitra = input('Masukkan nama Mitra : ').capitalize()
    alamatMitra = input('Masukkan lokasi Mitra : ').capitalize()
    kontakMitra = input('Masukkan kontak Mitra : ')
    if kodeMitra in data['kode'].values:
        print('Kode sudah ada, gunakan kode lain!')
        time.sleep(2)
        kelola_mitra_Tambah()
    else:
        with open('csv/dataMitra.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([kodeMitra,namaMitra,alamatMitra,kontakMitra,status])
        with open(f'csv/toko/{kodeMitra}.csv', 'w', newline='') as fil:
            writer2 = csv.writer(fil)
            writer2.writerow(['KodeBrg','NamaBrg','Harga','Stok'])
        print('Data anda berhasil ditambahkan...')
        time.sleep(2)
        kelola_mitra()

def kelola_mitra_edit():
    os.system('cls')
    data = pd.read_csv('csv/dataMitra.csv')
    data.index = range(1, len(data)+1)
    print(tabulate(data,headers='keys', tablefmt='grid'))
    print('KETIK "EXIT" UNTUK KEMBALI')
    kodeMitra = input('Masukkan kode toko yang ingin diubah : ').upper()
    if kodeMitra == 'EXIT':
        kelola_mitra()
    if kodeMitra in data['kode'].values:
        print('''Ingin mengubah bagian :
1. Nama
2. Lokasi
3. Kontak
4. Keluar''')
        try:
            inputUser = int(input('Masukkan pilihan : '))
            if inputUser == 1:
                inputNama = input('Masukkan nama baru : ')
                data.loc[data['kode'] == kodeMitra, 'Nama'] = inputNama
                data.to_csv('csv/dataMitra.csv',index=False)
                print('Nama berhasil diubah')
                time.sleep(2)
                kelola_mitra()
            elif inputUser == 2:
                inputLok = input('Masukkan lokasi baru : ')
                data.loc[data['kode'] == kodeMitra, 'Alamat'] = inputLok
                data.to_csv('csv/dataMitra.csv', index=False)
                print('Lokasi berhasil diubah...')
                time.sleep(2)
                kelola_mitra()
            elif inputUser == 3:
                inputKontak = input('Masukkan Kontak baru : ')
                data.loc[data['kode'] == kodeMitra, 'Kontak'] = inputKontak
                data.to_csv('csv/dataMitra.csv', index=False)
                print('Kontak berhasil diubah...')
                time.sleep(2)
                kelola_mitra()
            elif inputUser == 4:
                kelola_mitra()
            else:
                print('tidak ada di pilihan')
                time.sleep(2)
                kelola_mitra_edit()
        except ValueError:
            print('Pilihan harus berupa angka & tidak boleh kosong')
            time.sleep(2)
            kelola_mitra_edit()
    else:
        print('Tidak ada mitra dengan kode tersebut')
        time.sleep(2)
        kelola_mitra_edit()

def kelola_mitra_hapus():
    os.system('cls')
    data = pd.read_csv('csv/dataMitra.csv')
    data.index = range(1, len(data)+1)
    print(tabulate(data,headers='keys', tablefmt='grid'))
    print('KETIK "EXIT" UNTUK KEMBALI')
    hapusMitra = input('Masukkan kode mitra yang ingin dihapus : ').upper()
    if hapusMitra == 'EXIT':
        kelola_mitra()
    if os.path.exists(f'csv/toko/{hapusMitra}.csv'):
        konfirmasi = input('Apakah anda yakin ingin menghapus mitra [y][n] : ').lower()
        if konfirmasi == 'y':
            data.loc[data['kode'] == hapusMitra, 'Status'] = 'Tidak Aktif'
            data.to_csv('csv/dataMitra.csv', index=False)
            os.remove(f'csv/toko/{hapusMitra}.csv')
            print('Mitra berhasil dihapus...')
            time.sleep(2)
            kelola_mitra()
        elif konfirmasi == 'n':
            print('Penghapusan dibatalkan...')
            time.sleep(2)
            kelola_mitra_hapus()
        else:
            print('Pilihan tidak sesuai & tidak boleh kosong')
            time.sleep(2)
            kelola_mitra_hapus()
    else:
        print('Tidak ada mitra dengan kode tersebut')
        time.sleep(2)
        kelola_mitra_hapus()

def tambah_admin():
    os.system('cls')
    print('Anda masuk dalam menu tambah admin')
    print('Silahkan masukan data admin yang akan ditambahkan')
    adminUser = input('Masukkan username : ')
    adminPass = input('Masukkan Password : ')
    fileAda = os.path.exists('csv/dataAdmin.csv')
    with open('csv/dataAdmin.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if not fileAda:
            writer.writerow(['username','Password'])
        writer.writerow([adminUser,adminPass])
        print('data Admin berhasil ditambahkan')
        print('tekan enter untuk kembali>>>')
    halaman_admin()

def tambah_user():
    os.system('cls')
    saldo = 0
    adminUser = input('Masukkan username : ')
    adminPass = input('Masukkan Password : ')
    fileAda = os.path.exists('csv/dataUser.csv')
    with open('csv/dataUser.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if not fileAda:
            writer.writerow(['Username','Password'])
        writer.writerow([adminUser,adminPass,saldo])
        print('data User berhasil ditambahkan')
        input('tekan enter untuk kembali>>>')
    halaman_admin()

utama()