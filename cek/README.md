# cek.py — Pemeriksa kode Python berbasis tree-sitter

Skrip ini memeriksa seluruh file `.py` di dalam sebuah folder dan melaporkan
tiga hal:

1. Komentar yang mengandung `TODO` atau `FIXME`.
2. Fungsi yang panjangnya lebih dari 30 baris.
3. File yang pohon sintaksnya mengandung error (sintaks rusak).

## Cara memasang

```bash
python -m pip install tree-sitter tree-sitter-python
```

## Cara menjalankan

```bash
python cek.py <folder>
```

Contoh:

```bash
python cek.py uji
python cek.py <PATH_REPO_ANDA>
```

Folder `venv`, `.venv`, `.git`, `node_modules`, dan `__pycache__` otomatis
dilewati.

## Contoh output

Dari folder `uji/`:

```
uji\fungsi_panjang.py:1: fungsi 'hitung_statistik' 48 baris
uji\rusak.py:1: ERROR
uji\todo.py:1: # TODO: tambahkan validasi input
uji\todo.py:7: # TODO: buat unit test untuk fungsi ini
uji\todo.py:3: # FIXME: belum menangani tipe string
```

Dari folder/repo Python nyata milik sendiri:

```
<PATH_REPO_ANDA>\...:12: fungsi 'nama_fungsi' 42 baris
```

## Catatan

- Semua fungsi dihitung, termasuk method di dalam kelas dan fungsi bersarang.
- Jumlah baris dihitung dari baris `def` sampai baris terakhir badan fungsi.
