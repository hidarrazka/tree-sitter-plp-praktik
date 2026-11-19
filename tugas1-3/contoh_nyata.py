"""Modul contoh berukuran lebih dari 100 baris untuk Tugas 2."""



import json
from pathlib import Path

BOBOT_TUGAS = 0.30
BOBOT_UTS = 0.30
BOBOT_UAS = 0.40
NILAI_LULUS = 60


def validasi_nilai(nilai):
    """Pastikan nilai berada pada rentang 0 sampai 100."""
    if not isinstance(nilai, (int, float)):
        return False
    return 0 <= nilai <= 100


def validasi_bobot(tugas, uts, uas):
    """Pastikan total bobot sama dengan 1.0."""
    total = tugas + uts + uas
    return abs(total - 1.0) < 0.0001


def hitung_nilai_akhir(tugas, uts, uas):
    """Hitung nilai akhir dari tiga komponen penilaian."""
    if not validasi_nilai(tugas):
        raise ValueError("Nilai tugas tidak valid")
    if not validasi_nilai(uts):
        raise ValueError("Nilai UTS tidak valid")
    if not validasi_nilai(uas):
        raise ValueError("Nilai UAS tidak valid")

    akhir = (tugas * BOBOT_TUGAS) + (uts * BOBOT_UTS) + (uas * BOBOT_UAS)
    return round(akhir, 2)


def tentukan_huruf(nilai):
    """Ubah nilai angka menjadi huruf mutu."""
    if nilai >= 85:
        return "A"
    if nilai >= 75:
        return "AB"
    if nilai >= 65:
        return "B"
    if nilai >= NILAI_LULUS:
        return "BC"
    if nilai >= 50:
        return "C"
    if nilai >= 40:
        return "D"
    return "E"


def status_kelulusan(nilai):
    """Tentukan apakah mahasiswa lulus."""
    if nilai >= NILAI_LULUS:
        return "LULUS"
    return "TIDAK LULUS"


def ringkas_mahasiswa(mahasiswa):
    """Buat ringkasan satu mahasiswa dalam bentuk teks."""
    nilai = hitung_nilai_akhir(
        mahasiswa["tugas"],
        mahasiswa["uts"],
        mahasiswa["uas"],
    )
    huruf = tentukan_huruf(nilai)
    status = status_kelulusan(nilai)
    return f"{mahasiswa['nama']}: {nilai} ({huruf}) - {status}"


def rata_rata(daftar_nilai):
    """Hitung rata-rata dari sebuah daftar nilai."""
    if not daftar_nilai:
        return 0
    return round(sum(daftar_nilai) / len(daftar_nilai), 2)


def nilai_tertinggi(daftar_mahasiswa):
    """Cari mahasiswa dengan nilai akhir tertinggi."""
    if not daftar_mahasiswa:
        return None

    terbaik = None
    nilai_terbaik = -1
    for mahasiswa in daftar_mahasiswa:
        nilai = hitung_nilai_akhir(
            mahasiswa["tugas"],
            mahasiswa["uts"],
            mahasiswa["uas"],
        )
        if nilai > nilai_terbaik:
            nilai_terbaik = nilai
            terbaik = mahasiswa
    return terbaik


def nilai_terendah(daftar_mahasiswa):
    """Cari mahasiswa dengan nilai akhir terendah."""
    if not daftar_mahasiswa:
        return None

    terendah = None
    nilai_terendah_ = 101
    for mahasiswa in daftar_mahasiswa:
        nilai = hitung_nilai_akhir(
            mahasiswa["tugas"],
            mahasiswa["uts"],
            mahasiswa["uas"],
        )
        if nilai < nilai_terendah_:
            nilai_terendah_ = nilai
            terendah = mahasiswa
    return terendah


def kelompokkan_nilai(daftar_mahasiswa):
    """Kelompokkan mahasiswa berdasarkan huruf mutu."""
    kelompok = {}
    for mahasiswa in daftar_mahasiswa:
        nilai = hitung_nilai_akhir(
            mahasiswa["tugas"],
            mahasiswa["uts"],
            mahasiswa["uas"],
        )
        huruf = tentukan_huruf(nilai)
        if huruf not in kelompok:
            kelompok[huruf] = []
        kelompok[huruf].append(mahasiswa["nama"])
    return kelompok


def simpan_ke_json(daftar_mahasiswa, path):
    """Simpan daftar mahasiswa ke berkas JSON."""
    tujuan = Path(path)
    data = []
    for mahasiswa in daftar_mahasiswa:
        nilai = hitung_nilai_akhir(
            mahasiswa["tugas"],
            mahasiswa["uts"],
            mahasiswa["uas"],
        )
        data.append(
            {
                "nama": mahasiswa["nama"],
                "nilai_akhir": nilai,
                "huruf": tentukan_huruf(nilai),
            }
        )
    tujuan.write_text(json.dumps(data, indent=2), encoding="utf-8")


def baca_dari_json(path):
    """Baca daftar mahasiswa dari berkas JSON."""
    sumber = Path(path)
    if not sumber.exists():
        return []
    return json.loads(sumber.read_text(encoding="utf-8"))


class BukuNilai:
    """Kelas untuk mengelola daftar mahasiswa dan nilainya."""

    def __init__(self):
        self.daftar = []

    def tambah(self, nama, tugas, uts, uas):
        """Tambahkan satu mahasiswa ke buku nilai."""
        mahasiswa = {
            "nama": nama,
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
        }
        self.daftar.append(mahasiswa)
        return mahasiswa

    def jumlah(self):
        """Kembalikan banyaknya mahasiswa."""
        return len(self.daftar)

    def ringkasan(self):
        """Cetak ringkasan semua mahasiswa."""
        for mahasiswa in self.daftar:
            print(ringkas_mahasiswa(mahasiswa))

    def rata_rata_kelas(self):
        """Hitung rata-rata nilai akhir seluruh kelas."""
        semua = []
        for mahasiswa in self.daftar:
            nilai = hitung_nilai_akhir(
                mahasiswa["tugas"],
                mahasiswa["uts"],
                mahasiswa["uas"],
            )
            semua.append(nilai)
        return rata_rata(semua)

    def juara_kelas(self):
        """Kembalikan nama mahasiswa dengan nilai tertinggi."""
        terbaik = nilai_tertinggi(self.daftar)
        if terbaik is None:
            return None
        return terbaik["nama"]


def main():
    """Contoh pemakaian modul."""
    buku = BukuNilai()
    buku.tambah("Ani", 80, 75, 90)
    buku.tambah("Budi", 60, 65, 70)
    buku.tambah("Citra", 95, 88, 92)

    print("Jumlah mahasiswa:", buku.jumlah())
    buku.ringkasan()
    print("Rata-rata kelas:", buku.rata_rata_kelas())
    print("Juara kelas:", buku.juara_kelas())
    print("Kelompok:", kelompokkan_nilai(buku.daftar))


if __name__ == "__main__":
    main()
