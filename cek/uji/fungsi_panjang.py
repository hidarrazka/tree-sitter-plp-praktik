def hitung_statistik(data):
    jumlah = 0
    minimum = None
    maksimum = None
    genap = 0
    ganjil = 0
    positif = 0
    negatif = 0
    nol = 0
    kuadrat = 0
    kubik = 0
    total_kuadrat = 0
    total_kubik = 0
    rata_rata = 0
    selisih = 0
    rentang = 0
    banyak = 0
    pertama = None
    terakhir = None
    urutan = []
    unik = set()
    duplikat = 0
    besar = 0
    kecil = 0
    sedang = 0
    kelipatan_tiga = 0
    kelipatan_lima = 0
    prima = 0
    bukan_prima = 0
    jumlah_digit = 0
    rata_digit = 0
    maks_digit = 0
    min_digit = 0
    palindrom = 0
    bukan_palindrom = 0
    valid = 0
    tidak_valid = 0
    for nilai in data:
        jumlah += 1
        if minimum is None or nilai < minimum:
            minimum = nilai
        if maksimum is None or nilai > maksimum:
            maksimum = nilai
    return {
        "jumlah": jumlah,
        "minimum": minimum,
        "maksimum": maksimum,
    }


def fungsi_pendek(a, b):
    return a + b
