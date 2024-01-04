import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()

# Menjalankan query SELECT dengan LIKE
nama = 'B%'  # Mencari nama yang dimulai dengan 'John'
kursor.execute(f"SELECT * FROM HEWAN WHERE nama_hewan LIKE ?", (nama,))
baris_table = kursor.fetchall()

print("Data Hewan:")
print("="*130)
print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<30}".format("ID HEWAN", "NAMA HEWAN", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN TERAKHIR DITEMUKAN"))
print("-"*130)
for row in baris_table:
    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<30}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
 
koneksi.close()
