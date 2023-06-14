import csv
import sys

# Inisialisasi stack untuk melacak menu-menu yang dikunjungi
menu_stack = []

def load_data(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            try:
                header = next(reader)
            except StopIteration:
                print("File CSV kosong atau tidak memiliki header yang sesuai.")
                return [], data
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return [], data
    return header, data

def save_data(filename, header, data):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)
    except IOError:
        print("Terjadi kesalahan saat menyimpan data.")

def check_duplicate_data(data, new_data):
    for row in data:
        if row[:3] == new_data:
            return True
    return False

def input_data(data):
    asal = input("Masukkan Asal: ")
    NIK = input("Masukkan NIK: ")
    nama = input("Masukkan Nama: ")

    new_data = [asal, NIK, nama]

    if check_duplicate_data(data, new_data):
        print("Data sudah digunakan sebelumnya. Silakan input data lagi.")
        return

    data.append(new_data)
    print("Data berhasil disimpan.")

def main():
    filename = "data_pemilih.csv"
    header, data = load_data(filename)

    while True:
        print("\nMenu:")
        print("============SELAMAT DATANG DI MENU UTAMA PROGRAM PEMILU=============")
        print("1. Input Data Diri")
        print("2. Sudah Input Data Diri")
        print("3. Pemilihan DPRD Kota")
        print("4. Pemilihan DPRD Provinsi")
        print("5. Pemilihan DPD")
        print("6. Pemilihan DPR")
        print("7. Kembali ke Menu Sebelumnya")
        print("8. Exit")
        choice = input("Pilih menu (1/2/3/4/5/6/7/8): ")

        if choice == "1":
            # Tambahkan menu saat ini ke stack
            menu_stack.append(main)
            input_data(data)
        elif choice == "2":
            save_data(filename, header, data)
            break
        elif choice == "3":
            # Tambahkan menu saat ini ke stack
            menu_stack.append(main)
            pemilihan_dprd_kota()
        elif choice == "4":
            # Tambahkan menu saat ini ke stack
            menu_stack.append(main)
            pemilihan_DPRDProvinsi()
        elif choice == "5":
            # Tambahkan menu saat ini ke stack
            menu_stack.append(main)
            pemilihan_DPD()
        elif choice == "6":
            # Tambahkan menu saat ini ke stack
            menu_stack.append(main)
            pemilihan_DPR()
        elif choice == "7":
            # Cek apakah ada menu sebelumnya yang dapat dikembalikan
            if menu_stack:
                previous_menu = menu_stack.pop()
                previous_menu()
            else:
                print("Tidak ada menu sebelumnya yang dapat dikembalikan.")
        elif choice == "8":
            save_data(filename, header, data)
            print("Terima Kasih! Program selesai.")
            sys.exit()
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()


# Fungsi untuk membaca data calon DPRD Kota dari file JSON
import json

def baca_data_calon():
    try:
        with open("data_calon_dprd_kota.json", "r") as file:
            data_calon_dprd_kota = json.load(file)
        return data_calon_dprd_kota
    except FileNotFoundError:
        print("File data_calon_dprd_kota.json tidak ditemukan.")
        return {}

# Fungsi untuk menampilkan daftar calon DPRD Kota berdasarkan Kota
def tampilkan_daftar_calon(Kota, data_calon):
    if Kota not in data_calon:
        print(f"Tidak ada data calon DPRD Kota {Kota}.")
        return

    print(f"Daftar Calon DPRD Kota {Kota}:")
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
    nomor_urut = input("Masukkan nomor urut calon DPRD Kota yang Anda pilih: ")
    return nomor_urut

# Fungsi untuk mendapatkan visi dan misi calon berdasarkan nomor urut
def get_visi_misi(nomor_urut, data_calon_dprd_kota):
    visi = ""
    misi = ""

    for kota in data_calon_dprd_kota:
        for calon in data_calon_dprd_kota[kota]:
            if calon['nomor_urut'] == nomor_urut:
                visi = calon['visi']
                misi = calon['misi']
                break

    return visi, misi

