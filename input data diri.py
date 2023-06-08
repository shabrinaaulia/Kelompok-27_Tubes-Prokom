import csv

def is_unique(nim):
    with open('data_pemilih.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if nim == row[1]:
                return False
    return True

def input_data_pemilih():
    asal = input("Masukkan asal: ")
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan nama: ")

    if is_unique(nim):
        with open('data_pemilih.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([asal, nim, nama])
        print("Data pemilih berhasil disimpan.")
    else:
        print("NIM tersebut telah digunakan sebelumnya.")

def tampilkan_data_calon(kota):
    with open('data_calon_kota.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['kota'] == kota:
                print("Nama Calon: ", row['nama'])
                print("Partai: ", row['partai'])
                print("Kota: ", row['kota'])
                print("------------------------")

def main():
    input_data_pemilih()

    kota_pemilih = input("Masukkan kota pemilih: ")
    tampilkan_data_calon(kota_pemilih)

if __name__ == "__main__":
    main()
