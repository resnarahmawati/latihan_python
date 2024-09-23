username_benar = "admin"
password_benar = "nimda123"

username_input = input("Masukkan username: ")
password_input = input("Masukkan password: ")

if username_input == username_benar and password_input == password_benar:
    print("Login Berhasil")
else:
    print("Login Gagal")
