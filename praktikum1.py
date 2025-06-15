import numpy as np
import matplotlib.pyplot as plt


#-----------------input disini-----------------
# DEFINISIKAN FUNGSI
def f(x):
    # contoh fungsi : x^3 - x - 2
    # return x**3 - x - 2
    
    # contoh fungsi lain : e^x - 5x^2
    # return np.exp(x) - 5*(x**2)

    # contoh fungsi trigonometri: sin(x)
    # gunakan np.sin bukan sin
    # return np.sin(x)

    # fungsi sin(x) = 5x-2
    return np.sin(x) - (5 * x - 2)

# ubah ini juga sesuai fungsi (tampilkan di grafik)
fungsi_str = 'f(x) = sin(x)'
# ----------------------------------------------------


def regula_falsi(a, b, toleransi=1e-6, max_iterasi=100):
    """
    Implementasi metode Regula Falsi untuk mencari akar fungsi f(x).
    
    Args:
    a (float): Batas bawah interval.
    b (float): Batas atas interval.
    toleransi (float): Toleransi error yang diinginkan.
    max_iterasi (int): Jumlah maksimum iterasi.
    
    Returns:
    float: Akar pendekatan dari fungsi.
    list: Data histori iterasi.
    """
    if f(a) * f(b) >= 0:
        print("Error: Nilai f(a) dan f(b) harus memiliki tanda yang berbeda.")
        return None, None

    c = a  # Inisialisasi c
    histori_iterasi = []

    print("-" * 80)
    print("{:^80}".format("Proses Iteratif Numerik Metode Regula Falsi"))
    print("-" * 80)
    print("{:^5} | {:^15} | {:^15} | {:^15} | {:^15} |".format("Iter", "a", "b", "c", "f(c)"))
    print("-" * 80)

    for i in range(max_iterasi):
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        
        iterasi_data = [i + 1, a, b, c, f(c)]
        histori_iterasi.append(iterasi_data)
        
        print("{:^5} | {:^15.6f} | {:^15.6f} | {:^15.6f} | {:^15.6f} |".format(i + 1, a, b, c, f(c)))

        if abs(f(c)) < toleransi:
            print("-" * 80)
            print(f"\nSolusi ditemukan setelah {i+1} iterasi.")
            return c, histori_iterasi

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
            
    print("-" * 80)
    print(f"\nSolusi tidak konvergen setelah {max_iterasi} iterasi.")
    return c, histori_iterasi

def plot_grafik(akar, histori):
    a_awal = histori[0][1]
    b_awal = histori[0][2]
    x = np.linspace(min(a_awal, b_awal) - 1, max(a_awal, b_awal) + 1, 400)
    y = f(x) 

    plt.figure(figsize=(10, 6))
    
    plt.plot(x, y, label=fungsi_str, color='blue')
    
    if akar is not None:
        plt.plot(akar, f(akar), 'ro', markersize=8, label=f'Akar ditemukan: x = {akar:.6f}')
    
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    
    plt.title('Grafik Fungsi dan Akar dengan Metode Regula Falsi')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()


# -----------------input disini-----------------
if __name__ == "__main__":
    # Input disini
    # Batas interval awal [a, b]
    # Contoh untuk f(x) = sin(x), cari akar di antara 2 dan 4
    # batas_a = 2.0
    # batas_b = 4.0
    batas_a = 0.4
    batas_b = 1.0
# -----------------------------------------------
    
    akar_ditemukan, histori = regula_falsi(batas_a, batas_b)

    if akar_ditemukan is not None:
        print(f"\nAkar pendekatan adalah: x = {akar_ditemukan:.6f}")
        print(f"Nilai f(x) di akar: f({akar_ditemukan:.6f}) = {f(akar_ditemukan):.6f}")
        
        # Tampilkan grafik
        plot_grafik(akar_ditemukan, histori)
