# Tugas 1–3

Semua skrip memakai binding Python `tree-sitter` + grammar `tree-sitter-python`.

## Cara menjalankan

```powershell
python t1.py                                  # Tugas 1: pohon, node anonim, ERROR/MISSING
python -c "import tree_sitter_python, tree_sitter"   # cek dependensi

python jelajah.py contoh.py                    # Tugas 2: penjelajah rekursif
python jelajah.py contoh_nyata.py
python jelajah_cursor.py contoh_nyata.py       # pengayaan: TreeCursor

python q.py contoh.py nama_fungsi.scm          # Tugas 3: nama fungsi
python q_params.py contoh.py nama_fungsi_params.scm
python q.py contoh.py panggilan_print.scm
python q.py contoh.py import.scm
python q.py contoh.py docstring.scm            # pengayaan: docstring
```

Di Windows, jika keluaran ke file berisi karakter aneh, set encoding lebih dulu:

```powershell
cmd /c "set PYTHONUTF8=1&& python q.py contoh.py nama_fungsi.scm > output\q_nama_fungsi.txt"
```

## Keluaran

| File | Isi |
| --- | --- |
| `output/t1.txt` | Pohon 3 potongan, daftar node anonim, ERROR/MISSING |
| `output/jelajah_kecil.txt`, `output/jelajah_nyata.txt` | Penjelajah rekursif |
| `output/jelajah_cursor_kecil.txt`, `output/jelajah_cursor_nyata.txt` | Penjelajah TreeCursor |
| `output/q_*.txt` | Hasil query pada `contoh.py` |
| `output/q_*_nyata.txt` | Hasil query pada `contoh_nyata.py` |
| `pohon_perkiraan.txt` | Perbandingan pohon perkiraan (tulisan tangan) vs hasil |

## Verifikasi hitungan manual (Tugas 3)

Hitungan dilakukan manual pada kode sumber, lalu dicek ulang dengan modul
`ast` Python sebagai pembanding independen (bukan tree-sitter). Hasilnya
sama dengan keluaran query.

### `contoh.py` (30 baris)

| Query | Keluaran query | Hitungan manual | Cocok |
| --- | --- | --- | --- |
| `nama_fungsi.scm` | 4 nama: `hitung_luas` (7), `sapa` (14), `__init__` (19), `cetak` (22) | 4 fungsi | ya |
| `nama_fungsi_params.scm` | `hitung_luas`: 2, `sapa`: 1, `__init__`: 2, `cetak`: 1 | 2, 1, 2, 1 parameter | ya |
| `panggilan_print.scm` | 3 panggilan: baris 10, 15, 23 | 3 `print(...)` | ya |
| `import.scm` | `os` (3), `pathlib` (4) | 2 modul | ya |
| `docstring.scm` (pengayaan) | 1: baris 8 | 1 fungsi ber-docstring | ya |

### `contoh_nyata.py` (226 baris, ≥100 baris untuk Tugas 2)

| Query | Keluaran query | Hitungan manual | Cocok |
| --- | --- | --- | --- |
| `nama_fungsi.scm` | 19 nama fungsi | 19 fungsi | ya |
| `nama_fungsi_params.scm` | 19 fungsi, total 27 parameter | 19 fungsi, 27 parameter | ya |
| `panggilan_print.scm` | 5 panggilan | 5 `print(...)` | ya |
| `import.scm` | `json`, `pathlib` | 2 modul | ya |
| `docstring.scm` (pengayaan) | 18 docstring | 18 dari 19 fungsi (tanpa `__init__`) | ya |

Catatan: keluaran `panggilan_print.scm` menampilkan capture `@fn` dan `@args`
untuk setiap panggilan, jadi jumlah baris dua kali jumlah panggilan.
