# Program menghitung kebutuhan bahan bakar Dimas

# Data perjalanan
jarak_satu_kali = 100          # km
konsumsi_bensin = 40           # km per liter
sisa_bensin = 1.5              # liter
harga_bensin = 10000           # rupiah per liter

# 1. Total jarak perjalanan pulang-pergi
total_jarak = jarak_satu_kali * 2

# 2. Total kebutuhan bahan bakar
total_bensin = total_jarak / konsumsi_bensin

# 3. Jumlah bahan bakar yang harus dibeli
bensin_dibeli = total_bensin - sisa_bensin

# 4. Total biaya bahan bakar
total_biaya = bensin_dibeli * harga_bensin

# Menampilkan hasil
print("=== PERHITUNGAN BAHAN BAKAR DIMAS ===")
print("Total jarak perjalanan       :", total_jarak, "km")
print("Total kebutuhan bahan bakar :", total_bensin, "liter")
print("Bensin yang harus dibeli    :", bensin_dibeli, "liter")
print("Total biaya bahan bakar     : Rp", total_biaya)
