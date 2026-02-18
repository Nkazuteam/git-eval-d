# Text Analyzer

テキストの統計情報（文字数、単語数、行数、文数、単語頻度）を解析する Python ツール。

## セットアップ

```bash
pip install -r requirements.txt
```

## 使い方

```bash
# ファイルを解析
python -m src.cli sample.txt

# 標準入力から解析
echo "Hello world" | python -m src.cli

# 単語頻度も表示
python -m src.cli --freq --top 5 sample.txt
```

## テスト

```bash
pytest tests/ -v
```

## リンター

```bash
flake8 src/
```
