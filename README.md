# Minpro-2-DDP-Antrian-laundry

Nama: Nabilah Rahmadhani

NIM: 2609116041

Kelas: B

# FLOWCHART

<img width="3065" height="2387" alt="minpro ddp2 9" src="https://github.com/user-attachments/assets/471d1b31-6615-42f6-a337-0c2f0c1f7d20" />

PENJELASAN
1. start:

program dimulai
program dimulai dengan memasukkan username dan password. username dan password yang di input akan dibedakan menjadi dua role yaitu: admin & user.

- admin
  
  sistem akan menampilkan lima menu khusus admin saja yang bisa mengaksesnya. menu tersebut berupa tambah antrian, tampilkan antrian, ubah antrian, hapus antrian, dan keluar dari program.
  
- user
  
  sistem akan menampilkan tiga menu saja untuk user. menu tersebut berupa menambah antrian, tampilkan antrian, dan keluar dari program.

2. menu

pada menu, terdapat 5 jenis menu yang bisa dipilih:

- tambah antrean: sistem akan meminta pengguna menginput nama dan memilih jenis layanan laundry. terdapat 3 jenis laundry yang tersedia, yaitu cuci kering sekitar 1-2 hari, cuci + setrika sekitar 2-3 hari, dan express sekitar 1 hari. setelah memilih, pengguna akan diminta menginputkan berat pakaian. setelah itu, program akan menampilkan hasil antrian yang telah di input dan memberikan nomor antrian.

- tampilkan antrian: sistem akan menampilkan keseluruhan antrian laundry.

- ubah antrian: sistem akan menampilkan keseluruhan antrian dan pengguna akan diminta menginputkan nomor antrian mana yang ingin diubah. setelah itu, pengguna akan menginputkan nama baru, jenis layanan laundry, dan berat pakaian tersebut. maka data antrian berhasil diubah.

- hapus antrian: sistem mengecek terlebih dahulu apakah terdapat antrian atau tidak. setelah dikonfirmasi terdapat antrian, pengguna akan menginputkan nomor antrian yang ingin dihapus. setelah terhapus, sistem akan menampilkan keseluruhan data antrian.

- keluar: sistem akan menampilkan pesan terima kasih dan menutup program.

# TAMPILAN AWAL
<img width="182" height="101" alt="Screenshot 2026-10-06 042431" src="https://github.com/user-attachments/assets/63a828f0-1492-46ac-9ca5-43acf5ee84a0" />

tampilan awal dari antrian laundry lovely. pengguna akan diminta menginputkan username dan password tergantung dari role. jika admin bisa menginputkan username: admin & password: loveddp. jika user maka username: user & password: cintaddp.


# ROLE: ADMIN
<img width="353" height="199" alt="image" src="https://github.com/user-attachments/assets/1b1d2fb3-ce86-4e86-aa55-e370fee703da" />

pada role admin, terdapat lima jenis menu yang tersedia. menu tersebut berupa tambah antrean, tampilkan antrian, ubah antrian, hapus antrrian, dan keluar dari program.

# ROLE: USER
<img width="251" height="131" alt="Screenshot 2026-10-06 043445" src="https://github.com/user-attachments/assets/7707fe56-a522-4b90-bad7-79cd3994d664" />

pada role user, hanya terdapat 3 jenis menu yang tersedia. menu tersebut berupa tambah antrean, tampilkan antrian, dan keluar dari program.

# OUTPUT 1
<img width="653" height="414" alt="Screenshot 2026-10-06 042834" src="https://github.com/user-attachments/assets/8d56e75e-e2af-4dff-bd7f-ef7020d52800" />
<img width="698" height="224" alt="Screenshot 2026-10-06 042927" src="https://github.com/user-attachments/assets/be12e8b3-f0c3-4a69-98f9-952e1e08fc16" />

Saat pengguna menambahkan antrean, pengguna menginput nama pelanggan, kemudian memilih jenis layanan laundry. Terdapat tiga pilihan layanan, yaitu Cuci Kering, Cuci + Setrika, dan Express. Setiap layanan memiliki harga dan estimasi waktu pengerjaan yang berbeda. setelah itu, pengguna akan menginputkan berat pakaian. sistem akan menghitung berdasarkan input yang telah diterima dan memasukkan data tersebut ke dalam daftar antrean.

# OUTPUT 2
<img width="663" height="251" alt="Screenshot 2026-10-06 042946" src="https://github.com/user-attachments/assets/05f13809-d1e0-48f6-b020-5317c7cea109" />

saat pengguna memilih menu 2 (tampilkan antrian), sistem akan menampilkan keseluruhan daftar antrean laundry yang telah ditambahkan sebelumnya. daftar antrean tersebut berupa nomor antrian, nama, jenis layanan, berat, estimasi biaya, dan estimasi hari pengerjaaan.

# OUTPUT 3
<img width="687" height="413" alt="Screenshot 2026-10-06 043124" src="https://github.com/user-attachments/assets/e0247eef-e163-491b-92da-8ea415f9b575" />

pengguna yang memilih menu 3 dapat mengubah daftar antrean. pengguna akan diminta menginputkan nomor antrian yang ingin diubah, masukkan nama baru, jenis layanan, dan berat pakaian. Sistem kemudian menghitung kembali estimasi biaya berdasarkan data terbaru.

# OUTPUT 4
<img width="700" height="288" alt="Screenshot 2026-10-06 043251" src="https://github.com/user-attachments/assets/01d71420-60ab-4e7a-b6a6-508950d39a30" />

pengguna dapat menghapus antrean yang telah mereka tambahkan sebelumnya apabila sudah selesai atau sudah tidak diperlukan lagi.

# OUTPUT 5
<img width="267" height="149" alt="Screenshot 2026-10-06 043309" src="https://github.com/user-attachments/assets/28d16df5-987d-43f9-8070-b611322460d5" />

Setelah selesai menggunakan menu, pengguna dapat memilih keluar. Sistem kemudian kembali ke halaman login sehingga pengguna lain dapat melakukan login menggunakan akun masing-masing.

# PERUBAHAN DARI PROGRAM SEBELUMNYA

pada program sebelumnnya hanya terdapat 4 pilihan yaitu tambah antrian, tampilkan antrian, hapus antrian, dan keluar dari program. pada minpro 2 ini saya menambahkan satu fitur berupa ubah data. dikarenakan pada ketentuan minpro 2 ini terdapat ketentuan CRUD wajib lengkap.

# NILAI TAMBAH

<img width="656" height="200" alt="image" src="https://github.com/user-attachments/assets/13ed2471-0675-412c-b9a0-1dbdf4be3ad5" />

<img width="230" height="20" alt="image" src="https://github.com/user-attachments/assets/b466f1cf-b39a-4bdb-a83c-379e12802623" />

Pada minpro ini mencoba mendapatkan nilai tambah berupa *Menerapkan 3 library atau lebih sesuai dengan kebutuhan program.* saya menggunakan library pwinput untuk menyembunyikan tampilan password pada saat login, library PrettyTable pada menu dan jenis layanan laundry, dan library os untuk clear system.