# Fungsi untuk menjalankan program pemilihan DPRD Kota
def pemilihan_dprd_kota():
    data_suara = {}
    data_calon = baca_data_calon()

    for kota in data_calon:
        data_suara[kota] = {}

        for calon in data_calon[kota]:
            data_suara[kota][calon['nomor_urut']] = 0

    while True:
        print("Pemilihan DPRD Kota")
        print("--------------------")

        Kota = input_Kota()
        data_calon_dprd_kota = baca_data_calon()

        if Kota in data_calon_dprd_kota:
            tampilkan_daftar_calon(Kota, data_calon_dprd_kota)

            nomor_urut = input_nomor_urut()

            visi, misi = get_visi_misi(nomor_urut, data_calon_dprd_kota)

            print(f"Visi dan Misi Calon:")
            print("--------------------")
            print(f"Visi: {visi}")
            print(f"Misi: {misi}")
            print("--------------------")

            yakin = input("Apakah Anda yakin dengan pilihan Anda? (Ya/Tidak): ")
            if yakin.lower() != 'ya':
                continue

            if nomor_urut in data_suara[Kota]:
                data_suara[Kota][nomor_urut] += 1
                print("Suara Anda telah tercatat.")
            else:
                print("Nomor urut yang Anda pilih tidak valid.")

            break
        else:
            print("Kota yang Anda masukkan tidak valid. Silakan coba lagi.")

    try:
        with open("data_suara_dprd_kota.json", "w") as file:
            json.dump(data_suara, file)
        print("Terima kasih atas partisipasi Anda dalam pemilihan DPRD Kota.")
    except IOError:
        print("Terjadi kesalahan saat menyimpan data suara.")

# Menjalankan program pemilihan DPRD Kota
pemilihan_dprd_kota()

# Menjalankan program pemilihan DPRD Provinsi
import json

def baca_data_calon():
    try:
        with open("data_calon_DPRDProvinsi.json", "r") as file:
            data_calon_DPRDProvinsi = json.load(file)
        return data_calon_DPRDProvinsi
    except FileNotFoundError:
        print("File data_calon_DPRDProvinsi.json tidak ditemukan.")
        return {}

# Fungsi untuk menampilkan daftar calon DPRD Provinsi berdasarkan Provinsi
def tampilkan_daftar_calon(Provinsi, data_calon):
    if Provinsi not in data_calon:
        print(f"Tidak ada data calon DPRD Provinsi {Provinsi}.")
        return

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

    for Provinsi in data_calon_DPRDProvinsi:
        for calon in data_calon_DPRDProvinsi[Provinsi]:
            if calon['nomor_urut'] == nomor_urut:
                visi = calon['visi']
                misi = calon['misi']
                break

    return visi, misi

# Fungsi untuk menjalankan program pemilihan DPRD Provinsi
def pemilihan_DPRDProvinsi():
    data_suara = {}
    data_calon = baca_data_calon()

    for Provinsi in data_calon:
        data_suara[Provinsi] = {}

        for calon in data_calon[Provinsi]:
            data_suara[Provinsi][calon['nomor_urut']] = 0

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

            if nomor_urut in data_suara[Provinsi]:
                data_suara[Provinsi][nomor_urut] += 1
                print("Suara Anda telah tercatat.")
            else:
                print("Nomor urut yang Anda pilih tidak valid.")
            break
        else:
            print("Provinsi yang Anda masukkan tidak valid. Silakan coba lagi.")

    try:
        with open("data_suara_DPRDProvinsi.json", "w") as file:
            json.dump(data_suara, file)
        print("Terima kasih atas partisipasi Anda dalam pemilihan DPRD Provinsi.")
    except IOError:
        print("Terjadi kesalahan saat menyimpan data suara.")

# Menjalankan program pemilihan DPRD Provinsi
pemilihan_DPRDProvinsi()
import json

def baca_data_calon():
    try:
        with open("data_calon_DPD.json", "r") as file:
            data_calon_DPD = json.load(file)
        return data_calon_DPD
    except FileNotFoundError:
        print("File data_calon_DPD.json tidak ditemukan.")
        return {}

# Fungsi untuk menampilkan daftar calon DPD berdasarkan Provinsi
def tampilkan_daftar_calon(Provinsi, data_calon):
    if Provinsi not in data_calon:
        print(f"Tidak ada data calon DPD {Provinsi}.")
        return

    print(f"Daftar Calon DPD {Provinsi}:")
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
    nomor_urut = input("Masukkan nomor urut calon DPD yang Anda pilih: ")
    return nomor_urut

# Fungsi untuk mendapatkan visi dan misi calon berdasarkan nomor urut
def get_visi_misi(nomor_urut, data_calon_DPD):
    visi = ""
    misi = ""

    for Provinsi in data_calon_DPD:
        for calon in data_calon_DPD[Provinsi]:
            if calon['nomor_urut'] == nomor_urut:
                visi = calon['visi']
                misi = calon['misi']
                break

    return visi, misi

