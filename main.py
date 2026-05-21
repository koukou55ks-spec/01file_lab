  import argparse
  import csv
  import json
  from pathlib import Path


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


  def filter_by_category(rows, category):
      filtered_rows = []

      for row in rows:
          if row["category"] == category:
              filtered_rows.append(row)

      return filtered_rows


  def parse_args():
      parser = argparse.ArgumentParser(description="Read and filter files.")

      subparsers = parser.add_subparsers(dest="command", required=True)

      read_parser = subparsers.add_parser("read")
      read_parser.add_argument("file_path")

      read_json_parser = subparsers.add_parser("read-json")
      read_json_parser.add_argument("file_path")

      read_csv_parser = subparsers.add_parser("read-csv")
      read_csv_parser.add_argument("file_path")

      read_jsonl_parser = subparsers.add_parser("read-jsonl")
      read_jsonl_parser.add_argument("file_path")

      type_parser = subparsers.add_parser("type")
      type_parser.add_argument("file_path")

      filter_parser = subparsers.add_parser("filter")
      filter_parser.add_argument("file_path")
      filter_parser.add_argument("--category", required=True)

      return parser.parse_args()


  def main():
      args = parse_args()

      file_path = Path(args.file_path)

      if not file_path.exists():
          print(f"Error: file not found: {file_path}")
          return

      if args.command == "read":
          text = read_file(file_path)
          print(text)
          return

      if args.command == "read-json":
          data = read_json(file_path)
          print(data)
          return

      if args.command == "read-csv":
          rows = read_csv(file_path)
          print(rows)
          return

      if args.command == "read-jsonl":
          rows = read_jsonl(file_path)
          print(rows)
          return

      if args.command == "type":
          file_type = get_file_type(file_path)
          print(file_type)
          return

      if args.command == "filter":
          rows = read_jsonl(file_path)
          filtered_rows = filter_by_category(rows, args.category)
          print(filtered_rows)
          return


  if __name__ == "__main__":
      main()