import math

def fungsi_integrasi(x):
  """
  Fungsi yang akan diintegrasikan.
  Contoh: f(x) = sin(x)
  """
  return math.sin(x)

def metode_trapesium(f, a, b, n):
  """
  Menghitung integral numerik menggunakan metode Trapesium.
  f: fungsi
  a: batas bawah
  b: batas atas
  n: jumlah interval
  """
  h = (b - a) / n
  hasil = 0.5 * (f(a) + f(b))
  for i in range(1, n):
    hasil += f(a + i * h)
  return h * hasil

def integrasi_romberg(f, a, b, max_iter=5):
  """
  Menghitung integral numerik menggunakan metode Integrasi Romberg.
  Metode ini secara cerdas memperbaiki hasil dari metode Trapesium.
  """
  R = [[0.0] * max_iter for _ in range(max_iter)]
  
  print("--- Tabel Integrasi Romberg ---")
  print("Iterasi | Hasil Trapesium | Ekstrapolasi Romberg")
  print("-" * 50)

  for i in range(max_iter):
    # Hitung metode trapesium dengan n = 2^i interval
    n = 2**i
    R[i][0] = metode_trapesium(f, a, b, n)
    
    # Lakukan ekstrapolasi Richardson
    for j in range(1, i + 1):
      R[i][j] = (4**j * R[i][j-1] - R[i-1][j-1]) / (4**j - 1)

    # Cetak hasil setiap iterasi
    romberg_results = " ".join([f"{val:.8f}" for val in R[i][:i+1]])
    print(f"  {i+1:<6}  | {R[i][0]:.8f}    | {romberg_results}")
  
  print("-" * 50)
  return R[max_iter-1][max_iter-1]

# --- MAIN PROGRAM ---
if __name__ == "__main__":
  # Definisikan batas integrasi
  batas_bawah = 0
  batas_atas = math.pi
  nilai_eksak = 2.0

  print(f"Menghitung integral dari sin(x) dari {batas_bawah} sampai {batas_atas:.4f}")
  print(f"Nilai eksak integral adalah: {nilai_eksak}\n")

  # --- Demonstrasi Metode Romberg ---
  print("### Demonstrasi Metode Integrasi Romberg ###")
  # Romberg hanya memerlukan beberapa iterasi (misal: 5)
  hasil_romberg = integrasi_romberg(fungsi_integrasi, batas_bawah, batas_atas, max_iter=5)
  galat_romberg = abs(nilai_eksak - hasil_romberg)
  
  print(f"\nHasil akhir Integrasi Romberg: {hasil_romberg:.8f}")
  print(f"Galat (Error) Romberg:        {galat_romberg:.10f}\n")
  
  print("="*60 + "\n")

  # --- Demonstrasi Metode Trapesium ---
  print("### Demonstrasi Metode Trapesium Murni ###")
  print("Untuk mencapai akurasi serupa, Trapesium butuh banyak interval.")
  
  # Menggunakan jumlah interval yang sedikit (sama seperti iterasi awal Romberg)
  n_kecil = 16 # Sama dengan jumlah interval pada iterasi ke-5 Romberg (2^(5-1))
  hasil_trapesium_kecil = metode_trapesium(fungsi_integrasi, batas_bawah, batas_atas, n_kecil)
  galat_trapesium_kecil = abs(nilai_eksak - hasil_trapesium_kecil)
  print(f"Hasil Trapesium (n={n_kecil}):   {hasil_trapesium_kecil:.8f}")
  print(f"Galat (Error) Trapesium (n={n_kecil}): {galat_trapesium_kecil:.10f}\n")

  # Membutuhkan jumlah interval yang sangat besar untuk akurasi tinggi
  n_besar = 1000
  hasil_trapesium_besar = metode_trapesium(fungsi_integrasi, batas_bawah, batas_atas, n_besar)
  galat_trapesium_besar = abs(nilai_eksak - hasil_trapesium_besar)
  print(f"Hasil Trapesium (n={n_besar}): {hasil_trapesium_besar:.8f}")
  print(f"Galat (Error) Trapesium (n={n_besar}): {galat_trapesium_besar:.10f}")
