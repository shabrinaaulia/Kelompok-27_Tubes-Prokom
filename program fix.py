import json

def print_welcome_message():
    print("========Selamat datang di program Pemilihan Umum Provinsi Jakarta========")
    print("Anda akan melakukan pemilihan DPRD Kota, DPRD Provinsi, DPD, DPR, dan Presiden")


def get_voter_data(nik):
    try:
        with open('data_pemilih.csv', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if data[2] == nik:
                    return data
    except FileNotFoundError:
        print("File data_pemilih.csv tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file data_pemilih.csv: {str(e)}")
    return None


def is_voter_already_voted(nik):
    try:
        with open('hasil_pemilih.csv', 'a') as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == nik:
                    return True
    except FileNotFoundError:
        print("File hasil_pemilih.csv tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file hasil_pemilih.csv: {str(e)}")
    return False


def display_voter_info(nik):
    voter_data = get_voter_data(nik)
    if voter_data is not None:
        print("\nData Pemilih:")
        print(f"\nNIK           : {voter_data[2]}")
        print(f"Nama            : {voter_data[3]}")
        print(f"Asal Provinsi   : {voter_data[0]}")
        print(f"Asal Kota       : {voter_data[1]}")
    else:
        print("Data pemilih tidak ditemukan.")


def display_candidates(city, file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            candidates = data[city]
        print(f"Calon {file_name[:-5]} {city}:")
        for candidate in candidates:
            print(f"No. Urut      : {candidate['nomor_urut']}")
            print(f"Nama          : {candidate['nama']}")
            print(f"{candidate['visi']}")
            print(f"{candidate['misi']}")
            print()
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file {file_name}: {str(e)}")


def get_candidate_choice():
    return input("Masukkan nomor urut calon yang dipilih: ")


def confirm_choice():
    choice = input("Apakah Anda yakin dengan pilihan Anda? (ya/tidak): ")
    return choice.lower() == 'ya'


def save_vote(nik, choice):
    try:
        with open('hasil_pemilih.csv', 'a') as file:
            line = f"{nik},{choice}\n"
            file.write(line)
    except FileNotFoundError:
        print("File hasil_pemilih.csv tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan suara ke file hasil_pemilih.csv: {str(e)}")


def load_voted_niks():
    voted_niks = set()
    try:
        with open('hasil_pemilih.csv', 'r') as file:
            for line in file:
                data = line.strip().split(',')
                voted_niks.add(data[0])
    except FileNotFoundError:
        print("File hasil_pemilih.csv tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file hasil_pemilih.csv: {str(e)}")
    return voted_niks


def pemilihan_presiden(nik):
    print("Pemilihan Presiden")
    display_candidates("Presiden", "data_calon_presiden.json")  # Menampilkan data calon presiden

    while True:
        choice = get_candidate_choice()  # Meminta input nomor urut calon yang dipilih
        if confirm_choice():
            save_vote(nik, choice)  # Menyimpan suara ke file hasil_pemilih.csv
            print("Terima kasih, suara Anda telah tersimpan.")
            break
        else:
            print("Pemilihan Presiden dibatalkan.")


# Main program
print_welcome_message()
nik = input("Masukkan NIK Anda: ")

voted_niks = load_voted_niks()
if nik in voted_niks:
    print("Anda sudah melakukan pemilihan sebelumnya. Terima kasih.")
else:
    display_voter_info(nik)  # Menampilkan informasi pemilih berdasarkan NIK

    # Pemilihan DPRD Kota
    city = get_voter_data(nik)[1]
    if city:
        print("Pemilihan DPRD Kota")
        display_candidates(city, 'data_calon_dprd_kota.json')
        while True:
            choice = get_candidate_choice()
            if confirm_choice():
                save_vote(nik, choice)
                print("Terima kasih, suara Anda telah tersimpan.")
                break
            else:
                print("Pemilihan DPRD Kota dibatalkan.")
    else:
        print("Asal kota pemilih tidak ditemukan.")

    # Pemilihan DPRD Provinsi
    province = get_voter_data(nik)[0]
    if province:
        print("Pemilihan DPRD Provinsi")
        display_candidates(province, 'data_calon_DPRDProvinsi.json')
        while True:
            choice = get_candidate_choice()
            if confirm_choice():
                save_vote(nik, choice)
                print("Terima kasih, suara Anda telah tersimpan.")
                break
            else:
                print("Pemilihan DPRD Provinsi dibatalkan.")
    else:
        print("Asal provinsi pemilih tidak ditemukan.")

    # Pemilihan DPD
    province = get_voter_data(nik)[0]
    if province:
        print("Pemilihan DPD")
        display_candidates(province, 'data_calon_DPD.json')
        while True:
            choice = get_candidate_choice()
            if confirm_choice():
                save_vote(nik, choice)
                print("Terima kasih, suara Anda telah tersimpan.")
                break
            else:
                print("Pemilihan DPD dibatalkan.")
    else:
        print("Asal provinsi pemilih tidak ditemukan.")

    # Pemilihan DPR
    city = get_voter_data(nik)[1]
    if city:
        print("Pemilihan DPR")
        display_candidates(city, 'data_calon DPR.json')
        while True:
            choice = get_candidate_choice()
            if confirm_choice():
                save_vote(nik, choice)
                print("Terima kasih, suara Anda telah tersimpan.")
                break
            else:
                print("Pemilihan DPR dibatalkan.")
    else:
        print("Asal kota pemilih tidak ditemukan.")

    # Pemilihan Presiden
    pemilihan_presiden(nik)
