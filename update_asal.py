import sqlite3
conn = sqlite3.connect('database_hewan1.db')
cursor = conn.cursor()

# Data yang ingin diubah
id_hewan = 3

# Menjalankan query UPDATE
cursor.execute(f"UPDATE HEWAN SET asal = 'Nusa Tenggara Timur' WHERE id_hewan = {id_hewan}")
conn.commit()

# Menampilkan pesan setelah update berhasil
if cursor.rowcount > 0:
    print(f"Data hewan dengan ID {id_hewan} berhasil diupdate.")
else:
    print(f"Tidak ada data hewan dengan ID {id_hewan}.")

# Menutup koneksi
conn.close()
