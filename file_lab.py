import sys
from pathlib import Path
import json
import csv


def read_csv(file_path):
    with file_path.open() as f:
        reader = csv.DictReader(f)
        return list(reader)

def read_json(file_path):
    return json.loads(file_path.read_text())

def read_jsonl(file_path):
    rows = []
    for line in file_path.read_text().splitlines():
        rows.append(json.loads(line))
    return rows

def read_file(file_path):
    return file_path.read_text()

def get_file_type(file_path):
    return file_path.suffix 

def filter_by_category(rows,category):
    filtered_rows = []

    for row in rows:
        if row["category"] == category:
            filtered_rows.append(row)
    return filtered_rows

def print_usage():
      print("Usage:")
      print("  python file_lab.py read <file_path>")
      print("  python file_lab.py read-json <file_path>")
      print("  python file_lab.py read-csv <file_path>")
      print("  python file_lab.py read-jsonl <file_path>")
      print("  python file_lab.py type <file_path>")
      print("  python file_lab.py filter <file_path> <category>")

def main():
    if len(sys.argv) < 2:
        print_usage()
        return
    command = sys.argv[1]
    if command == "filter":
        if len(sys.argv) != 5:
            print_usage()
            return
        if sys.argv[3] != "--category":
            print_usage()
            return
        file_path = Path(sys.argv[2])
        category = sys.argv[4]
        if not file_path.exists():
            print_usage()
            return

        rows = read_jsonl(file_path)
        filtered_rows = filter_by_category(rows,category)
        print(filtered_rows)
        return

    if len(sys.argv) != 3:
        print_usage()
        return
    
    file_path = Path(sys.argv[2])
    
    
    if not file_path.exists():
        print_usage()
        return
    if command == "read":
        text = read_file(file_path)
        print(text)
        return
    elif command == "read-json":
        data = read_json(file_path)
        print(data)
        return
    elif command == "read-csv":
        rows = read_csv(file_path)
        print(rows)
        return
    elif command == "read-jsonl":
        rows = read_jsonl(file_path)
        print(rows)
        return
    elif command == "type":
        file_type = get_file_type(file_path)
        print(file_type)
        return

    else:    
        print_usage()
   


if __name__ == "__main__":
    main()
