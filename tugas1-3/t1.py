import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))

POTONGAN = {
    "1. Fungsi": b"""def sapa(nama):
    return "Halo " + nama
""",
    "2. If/Else": b"""nilai = 80
if nilai >= 75:
    status = "lulus"
else:
    status = "tidak lulus"
""",
    "3. Kelas dengan satu method": b"""class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
""",
}


def tampilkan_pohon(judul, kode):
    print("=" * 60)
    print(judul)
    print("=" * 60)
    tree = parser.parse(kode)
    print(tree.root_node)
    print()


def tampilkan_anonim(kode):
    tree = parser.parse(kode)
    fungsi = tree.root_node.children[0]

    print("Anak langsung node function_definition:")
    for anak in fungsi.children:
        jenis = "bernama" if anak.is_named else "anonim"
        print(f"  {anak.type:12s} {jenis}")
    print()

    print("Anak node parameters (tanda kurung ada di sini):")
    parameters = fungsi.child_by_field_name("parameters")
    for anak in parameters.children:
        jenis = "bernama" if anak.is_named else "anonim"
        print(f"  {anak.type:12s} {jenis}")
    print()


def cari_masalah(node):
    hasil = []
    if node.is_error or node.is_missing:
        hasil.append(node)
    for anak in node.children:
        hasil.extend(cari_masalah(anak))
    return hasil


def tampilkan_error():
    contoh = [
        ("4a. Tanda ':' dihapus", b"def sapa(nama)\n    return nama\n"),
        ("4b. Parameter dan ')' dihapus", b"def sapa(:\n    return nama\n"),
    ]

    for judul, kode in contoh:
        print("=" * 60)
        print(judul)
        print("=" * 60)
        print(kode.decode())
        print("Pohon yang dihasilkan:")
        tree = parser.parse(kode)
        print(tree.root_node)
        print()

        print("Node bermasalah yang ditemukan:")
        for node in cari_masalah(tree.root_node):
            jenis = "MISSING" if node.is_missing else "ERROR"
            baris, kolom = node.start_point
            print(f"  {jenis}: {node.type} di baris {baris + 1}, kolom {kolom}")
        print()


for judul, kode in POTONGAN.items():
    tampilkan_pohon(judul, kode)

tampilkan_anonim(POTONGAN["1. Fungsi"])
tampilkan_error()
