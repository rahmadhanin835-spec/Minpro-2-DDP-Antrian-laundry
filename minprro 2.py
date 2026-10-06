import pwinput
from prettytable import PrettyTable
import os

akun = {
    "admin":{
        "password":"loveddp",
        "role":"admin"
    },
    "user":{
        "password":"cintaddp",
        "role":"user"
    }
}
antrian = []

def login():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== LOGIN ===")
    username = input("Masukkan username: ")
    password = pwinput.pwinput("Masukkan password: ")
    if username in akun and akun[username]["password"] == password:
        print(f"Selamat datang, {username}!")
        return akun[username]["role"]
    else:
        print("Username atau password salah!")
        return None

def tambah_antrian():
    nama = input("Masukkan nama: ")
    print("====== JENIS LAYANAN ======")
    tabel = PrettyTable()
    tabel.field_names = ["NO", "Jenis layanan", "Estimasi waktu"]
    tabel.add_row(["1", "Cuci Kering", "1-2 hari"])
    tabel.add_row(["2", "Cuci + Setrika", "2-3 hari"])
    tabel.add_row(["3", "Express", "1 hari"])
    print(tabel)
    layanan = input("Pilih jenis layanan (1/2/3): ")
    if layanan == "1":
        jenis_layanan = "Cuci Kering"
        harga = 4000
        waktu = "1-2 hari"
    elif layanan == "2":
        jenis_layanan = "Cuci + Setrika"
        harga = 6000
        waktu = "2-3 hari"
    elif layanan == "3":
        jenis_layanan = "Express"
        harga = 10000
        waktu = "1 hari"
    else:
        print("Layanan tidak tersedia")
        return
    berat = float(input("Masukkan berat pakaian (kg): "))
    if berat <= 0:
        print("Berat pakaian harus lebih dari 0 kg!")
        return
    estimasi_biaya = harga * berat
    if not antrian:
        nomor_antrian = 1
    else:
        nomor_antrian = antrian[-1]["nomor_antrian"] + 1
    data = {"nomor_antrian": nomor_antrian, "nama": nama, "jenis_layanan": jenis_layanan, "berat": berat, "estimasi_biaya": estimasi_biaya, "waktu": waktu}
    antrian.append(data)
    print("===== Antrean berhasil ditambahkan =====")
    tabel = PrettyTable()
    tabel.field_names = ["Nomor antrean", "Nama pelanggan", "Jenis layanan", "Berat pakaian (kg)", "Estimasi biaya", "Estimasi waktu"]
    tabel.add_row([nomor_antrian, nama, jenis_layanan, berat, int(estimasi_biaya), waktu])
    print(tabel)
    print("Nomor antrean: ", nomor_antrian)

def tampilkan_antrian():
    if not antrian:
        print("Belum ada antrean laundry")
        return
    print("---- Daftar antrean Laundry Lovely ----")
    tabel = PrettyTable()
    tabel.field_names = ["Nomor antrean", "Nama pelanggan", "Jenis layanan", "Berat pakaian (kg)", "Estimasi biaya", "Estimasi waktu"]
    for data in antrian:
        tabel.add_row([data["nomor_antrian"], data["nama"], data["jenis_layanan"], data["berat"], int(data["estimasi_biaya"]), data["waktu"]])
    print(tabel)

def ubah_antrian():
    if not antrian:
        print("Belum ada antrean laundry!")
        return
    tampilkan_antrian()
    nomor = int(input("Masukkan nomor antrean yang ingin diubah: "))
    for data in antrian:
        if data["nomor_antrian"] == nomor:
            nama_baru = input("Masukkan nama baru: ")
            print("====== JENIS LAYANAN ======")
            tabel = PrettyTable()
            tabel.field_names = ["NO", "Jenis layanan", "Estimasi waktu"]
            tabel.add_row(["1", "Cuci Kering", "1-2 hari"])
            tabel.add_row(["2", "Cuci + Setrika", "2-3 hari"])
            tabel.add_row(["3", "Express", "1 hari"])
            print(tabel)
            layanan = input("Pilih jenis layanan (1/2/3): ")
            if layanan == "1":
                jenis_layanan_baru = "Cuci Kering"
                harga = 4000
                waktu_baru = "1-2 hari"
            elif layanan == "2":
                jenis_layanan_baru = "Cuci + Setrika"
                harga = 6000
                waktu_baru = "2-3 hari"
            elif layanan == "3":
                jenis_layanan_baru = "Express"
                harga = 10000
                waktu_baru = "1 hari"
            else:
                print("Layanan tidak tersedia!")
                return
            berat_baru = float(input("Masukkan berat baru (kg): "))
            if berat_baru <= 0:
                print("Berat harus lebih dari 0 kg!")
                return
            data["nama"] = nama_baru
            data["jenis_layanan"] = jenis_layanan_baru
            data["berat"] = berat_baru
            data["estimasi_biaya"] = harga * berat_baru
            data["waktu"] = waktu_baru
            print("Data antrean berhasil diubah!")
            return
    print("Nomor antrean tidak ditemukan!")

def hapus_antrian():
    if not antrian:
        print("Belum ada antrean laundry")
        return
    else:
        tampilkan_antrian()
        nomor = int(input("Masukkan nomor antrean: "))
        for data in antrian:
            if data["nomor_antrian"] == nomor:
                antrian.remove(data)
                print("Antrian berhasil dihapus")
                return

def menu_admin():
    while True:
        print("====== MENU ADMIN LAUNDRY LOVELY ======")
        tabel = PrettyTable()
        tabel.field_names = ["No", "Menu"]
        tabel.add_row([1, "Tambah antrean"])
        tabel.add_row([2, "Tampilkan antrean"])
        tabel.add_row([3, "Ubah antrean"])
        tabel.add_row([4, "Hapus antrean"])
        tabel.add_row([5, "Keluar"])
        print(tabel)
        pilih = input("Pilih menu: ")
        if pilih == "1":
            tambah_antrian()
        elif pilih == "2":
            tampilkan_antrian()
        elif pilih == "3":
            ubah_antrian()
        elif pilih == "4":
            hapus_antrian()
        elif pilih == "5":
            print("Terima kasih telah menggunakan layanan laundry lovely")
            break
        else:
            print("Pilihan menu tidak tersedia")

def menu_user():
    while True:
        print("====== MENU USER LAUNDRY LOVELY ======")
        tabel = PrettyTable()
        tabel.field_names = ["No", "Menu"]
        tabel.add_row([1, "Tambah antrean"])
        tabel.add_row([2, "Tampilkan antrean"])
        tabel.add_row([3, "keluar"])
        print(tabel)
        pilih = input("Pilih menu: ")
        if pilih == "1":
            tambah_antrian()
        elif pilih == "2":
            tampilkan_antrian()
        elif pilih == "3":
            print("Terima kasih telah menggunakan layanan laundry lovely")
            break
        else:
            print("Pilihan menu tidak tersedia")

while True:
    role = login()
    if role == "admin":
        menu_admin()
    elif role == "user":
        menu_user()
    else:
        print("Silakan login kembali.")