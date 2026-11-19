import sys
from pathlib import Path

import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)

Q_TODO = Query(PY, '((comment) @c (#match? @c "TODO|FIXME"))')
Q_FUNGSI = Query(PY, '(function_definition name: (identifier) @nama) @fungsi')


FOLDER_DILEWATI = {"venv", ".venv", ".git", "node_modules", "__pycache__"}


def cek_todo(path, tree):
    for node in QueryCursor(Q_TODO).captures(tree.root_node).get("c", []):
        teks = node.text.decode(errors="replace").strip()
        print(f"{path}:{node.start_point[0] + 1}: {teks}")


def cek_file(path):
    tree = parser.parse(path.read_bytes())
    cek_todo(path, tree)

def cek_fungsi_panjang(path, tree):
    for _, cap in QueryCursor(Q_FUNGSI).matches(tree.root_node):
        fungsi = cap["fungsi"][0]
        nama = cap["nama"][0].text.decode(errors="replace")
        jumlah_baris = fungsi.end_point[0] - fungsi.start_point[0] + 1
        if jumlah_baris > 30:
            baris = fungsi.start_point[0] + 1
            print(f"{path}:{baris}: fungsi '{nama}' {jumlah_baris} baris")

def cek_file(path):
    tree = parser.parse(path.read_bytes())
    cek_todo(path, tree)
    cek_fungsi_panjang(path, tree)


def main():
    if len(sys.argv) < 2:
        print("Pakai: python cek.py <folder>")
        return

    folder = Path(sys.argv[1])
    for path in folder.rglob("*.py"):
        if any(bagian in FOLDER_DILEWATI for bagian in path.parts):
            continue
        cek_file(path)


if __name__ == "__main__":
    main()
