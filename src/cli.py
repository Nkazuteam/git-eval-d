"""テキスト解析の CLI エントリポイント。

標準入力またはファイルからテキストを読み取り、統計情報を表示する。
"""

import argparse
import sys

from src.analyzer import analyze, get_word_frequencies


def format_report(stats, frequencies=None):
    """統計情報を人間が読みやすい形式に整形する。"""
    lines = [
        "=== テキスト統計 ===",
        f"文字数:         {stats['characters']}",
        f"文字数(空白除く): {stats['characters_no_spaces']}",
        f"単語数:         {stats['words']}",
        f"行数:           {stats['lines']}",
        f"文数:           {stats['sentences']}",
    ]

    if frequencies:
        lines.append("")
        lines.append("=== 単語出現頻度 ===")
        for word, count in frequencies:
            lines.append(f"  {word}: {count}")

    return "\n".join(lines)


def main():
    """CLI のメインエントリポイント。"""
    parser = argparse.ArgumentParser(
        description="テキストの統計情報を表示する"
    )
    parser.add_argument(
        "file",
        nargs="?",
        help="解析するテキストファイル（省略時は標準入力）",
    )
    parser.add_argument(
        "--freq",
        action="store_true",
        help="単語出現頻度も表示する",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=10,
        help="出現頻度の上位何件を表示するか（デフォルト: 10）",
    )

    args = parser.parse_args()

    if args.file:
        with open(args.file, encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    stats = analyze(text)
    frequencies = get_word_frequencies(text, args.top) if args.freq else None
    print(format_report(stats, frequencies))


if __name__ == "__main__":
    main()
