from pathlib import Path
from file_lab import read_file
from file_lab import get_file_type
from file_lab import read_json
from file_lab import read_csv
from file_lab import read_jsonl
from file_lab import filter_by_category
import subprocess

def test_read_file():
    result = read_file(Path("data/sample.txt"))
    assert result == "hello file lab\n"
def test_get_file_type():
    result = get_file_type(Path("data/sample.txt"))
    assert result == ".txt"
def test_read_json():
    result = read_json(Path("data/sample.json"))
    assert result =={
        "name": "Alice",
        "category": "math",
        "score": 90,
    }
def test_read_csv():
    result = read_csv(Path("data/sample.csv"))
    assert result == [
        {"name": "Alice","category": "math","score": "90"},
        {"name": "Bob","category": "english", "score": "80"},
        ]
def test_read_jsonl():
    result = read_jsonl(Path("data/sample.jsonl"))
    assert result == [
        {"name": "Alice","category": "math","score": 90},
        {"name": "Bob","category": "english", "score": 80},
        ]
def test_filter_by_category():
    rows = [
          {"name": "Alice", "category": "math", "score": 90},
          {"name": "Bob", "category": "english", "score": 80},
      ]
    result = filter_by_category(rows,"math")
    assert result ==  [
          {"name": "Alice", "category": "math", "score": 90},
      ]
def test_cli_filter_by_category():
    result = subprocess.run(
        [
            "python",
            "file_lab.py",
            "filter",
            "data/sample.jsonl",
            "--category",
            "math",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "{'name': 'Alice', 'category': 'math', 'score': 90}" in result.stdout
            

    