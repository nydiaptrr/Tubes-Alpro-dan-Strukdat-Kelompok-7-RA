import tkinter as tk
from tkinter import messagebox, simpledialog

# Tempat menyimpan daftar soal dan jawabannya (kosong saat pertama kali dijalankan)
daftar_soal = []

# Fungsi untuk proses login
def login():
    # Ambil data dari kolom input username dan password
    username = kolom_username.get()
    password = kolom_password.get()
    
    # Cek apakah kedua kolom telah diisi
    if username and password:
        messagebox.showinfo("Login Berhasil", f"Halo, {username}! Selamat datang.")
        menu_utama()  # Pindah ke menu utama
    else:
        messagebox.showerror("Login Gagal", "Username dan password tidak boleh kosong!")

# Fungsi untuk menampilkan menu utama
def menu_utama():
    # Tutup jendela login
    jendela_login.destroy()
    
    # Buat jendela baru untuk menu utama
    global jendela_utama
    jendela_utama = tk.Tk()
    jendela_utama.title("Aplikasi Kuis - Menu Utama")
    jendela_utama.configure(bg="#f0f0f0")  # Warna latar belakang

    # Tambahkan tombol untuk berbagai fitur
    tk.Button(jendela_utama, text="Tambah Soal", command=tambah_soal, width=20, bg="#4CAF50", fg="white").pack(pady=5)
    tk.Button(jendela_utama, text="Edit Soal", command=edit_soal, width=20, bg="#2196F3", fg="white").pack(pady=5)
    tk.Button(jendela_utama, text="Hapus Soal", command=hapus_soal, width=20, bg="#f44336", fg="white").pack(pady=5)
    tk.Button(jendela_utama, text="Mulai Kuis", command=mulai_kuis, width=20, bg="#FF9800", fg="white").pack(pady=5)
    tk.Button(jendela_utama, text="Keluar", command=jendela_utama.destroy, width=20, bg="#9E9E9E", fg="white").pack(pady=5)

    jendela_utama.mainloop()

# Fungsi untuk menambahkan soal
def tambah_soal():
    # Tampilkan dialog untuk menulis pertanyaan
    pertanyaan = simpledialog.askstring("Tambah Soal", "Masukkan pertanyaan:")
    if pertanyaan:
        jawaban = simpledialog.askstring("Jawaban Soal", "Masukkan jawaban yang benar:")
        if jawaban:
            daftar_soal.append({"soal": pertanyaan, "jawaban": jawaban})
            messagebox.showinfo("Sukses", "Soal berhasil ditambahkan!")
        else:
            messagebox.showerror("Error", "Jawaban tidak boleh kosong!")
    else:
        messagebox.showerror("Error", "Pertanyaan tidak boleh kosong!")

# Fungsi untuk mengedit soal
def edit_soal():
    if not daftar_soal:
        messagebox.showerror("Error", "Tidak ada soal yang tersedia untuk diedit.")
        return

    # Minta pengguna memilih nomor soal yang akan diedit
    nomor_soal = simpledialog.askinteger("Edit Soal", f"Pilih nomor soal (1-{len(daftar_soal)}):")
    if nomor_soal and 1 <= nomor_soal <= len(daftar_soal):
        soal_baru = simpledialog.askstring("Edit Soal", "Masukkan pertanyaan baru:")
        jawaban_baru = simpledialog.askstring("Edit Jawaban", "Masukkan jawaban baru:")
        if soal_baru and jawaban_baru:
            daftar_soal[nomor_soal - 1] = {"soal": soal_baru, "jawaban": jawaban_baru}
            messagebox.showinfo("Sukses", "Soal berhasil diperbarui!")
        else:
            messagebox.showerror("Error", "Pertanyaan atau jawaban tidak boleh kosong!")
    else:
        messagebox.showerror("Error", "Nomor soal tidak valid!")

# Fungsi untuk menghapus soal
def hapus_soal():
    if not daftar_soal:
        messagebox.showerror("Error", "Tidak ada soal yang tersedia untuk dihapus.")
        return

    # Minta pengguna memilih nomor soal yang akan dihapus
    nomor_soal = simpledialog.askinteger("Hapus Soal", f"Pilih nomor soal (1-{len(daftar_soal)}):")
    if nomor_soal and 1 <= nomor_soal <= len(daftar_soal):
        del daftar_soal[nomor_soal - 1]
        messagebox.showinfo("Sukses", "Soal berhasil dihapus!")
    else:
        messagebox.showerror("Error", "Nomor soal tidak valid!")

# Fungsi untuk memulai kuis
def mulai_kuis():
    if not daftar_soal:
        messagebox.showerror("Error", "Tidak ada soal untuk dimainkan. Tambahkan soal terlebih dahulu!")
        return

    skor = 0  # Inisialisasi skor
    tampilkan_soal(0, skor)  # Mulai dari soal pertama

# Fungsi untuk menampilkan soal (dengan rekursi)
def tampilkan_soal(indeks, skor):
    if indeks < len(daftar_soal):
        soal = daftar_soal[indeks]
        jawaban_pengguna = simpledialog.askstring(f"Soal {indeks + 1}", soal["soal"])
        if jawaban_pengguna and jawaban_pengguna.lower() == soal["jawaban"].lower():
            skor += 1
            messagebox.showinfo("Benar", "Jawaban Anda benar!")
        else:
            messagebox.showinfo("Salah", f"Jawaban yang benar: {soal['jawaban']}")
        tampilkan_soal(indeks + 1, skor)  # Panggil fungsi ini lagi untuk soal berikutnya
    else:
        messagebox.showinfo("Hasil Kuis", f"Skor Anda: {skor} dari {len(daftar_soal)}")

# Jendela login
jendela_login = tk.Tk()
jendela_login.title("Aplikasi Kuis - Login")
jendela_login.configure(bg="#f0f0f0")

# Kolom input username dan password
tk.Label(jendela_login, text="Username:", bg="#f0f0f0").pack()
kolom_username = tk.Entry(jendela_login)
kolom_username.pack()

tk.Label(jendela_login, text="Password:", bg="#f0f0f0").pack()
kolom_password = tk.Entry(jendela_login, show="*")
kolom_password.pack()

# Tombol login
tk.Button(jendela_login, text="Login", command=login, bg="#2196F3", fg="white").pack()

jendela_login.mainloop()
