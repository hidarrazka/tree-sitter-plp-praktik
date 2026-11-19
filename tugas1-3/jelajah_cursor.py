import sys
import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))


def jelajah_cursor(tree):
    cursor = tree.walk()
    cetak(cursor, 0)


def cetak(cursor, kedalaman):
    baris, kolom = cursor.node.start_point
    field = cursor.field_name
    label = f"{field}: " if field else ""
    print("  " * kedalaman + f"{label}{cursor.node.type} [{baris + 1}:{kolom}]")

    if not cursor.goto_first_child():
        return

    while True:
        if cursor.node.is_named:
            cetak(cursor, kedalaman + 1)
        if not cursor.goto_next_sibling():
            break

    cursor.goto_parent()


def main():
    if len(sys.argv) < 2:
        print("Pakai: python jelajah_cursor.py <file.py>")
        return

    with open(sys.argv[1], "rb") as f:
        tree = parser.parse(f.read())

    jelajah_cursor(tree)


if __name__ == "__main__":
    main()
