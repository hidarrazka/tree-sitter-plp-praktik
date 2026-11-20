import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

DIR = Path(__file__).resolve().parent


def parse_xml(path):
    cli = shutil.which("tree-sitter")
    if cli is None:
        raise SystemExit("tree-sitter CLI tidak ditemukan di PATH")
    hasil = subprocess.run(
        [cli, "parse", "-x", str(path)],
        cwd=DIR,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if hasil.returncode != 0:
        raise SystemExit(hasil.stderr)
    return ET.fromstring(hasil.stdout)


def anak(elem, nama_field):
    for child in elem:
        if child.get("field") == nama_field:
            return child
    return None


def nilai(elem):
    teks = (elem.text or "").strip()
    if elem.tag == "string":
        return teks[1:-1]
    if elem.tag == "number":
        return float(teks) if "." in teks else int(teks)
    if elem.tag == "boolean":
        return teks == "true"
    raise ValueError(f"nilai tidak dikenal: {elem.tag}")


def bangun(elem, params):
    tag = elem.tag

    if tag == "comparison":
        kolom = anak(elem, "field")
        value = anak(elem, "value")
        op = kolom.tail.strip()
        if op == "!=":
            op = "<>"
        params.append(nilai(value))
        return f"{kolom.text} {op} ?"

    if tag == "and_expression":
        kiri = bangun(anak(elem, "left"), params)
        kanan = bangun(anak(elem, "right"), params)
        return f"({kiri} AND {kanan})"

    if tag == "or_expression":
        kiri = bangun(anak(elem, "left"), params)
        kanan = bangun(anak(elem, "right"), params)
        return f"({kiri} OR {kanan})"

    if tag == "not_expression":
        operand = bangun(anak(elem, "operand"), params)
        if operand.startswith("(") and operand.endswith(")"):
            return f"NOT {operand}"
        return f"NOT ({operand})"

    if tag == "parenthesized":
        dalam = list(elem)[0]
        return bangun(dalam, params)

    if tag == "in_expression":
        kolom = anak(elem, "field")
        daftar = anak(elem, "values")
        penanda = ", ".join("?" for _ in list(daftar))
        for item in list(daftar):
            params.append(nilai(item))
        return f"{kolom.text} IN ({penanda})"

    if tag == "contains_expression":
        kolom = anak(elem, "field")
        value = anak(elem, "value")
        params.append(f"%{nilai(value)}%")
        return f"{kolom.text} LIKE ?"

    raise ValueError(f"node tidak dikenal: {tag}")


def main():
    if len(sys.argv) < 2:
        print("Pakai: python sql_where.py <file.filter>")
        return

    root = parse_xml(sys.argv[1])
    query = root.find(".//query")
    if query is None or len(query) == 0:
        print("Tidak ada query di file.")
        return

    params = []
    ekspresi = bangun(list(query)[0], params)
    print(f"WHERE {ekspresi};")
    print(f"Params: {params}")


if __name__ == "__main__":
    main()
