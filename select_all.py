import sqlite3

conn = sqlite3.connect('database_hewan1.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM HEWAN")
rows = cursor.fetchall()

print("Data Hewan:")
print("="*130)
print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<30}".format("ID HEWAN", "NAMA HEWAN", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN TERAKHIR DITEMUKAN"))
print("-"*130)
for row in rows:
    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<30}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
 
conn.close()