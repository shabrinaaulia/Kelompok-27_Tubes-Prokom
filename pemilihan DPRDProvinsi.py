import json

# Fungsi untuk membaca data calon DPRD Provinsi dari file JSON
def baca_data_calon():
    with open("data_calon_DPRDProvinsi.json", "r") as file:
        data_calon_DPRDProvinsi = json.load(file)
    return data_calon_DPRDProvinsi

# Fungsi untuk menampilkan daftar calon DPRD Provinsi berdasarkan Provinsi
def tampilkan_daftar_calon(Provinsi, data_calon):
    print(f"Daftar Calon DPRD Provinsi {Provinsi}:")
    print("--------------------")

    for calon in data_calon[Provinsi]:
        print(f"Nomor Urut: {calon['nomor_urut']}")
        print(f"Nama Calon: {calon['nama']}")
        print("--------------------")

# Fungsi untuk mendapatkan input Provinsi dari pengguna
def input_Provinsi():
    Provinsi = input("Masukkan nama Provinsi Anda: ")
    return Provinsi

# Fungsi untuk mendapatkan input nomor urut calon dari pengguna
def input_nomor_urut():
    nomor_urut = input("Masukkan nomor urut calon DPRD Provinsi yang Anda pilih: ")
    return nomor_urut

# Fungsi untuk mendapatkan visi dan misi calon berdasarkan nomor urut
def get_visi_misi(nomor_urut, data_calon_DPRDProvinsi):
    visi = ""
    misi = ""

    for kota in data_calon_DPRDProvinsi:
        for calon in data_calon_DPRDProvinsi[kota]:
            if calon['nomor_urut'] == nomor_urut:
                visi = calon['visi']
                misi = calon['misi']
                break

    return visi, misi

# Fungsi untuk menjalankan program pemilihan DPRD Provinsi
def pemilihan_DPRDProvinsi():
    while True:
        print("Pemilihan DPRD Provinsi")
        print("--------------------")

        Provinsi = input_Provinsi()
        data_calon_DPRDProvinsi = baca_data_calon()

        if Provinsi in data_calon_DPRDProvinsi:
            tampilkan_daftar_calon(Provinsi, data_calon_DPRDProvinsi)

            nomor_urut = input_nomor_urut()

            visi, misi = get_visi_misi(nomor_urut, data_calon_DPRDProvinsi)

            print(f"Visi dan Misi Calon:")
            print("--------------------")
            print(f"Visi: {visi}")
            print(f"Misi: {misi}")
            print("--------------------")

            yakin = input("Apakah Anda yakin dengan pilihan Anda? (Ya/Tidak): ")
            if yakin.lower() != 'ya':
                continue

            print("Terima kasih atas partisipasi Anda dalam pemilihan DPRD Provinsi.")
            break
        else:
            print("Provinsi yang Anda masukkan tidak valid. Silakan coba lagi.")

# Menjalankan program pemilihan DPRD Provinsi
pemilihan_DPRDProvinsi() 