import psycopg2

# PASIEN
conn = psycopg2.connect(
    host="localhost",       
    database="KlinikGigi",  
    user="postgres",        
    password="1"  
)

# Membuat cursor untuk mengeksekusi perintah SQL
cur = conn.cursor()

# Menjalankan query untuk mengambil semua data dari tabel pasien
cur.execute("SELECT * FROM pasien")

# Mengambil semua hasil query
rows = cur.fetchall()

# Menampilkan hasil
print("Data Pasien:")
for row in rows:
    print(row)

# Menutup koneksi
cur.close()
conn.close()


# DOKTER
conn = psycopg2.connect(
    host="localhost",         # Ganti jika host bukan localhost
    database="KlinikGigi",  # Ganti dengan nama database kamu
    user="postgres",          # Ganti jika username bukan postgres
    password="1"     # Ganti dengan password PostgreSQL kamu
)

# Membuat cursor untuk menjalankan SQL
cur = conn.cursor()

# Menjalankan query untuk mengambil semua data dari tabel dokter
cur.execute("SELECT * FROM dokter")

# Mengambil semua hasil query
rows = cur.fetchall()

# Menampilkan hasil
print("Data Dokter:")
for row in rows:
    print(row)

# Menutup koneksi
cur.close()
conn.close()

#STAFF
conn = psycopg2.connect(
    host="localhost",         # Ganti sesuai host PostgreSQL
    database="KlinikGigi",  # Ganti dengan nama database kamu
    user="postgres",          # Ganti jika bukan user default
    password="1"     # Ganti dengan password kamu
)

# Membuat cursor
cur = conn.cursor()

# Menjalankan query untuk mengambil semua data dari tabel staff
cur.execute("SELECT * FROM staff")

# Mengambil semua data
rows = cur.fetchall()

# Menampilkan data
print("Data Staff:")
for row in rows:
    print(row)

# Menutup koneksi
cur.close()
conn.close()

#RESERVASI
conn = psycopg2.connect(
    host="localhost",         # Ganti jika bukan localhost
    database="KlinikGigi",  # Ganti dengan nama database kamu
    user="postgres",          # Ganti dengan user PostgreSQL kamu
    password="1"     # Ganti dengan password kamu
)

# Membuat cursor
cur = conn.cursor()

# Menjalankan query untuk mengambil semua data dari tabel reservasi
cur.execute("SELECT * FROM reservasi")

# Mengambil semua hasil
rows = cur.fetchall()

# Menampilkan data
print("Data Reservasi:")
for row in rows:
    print(row)

# Menutup koneksi
cur.close()
conn.close()

#LAYANAN
conn = psycopg2.connect(
    host="localhost",         # Ganti jika bukan localhost
    database="KlinikGigi",  # Ganti dengan nama database kamu
    user="postgres",          # Ganti dengan user PostgreSQL kamu
    password="1"     # Ganti dengan password kamu
)

# Membuat cursor
cur = conn.cursor()

# Menjalankan query untuk mengambil semua data dari tabel layanan
cur.execute("SELECT * FROM layanan")

# Mengambil semua hasil
rows = cur.fetchall()

# Menampilkan data
print("Data Layanan:")
for row in rows:
    print(row)

# Menutup koneksi
cur.close()
conn.close()

#TRANSAKSI
conn = psycopg2.connect(
    host="localhost",           # Ganti jika host bukan localhost
    database="KlinikGigi",    # Ganti dengan nama database kamu
    user="postgres",            # Ganti jika user berbeda
    password="1"       # Ganti dengan password kamu
)

# Membuat cursor
cur = conn.cursor()

# Menjalankan query untuk mengambil semua data dari tabel transaksi
cur.execute("SELECT * FROM transaksi")

# Mengambil semua hasil
rows = cur.fetchall()

# Menampilkan hasil
print("Data Transaksi:")
for row in rows:
    print(row)

# Menutup koneksi
cur.close()
conn.close()

#REKAM MEDIS
conn = psycopg2.connect(
    host="localhost",           # Ganti jika bukan localhost
    database="KlinikGigi",    # Ganti dengan nama database kamu
    user="postgres",            # Ganti dengan user PostgreSQL kamu
    password="1"       # Ganti dengan password PostgreSQL kamu
)

# Membuat cursor
cur = conn.cursor()

# Menjalankan query untuk mengambil semua data dari tabel rekam_medis
cur.execute("SELECT * FROM rekam_medis")

# Mengambil semua hasil
rows = cur.fetchall()

# Menampilkan data
print("Data Rekam Medis:")
for row in rows:
    print(row)

# Menutup koneksi
cur.close()
conn.close()

#STATUS PEMBAYARAN
conn = psycopg2.connect(
    host="localhost",           # Ganti jika bukan localhost
    database="KlinikGigi",    # Ganti dengan nama database kamu
    user="postgres",            # Ganti jika user bukan postgres
    password="1"       # Ganti dengan password PostgreSQL kamu
)

# Membuat cursor
cur = conn.cursor()

# Menjalankan query untuk mengambil semua data dari tabel status_pembayaran
cur.execute("SELECT * FROM status_pembayaran")

# Mengambil semua hasil
rows = cur.fetchall()

# Menampilkan data
print("Data Status Pembayaran:")
for row in rows:
    print(row)

# Menutup koneksi
cur.close()
conn.close()

#OBAT SAMPAI OBAT REKAM MEDIS BELUM, MINTA TOLONG LANJUTIN YA