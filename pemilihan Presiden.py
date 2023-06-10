import json

def load_candidates(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data['Presiden']

def display_candidates(candidates):
    print("Daftar Calon Presiden:")
    print("--------------------")

    for candidate in candidates:
        print(f"Nomor Urut: {candidate['nomor_urut']}")
        print(f"Nomor Urut: {candidate['nama']}")
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
            print("\nTerima kasih telah melakukan voting!")
            break
        else:
            print("\nPilihan Anda dibatalkan.")

if __name__ == "__main__":
    main()
