import json

# Fungsi untuk membaca data calon DPR dari file JSON 
def baca_data_calon():
    with open("data_calon DPR.json", "r") as file:
        data_calon_DPR = json.load(file)
    return data_calon_DPR

# Fungsi untuk menampilkan daftar calon DPR berdasrkan kota
def tampilkan_daftar_calon(Kota, data_calon):
    print(f"Daftar Calon DPR Kota {Kota}:")
    print("--------------------")

    for calon in data_calon[Kota]:
        print(f"Nomor Urut: {calon['nomor_urut']}")
        print(f"Nama Calon: {calon['nama']}")
        print("--------------------")

# Fungsi untuk mendapatkan input Kota dari pengguna
def input_Kota():
    Kota = input("Masukkan nama Kota Anda: ")
    return Kota

# Fungsi untuk mendapatkan input nomor urut calon dari pengguna
def input_nomor_urut():
    nomor_urut = input("Masukkan nomor urut calon DPR Kota yang Anda pilih: ")
    return nomor_urut

# Fungsi untuk mendapatkan visi dan misi calon berdasarkan nomor urut
def get_visi_misi(nomor_urut, data_calon_DPR):
    visi = ""
    misi = ""

    for kota in data_calon_DPR:
        for calon in data_calon_DPR[kota]:
            if calon['nomor_urut'] == nomor_urut:
                visi = calon['visi']
                misi = calon['misi']
                break

    return visi, misi

# Fungsi untuk menjalankan program pemilihan DPR 
def pemilihan_DPR():
    while True:
        print("Pemilihan DPR")
        print("--------------------")

        Kota = input_Kota()
        data_calon_DPR = baca_data_calon()

        if Kota in data_calon_DPR:
            tampilkan_daftar_calon(Kota, data_calon_DPR)

            nomor_urut = input_nomor_urut()

            visi, misi = get_visi_misi(nomor_urut, data_calon_DPR)

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

# Menjalankan program pemilihan DPR
pemilihan_DPR() 