"""テキスト解析モジュール。

文字数、単語数、行数などの基本的なテキスト統計を計算する。
"""

import re
from collections import Counter


def count_characters(text):
    """テキストの文字数を返す（空白を含む）。"""
    return len(text)


def count_characters_no_spaces(text):
    """テキストの文字数を返す（空白を除く）。"""
    return len(text.replace(" ", "").replace("\t", "").replace("\n", ""))


def count_words(text):
    """テキストの単語数を返す。

    日本語と英語の両方に対応。英語は空白区切り、
    日本語は連続する非ASCII文字を1単語として数える。
    """
    if not text.strip():
        return 0

    words = re.findall(r'[a-zA-Z]+|[^\s\x00-\x7F]+', text)
    return len(words)


def count_lines(text):
    """テキストの行数を返す。空文字列の場合は0。"""
    if not text:
        return 0
    return text.count("\n") + 1


def count_sentences(text):
    """テキストの文の数を返す。

    句点（。）、ピリオド（.）、感嘆符（!）、疑問符（?）で区切る。
    """
    if not text.strip():
        return 0

    sentences = re.split(r'[。.!?！？]+', text.strip())
    return len([s for s in sentences if s.strip()])


def count_paragraphs(text):
    """テキストの段落数を返す。空行で区切られたブロックを段落とする。"""
    if not text.strip():
        return 0
    paragraphs = re.split(r'\n\s*\n', text.strip())
    return len([p for p in paragraphs if p.strip()])


def get_word_frequencies(text, top_n=10):
    """テキスト内の単語出現頻度を返す。

    Args:
        text: 解析対象のテキスト
        top_n: 上位何件を返すか

    Returns:
        出現頻度の高い順に (単語, 回数) のリスト
    """
    words = re.findall(r'[a-zA-Z]+|[^\s\x00-\x7F]+', text.lower())
    if not words:
        return []
    return Counter(words).most_common(top_n)


def analyze(text):
    """テキストの総合的な統計情報を辞書で返す。"""
    return {
        "characters": count_characters(text),
        "characters_no_spaces": count_characters_no_spaces(text),
        "words": count_words(text),
        "lines": count_lines(text),
        "sentences": count_sentences(text),
        "paragraphs": count_paragraphs(text),
    }