# Fungsi untuk menjalankan program pemilihan DPD
def pemilihan_DPD():
    data_suara = {}
    data_calon = baca_data_calon()

    for Provinsi in data_calon:
        data_suara[Provinsi] = {}

        for calon in data_calon[Provinsi]:
            data_suara[Provinsi][calon['nomor_urut']] = 0

    while True:
        print("Pemilihan DPD")
        print("--------------------")

        Provinsi = input_Provinsi()
        data_calon_DPD = baca_data_calon()

        if Provinsi in data_calon_DPD:
            tampilkan_daftar_calon(Provinsi, data_calon_DPD)

            nomor_urut = input_nomor_urut()

            visi, misi = get_visi_misi(nomor_urut, data_calon_DPD)

            print(f"Visi dan Misi Calon:")
            print("--------------------")
            print(f"Visi: {visi}")
            print(f"Misi: {misi}")
            print("--------------------")

            yakin = input("Apakah Anda yakin dengan pilihan Anda? (Ya/Tidak): ")
            if yakin.lower() != 'ya':
                continue

            if nomor_urut in data_suara[Provinsi]:
                data_suara[Provinsi][nomor_urut] += 1
                print("Suara Anda telah tercatat.")
            else:
                print("Nomor urut yang Anda pilih tidak valid.")
            break
        else:
            print("Provinsi yang Anda masukkan tidak valid. Silakan coba lagi.")

    try:
        with open("data_suara_DPD.json", "w") as file:
            json.dump(data_suara, file)
        print("Terima kasih atas partisipasi Anda dalam pemilihan DPD.")
    except IOError:
        print("Terjadi kesalahan saat menyimpan data suara.")

# Menjalankan program pemilihan DPD
pemilihan_DPD()

def baca_data_calon():
    with open("data_calon DPR.json", "r") as file:
        data_calon_DPR = json.load(file)
    return data_calon_DPR

# Fungsi untuk menampilkan daftar calon DPR berdasarkan Kota
def tampilkan_daftar_calon(Kota, data_calon):
    print(f"Daftar Calon DPR {Kota}:")
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
    nomor_urut = input("Masukkan nomor urut calon DPR yang Anda pilih: ")
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
    data_suara = {}
    data_calon = baca_data_calon()
    
    for kota in data_calon:
        data_suara[kota] = {}
        
        for calon in data_calon[kota]:
            data_suara[kota][calon['nomor_urut']] = 0
    
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

            if nomor_urut in data_suara[Kota]:
                data_suara[Kota][nomor_urut] += 1
                print("Suara Anda telah tercatat.")

            else:
                print("Nomor urut yang Anda pilih tidak valid.")

            break
        else:
            print("Kota yang Anda masukkan tidak valid. Silakan coba lagi.")

    with open("data_suara_DPR.json", "w") as file:
        json.dump(data_suara, file)

    print("Terima kasih atas partisipasi Anda dalam pemilihan DPR.")

# Menjalankan program pemilihan DPR
pemilihan_DPR()

import json

def load_candidates(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data['Presiden']
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
        return []
    except json.JSONDecodeError:
        print(f"File {filename} tidak valid. Format JSON tidak sesuai.")
        return []

def display_candidates(candidates):
    if not candidates:
        print("Tidak ada data calon Presiden.")
        return

    print("Daftar Calon Presiden:")
    print("--------------------")

    for candidate in candidates:
        print(f"Nomor Urut: {candidate['nomor_urut']}")
        print(f"Nama Calon: {candidate['nama']}")
        print("--------------------")

def vote(candidates):
    while True:
        selected_candidate = input("Masukkan nomor urut calon presiden pilihan Anda: ")

        for candidate in candidates:
            if candidate['nomor_urut'] == selected_candidate:
                return candidate

        print("Nomor urut yang Anda masukkan tidak valid. Silakan coba lagi.")

def main():
    candidates = load_candidates("data_calon_presiden.json")

    while True:
        print("Pemilihan Presiden")
        print("--------------------")

        display_candidates(candidates)
        selected_candidate = vote(candidates)

        print("\nAnda telah memilih:")
        print(f"Nomor Urut: {selected_candidate['nomor_urut']}")
        print(f"Nama: {selected_candidate['nama']}")
        print(f"Visi: {selected_candidate['visi']}")
        print(f"Misi: {selected_candidate['misi']}")

        confirm = input("\nApakah Anda yakin dengan pilihan Anda? (ya/tidak): ")
        if confirm.lower() == "ya":
            try:
                with open("data_suara_presiden.json", "w") as file:
                    json.dump(selected_candidate, file)
                print("\nTerima kasih telah melakukan voting!")
            except IOError:
                print("Terjadi kesalahan saat menyimpan data suara.")
            break
        else:
            print("\nPilihan Anda dibatalkan.")

if __name__ == "__main__":
    main()
