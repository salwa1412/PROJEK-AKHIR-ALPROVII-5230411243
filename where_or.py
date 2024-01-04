import sqlite3

koneksi = sqlite3.connect('database_hewan1.db')
kursor = koneksi.cursor()

kursor.execute(f"SELECT * FROM HEWAN WHERE asal = 'Sumatera' OR jml_skrng >= '500'")
baris_table = kursor.fetchall()

print("Data Hewan:")
print("="*130)
print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<30}".format("ID HEWAN", "NAMA HEWAN", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN TERAKHIR DITEMUKAN"))
print("-"*130)
for row in baris_table:
    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<30}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
 

koneksi.close()
