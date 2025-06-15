import psycopg2
import os
import pandas as pd
import time
import datetime
from tabulate import tabulate

def connectDb():
    conn = psycopg2.connect(database='KlinikGigi', user='postgres',password='1',host='localhost',port=5432)
    curr = conn.cursor()
    return conn, curr

def clear():
    os.system('cls')

def postgre_cls(conn, cur):
    cur.close()
    conn.close()

def utama():
    clear()
    print("SELAMAT DATANG DI KLINIK GIGI BERSAMA")
    print("1. Login")
    print("2. Register")
    pilihanUser = input("Masukkan Pilihan : ")
    if pilihanUser == "1":
        loginUser()
    elif pilihanUser == "2":
        registerUser()
    else:
        print("Tidak ada dipilihan")
        time.sleep(2)
        utama()

def loginUser():
    clear()
    global username
    print("SELAMAT DATANG DI FITUR LOGIN")
    username = input('Masukkan Username : ')
    password = input('Masukkan password : ')
    conn, cur = connectDb()
    cur.execute(f"SELECT * FROM pasien WHERE username = %s and password = %s", (username, password))
    is_pasien = cur.fetchone()
    cur.execute(f"SELECT * FROM dokter WHERE username = %s and password = %s", (username, password))
    is_dokter = cur.fetchone()
    cur.execute(f"SELECT * FROM staff WHERE username = %s and password = %s", (username, password))
    is_staff = cur.fetchone()
    postgre_cls(conn, cur)
    if is_pasien:
        print(f'Selamat datang! pasien {username}')
        time.sleep(2)
        pasien()
    elif is_dokter:
        print(f'Selamat datang! dokter {username}')
        time.sleep(2)
        dokter()
    elif is_staff:
        print(f'Selamat datang! staff {username}')
        time.sleep(2)
        staff()
    else:
        print('Akun tidak ditemukan!')
        time.sleep(2)
        loginUser()
        postgre_cls(conn, cur)

def registerUser():
    clear()
    nama = input('Masukkan nama lengkap : ')
    print('''1. Laki-Laki
2. Perempuan''')
    kelamin = input('Jenis kelamin : ')
    if kelamin == '1':
        kelamin = 'Laki-Laki'
    elif kelamin == '2':
        kelamin = 'Perempuan'
    tanggal = input('Masukkan tanggal lahir [yyyy-mm-dd]: ')
    telepon = input('Masukkan nomor telepon : ')
    user = input('Username : ')
    passw = input('Password : ')
    conn, cur = connectDb()
    query = (f'INSERT INTO pasien(nama_pasien,jenis_kelamin,tanggal_lahir,no_telepon,username,password) VALUES (%s, %s, %s, %s, %s, %s)')
    values = (nama, kelamin, tanggal, telepon, user, passw)
    cur.execute(query, values)
    conn.commit()
    print('Berhasil register!')
    time.sleep(2)
    postgre_cls(conn, cur)
    loginUser()


def pasien():
    clear()
    conn, cur = connectDb()
    query = 'SELECT nama_pasien FROM pasien WHERE username = %s'
    cur.execute(query, (username,))
    hasil = cur.fetchone()
    if hasil:  
        nama_pasien = hasil[0]
        print(f'=====HALO PASIEN {nama_pasien}=====')
    else:
        print('Pasien tidak ditemukan.')
    print('''1. Lihat Profil
2. Reservasi
3. Cek reservasi
4. Cek dokter
5. Keluar''')
    while True:
        pilihanPasien = input('Masukkan pilihan : ')
        if pilihanPasien == '1':
            lihatProfil()
        elif pilihanPasien == '2':
            reservasi()
        elif pilihanPasien == '3':
            cekReservasi()
        elif pilihanPasien == '4':
            cekDokter()
        elif pilihanPasien == '5':
            loginUser()
        else:
            print('Tidak ada dipilihan')
            time.sleep(2)
            return
        break
        
def lihatProfil():
    clear()
    conn, cur = connectDb()
    queryNama = 'SELECT nama_pasien FROM pasien WHERE username = %s'
    cur.execute(queryNama, (username,))
    hasilNama = cur.fetchone()[0]
    queryKelamin = 'SELECT jenis_kelamin FROM pasien WHERE username = %s'
    cur.execute(queryKelamin, (username,))
    hasilKelamin = cur.fetchone()[0]
    queryTanggal = 'SELECT tanggal_lahir FROM pasien WHERE username = %s'
    cur.execute(queryTanggal, (username,))
    hasilTanggal = cur.fetchone()[0]
    queryTelepon = 'SELECT no_telepon FROM pasien WHERE username = %s'
    cur.execute(queryTelepon, (username,))
    hasilTelepon = cur.fetchone()[0]
    while True:
        print('=====BERIKUT INFORMASI AKUN ANDA=====')
        print(f'NAMA LENGKAP : {hasilNama}')
        print(f'JENIS KELAMIN : {hasilKelamin}')
        print(f'TANGGAL LAHIR : {hasilTanggal}')
        print(f'TANGGAL LAHIR : {hasilTelepon}')
        input('TEKAN ENTER UNTUK KEMBALI')
        break
    pasien()

def reservasi():
    clear()
    conn, cur = connectDb()

def cekReservasi():
    clear()
    conn, cur = connectDb()
    query = '''select r.tanggal_kunjungan, p.nama_pasien, l.nama_layanan, d.nama_dokter
from reservasi r
JOIN pasien p on r.id_pasien = p.id_pasien
JOIN layanan l on r.id_layanan = l.id_layanan
JOIN dokter d on d.id_dokter = r.id_dokter
WHERE p.username = %s'''
    cur.execute(query, (username,))
    data = cur.fetchall()
    if data:
        tabel = pd.DataFrame(data, columns=["tanggal Kunjungan", "nama pasien", "layanan", "Dokter menangani"])
        tabel.index = range(1, len(tabel)+1)
        print(tabulate(tabel, headers='keys',tablefmt='grid'))
        input('TEKAN ENTER UNTUK KEMBALI >>>')
        pasien()
    else:
        print('Belum ada data!')
        time.sleep(2)
    postgre_cls(conn, cur)
    pasien()

def cekDokter():
    clear()
    conn, cur = connectDb()
    query = 'SELECT nama_dokter,no_telepon FROM dokter'
    cur.execute(query)
    data = cur.fetchall()
    tabel = pd.DataFrame(data, columns=["Nama Dokter", "Nomor Telepon dokter"])
    tabel.index = range(1, len(tabel)+1)
    print(tabulate(tabel, headers='keys',tablefmt='grid'))
    input('TEKAN ENTER UNTUK KEMBALI >>>')
    postgre_cls(conn, cur)
    pasien()


def dokter():
    clear()

def staff():
    clear()


utama()