import sys
import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)


def main():
    if len(sys.argv) < 3:
        print("Pakai: python q.py <file.py> <pola.scm>")
        return

    kode = open(sys.argv[1], "rb").read()
    pola = open(sys.argv[2], encoding="utf-8").read()
    tree = parser.parse(kode)

    hasil = QueryCursor(Query(PY, pola)).captures(tree.root_node)
    for nama, nodes in hasil.items():
        for n in nodes:
            teks = n.text.decode(errors="replace").splitlines()[0]
            print(f"@{nama}  baris {n.start_point[0] + 1}: {teks}")


if __name__ == "__main__":
    main()
