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
        
input_data_pemilih()