# File Lab

Pythonでファイルの読み書きとCLIの基本を学ぶための小さなプロジェクトです。

このプロジェクトでは、`txt`, `csv`, `json`, `jsonl` を読み込み、JSONLデータを `category` で絞り込むCLIツールを作ります。

## 目的

このプロジェクトの目的は、完成したツールを作ることだけではありません。

ファイルを読む処理、コマンドライン引数、データ形式ごとの違い、テスト、エラー処理を小さく分解して理解することが目的です。

## 今できること

- txtファイルを読む
- JSONファイルを読む
- CSVファイルを読む
- JSONLファイルを読む
- ファイルの拡張子を表示する
- JSONLを `category` で絞り込む
- 関数単位のテストを実行する
- CLIとして実行した結果をテストする

## セットアップ

このプロジェクトでは `uv` を使います。

依存関係は `pyproject.toml` と `uv.lock` で管理します。

```bash
uv sync
```

## 使い方

### txtファイルを読む

```bash
uv run python file_lab.py read data/sample.txt
```

期待する出力:

```text
hello file lab
```

### JSONファイルを読む

```bash
uv run python file_lab.py read-json data/sample.json
```

期待する出力:

```text
{'name': 'Alice', 'category': 'math', 'score': 90}
```

### CSVファイルを読む

```bash
uv run python file_lab.py read-csv data/sample.csv
```

期待する出力:

```text
[{'name': 'Alice', 'category': 'math', 'score': '90'}, {'name': 'Bob', 'category': 'english', 'score': '80'}]
```

CSVは基本的に文字として読まれるため、`score` は `"90"` のような文字列になります。

### JSONLファイルを読む

```bash
uv run python file_lab.py read-jsonl data/sample.jsonl
```

期待する出力:

```text
[{'name': 'Alice', 'category': 'math', 'score': 90}, {'name': 'Bob', 'category': 'english', 'score': 80}]
```

JSONLは、1行ごとに1つのJSONが入っている形式です。

### ファイルの拡張子を表示する

```bash
uv run python file_lab.py type data/sample.txt
```

期待する出力:

```text
.txt
```

### JSONLをcategoryで絞り込む

```bash
uv run python file_lab.py filter data/sample.jsonl --category math
```

期待する出力:

```text
[{'name': 'Alice', 'category': 'math', 'score': 90}]
```

## テスト

テストは `pytest` で実行します。

```bash
uv run python -m pytest
```

テストでは、次のようなことを確認します。

- `read_file()` がtxtファイルを読めること
- `get_file_type()` が拡張子を返せること
- `read_json()` がJSONをPythonの辞書として読めること
- `read_csv()` がCSVを辞書のリストとして読めること
- `read_jsonl()` がJSONLを辞書のリストとして読めること
- `filter_by_category()` が指定したcategoryだけを残せること
- CLIからfilterを実行できること

## ファイル構成

```text
01.file_lab/
├── data/
│   ├── sample.txt
│   ├── sample.json
│   ├── sample.csv
│   └── sample.jsonl
├── tests/
│   └── test_read.py
├── file_lab.py
├── pyproject.toml
├── uv.lock
├── project.md
└── README.md
```

## コードの流れ

このツールは、まずコマンドライン引数を読みます。

たとえば次のコマンドを実行します。

```bash
uv run python file_lab.py filter data/sample.jsonl --category math
```

Pythonの中では、だいたい次のように見えます。

```python
[
    "file_lab.py",
    "filter",
    "data/sample.jsonl",
    "--category",
    "math",
]
```

そのあと、`main()` が次の順番で処理します。

1. コマンド名を確認する
2. 引数の数が正しいか確認する
3. ファイルが存在するか確認する
4. コマンドに対応する関数を呼ぶ
5. 結果を表示する

`filter` コマンドの場合は、次の流れです。

```text
read_jsonl(file_path)
  JSONLファイルを読む

filter_by_category(rows, category)
  categoryが一致する行だけ残す

print(filtered_rows)
  結果を画面に表示する
```

## 学んだこと

- `sys.argv` でCLI引数を受け取る
- `pathlib.Path` でファイルパスを扱う
- `read_text()` でテキストファイルを読む
- `json.loads()` でJSON文字列をPythonのデータに変換する
- `csv.DictReader` でCSVを辞書として読む
- `for` で複数行のデータを1つずつ処理する
- `if / elif / else` でコマンドごとに処理を分ける
- `pytest` で関数の動作を確認する
- `subprocess` でCLI全体の動作を確認する

## 次に改善できること

- `argparse` を使ってCLI引数の処理を整理する
- JSONやCSVの出力を見やすく整形する
- ファイル読み込み時の文字コードを明示する
- 不正なJSONやCSVに対するエラー処理を追加する
- `src/` 構成に分けて、プロジェクト構造をより実務的にする
