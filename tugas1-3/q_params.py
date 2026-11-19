import sys
import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)


def main():
    if len(sys.argv) < 3:
        print("Pakai: python q_params.py <file.py> <pola.scm>")
        return

    kode = open(sys.argv[1], "rb").read()
    pola = open(sys.argv[2], encoding="utf-8").read()
    tree = parser.parse(kode)

    for _, cap in QueryCursor(Query(PY, pola)).matches(tree.root_node):
        nama = cap["nama"][0].text.decode(errors="replace")
        params = cap.get("params", [])
        jumlah = params[0].named_child_count if params else 0
        print(f"{nama}: {jumlah} parameter")


if __name__ == "__main__":
    main()
