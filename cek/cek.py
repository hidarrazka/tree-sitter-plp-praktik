import sys
from pathlib import Path

import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)

Q_TODO = Query(PY, '((comment) @c (#match? @c "TODO|FIXME"))')

FOLDER_DILEWATI = {"venv", ".venv", ".git", "node_modules", "__pycache__"}


def cek_todo(path, tree):
    for node in QueryCursor(Q_TODO).captures(tree.root_node).get("c", []):
        teks = node.text.decode(errors="replace").strip()
        print(f"{path}:{node.start_point[0] + 1}: {teks}")


def cek_file(path):
    tree = parser.parse(path.read_bytes())
    cek_todo(path, tree)


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
