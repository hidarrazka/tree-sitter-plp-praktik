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

## Uji pada repositori nyata

Repositori uji: [pallets/itsdangerous](https://github.com/pallets/itsdangerous)
(commit `672971d`, di-clone dengan `git clone --depth 1`).

Perintah dijalankan dari root repositori agar path yang dilaporkan relatif:

```bash
python <path-ke-cek.py> .
```

Hasil lengkap ada di `output/hasil_repo.txt`:

```
src\itsdangerous\serializer.py:190: fungsi '__init__' 45 baris
src\itsdangerous\signer.py:129: fungsi '__init__' 45 baris
src\itsdangerous\signer.py:182: fungsi 'derive_key' 32 baris
src\itsdangerous\timed.py:182: # TODO: Signature is incompatible because parameters were added
src\itsdangerous\timed.py:72: fungsi 'unsign' 87 baris
src\itsdangerous\timed.py:185: fungsi 'loads' 36 baris
src\itsdangerous\url_safe.py:23: fungsi 'load_payload' 31 baris
```

### Verifikasi manual 2 file

| File | Cek manual | Temuan `cek.py` | Cocok |
| --- | --- | --- | --- |
| `src/itsdangerous/url_safe.py` | `load_payload` baris 23–53 = 31 baris; tidak ada TODO/FIXME; sintaks valid | `url_safe.py:23: fungsi 'load_payload' 31 baris` | Ya |
| `src/itsdangerous/timed.py` | TODO baris 182; `unsign` baris 72–158 = 87 baris; `loads` baris 185–220 = 36 baris; sintaks valid | `timed.py:182` TODO, `timed.py:72` 87 baris, `timed.py:185` 36 baris | Ya |

Catatan: seluruh file `src/` lolos `ast.parse`, jadi tidak ada file yang dilaporkan
sebagai error pada repo ini. Itu benar, bukan bug tool.

## Catatan

- Semua fungsi dihitung, termasuk method di dalam kelas dan fungsi bersarang.
- Jumlah baris dihitung dari baris `def` sampai baris terakhir badan fungsi.
