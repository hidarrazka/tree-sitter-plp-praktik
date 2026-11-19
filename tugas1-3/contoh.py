"""Contoh file untuk latihan query Tugas 3."""

import os
from pathlib import Path


def hitung_luas(panjang, lebar):
    """Menghitung luas persegi panjang."""
    hasil = panjang * lebar
    print("Luas:", hasil)
    return hasil


def sapa(nama):
    print("Halo", nama)


class Laporan:
    def __init__(self, judul):
        self.judul = judul

    def cetak(self):
        print(self.judul)
        os.path.exists(self.judul)


luas = hitung_luas(3, 4)
sapa("Budi")
Laporan("Harian").cetak()
Path("data.txt").exists()
