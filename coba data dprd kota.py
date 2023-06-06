import csv

# Fungsi untuk membaca data calon DPRD Kota dari file
def baca_data_calon():
    with open("data_calon.csv", "r") as file:
        data_calon = csv.load(file)
    return data_calon

# Fungsi untuk menampilkan daftar calon DPRD Kota berdasarkan kota
def tampilkan_daftar_calon(kota, data_calon):
    print(f"Daftar Calon DPRD Kota {kota}:")
    print("--------------------")

    for calon in data_calon[kota]:
        print(f"Nomor Urut: {calon['nomor_urut']}")
        print(f"Nama Calon: {calon['nama']}")
        print("--------------------")

# Fungsi untuk mendapatkan input kota dari pengguna
def input_kota():
    kota = input("Masukkan nama kota Anda: ")
    return kota

# Fungsi untuk mendapatkan input nomor urut calon dari pengguna
def input_nomor_urut():
    nomor_urut = input("Masukkan nomor urut calon DPRD Kota yang Anda pilih: ")
    return nomor_urut

# Fungsi untuk mendapatkan visi dan misi calon berdasarkan nomor urut
def get_visi_misi(nomor_urut, data_calon):
    visi = ""
    misi = ""

    for kota in data_calon:
        for calon in data_calon[kota]:
            if calon['nomor_urut'] == nomor_urut:
                visi = calon['visi']
                misi = calon['misi']
                break

    return visi, misi

# Fungsi untuk menjalankan program pemilihan DPRD Kota
def pemilihan_dprd_kota():
    while True:
        print("Pemilihan DPRD Kota")
        print("--------------------")

        kota = input_kota()
        data_calon = baca_data_calon()

        if kota in data_calon:
            tampilkan_daftar_calon(kota, data_calon)

            nomor_urut = input_nomor_urut()

            visi, misi = get_visi_misi(nomor_urut, data_calon)

            print(f"Visi dan Misi Calon:")
            print("--------------------")
            print(f"Visi: {visi}")
            print(f"Misi: {misi}")
            print("--------------------")

            yakin = input("Apakah Anda yakin dengan pilihan Anda? (Ya/Tidak): ")
            if yakin.lower() != 'y':
                continue

            print("Terima kasih atas partisipasi Anda dalam pemilihan DPRD Kota.")
            break
        else:
            print("Kota yang Anda masukkan tidak valid. Silakan coba lagi.")

pemilihan_dprd_kota()
