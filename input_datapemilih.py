import csv

def load_data(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            data.append(row)
    return header, data

def save_data(filename, header, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

def check_duplicate_data(data, new_data):
    for row in data:
        if row[:3] == new_data:
            return True
    return False

def input_data(data):
    asal = input("Masukkan Asal: ")
    nim = input("Masukkan Nim: ")
    nama = input("Masukkan Nama: ")

    new_data = [asal, nim, nama]

    if check_duplicate_data(data, new_data):
        print("Data sudah digunakan sebelumnya. Silakan input data lagi.")
        return

    data.append(new_data)
    print("Data berhasil disimpan.")

def main():
    filename = "datapemilih.csv"
    header, data = load_data(filename)

    while True:
        print("\nMenu:")
        print("1. Input Data Diri")
        print("2. Sudah Input Data Diri")
        choice = input("Pilih menu (1/2): ")

        if choice == "1":
            input_data(data)
        elif choice == "2":
            save_data(filename, header, data)
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

main()
