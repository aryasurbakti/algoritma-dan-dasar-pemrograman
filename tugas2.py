# Program menghitung volume kerucut

# Input jari-jari dan tinggi
r = float(input("Masukkan jari-jari alas (cm): "))
t = float(input("Masukkan tinggi kerucut (cm): "))

# Nilai pi
pi = 3.14

# Menghitung volume kerucut
volume = (1/3) * pi * r**2 * t

# Menampilkan hasil
print("Volume kerucut =", volume, "cm³")
