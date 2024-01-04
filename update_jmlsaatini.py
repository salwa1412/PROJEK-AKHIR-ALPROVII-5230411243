import sqlite3
conn = sqlite3.connect('database_hewan1.db')
cursor = conn.cursor()

# Data yang ingin diubah
id_hewan = 1
jml_baru = 900

# Menjalankan query UPDATE
cursor.execute(f"UPDATE HEWAN SET jml_skrng = {jml_baru} WHERE id_hewan = {id_hewan}")
conn.commit()

# Menampilkan pesan setelah update berhasil
if cursor.rowcount > 0:
    print(f"Data hewan dengan ID {id_hewan} berhasil diupdate.")
else:
    print(f"Tidak ada data hewan dengan ID {id_hewan}.")

# Menutup koneksi
conn.close()
