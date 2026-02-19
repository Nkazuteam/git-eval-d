"""analyzer モジュールのテスト。"""

import pytest

from src.analyzer import (
    analyze,
    count_characters,
    count_characters_no_spaces,
    count_lines,
    count_paragraphs,
    count_sentences,
    count_words,
    get_word_frequencies,
)


class TestCountCharacters:
    def test_empty_string(self):
        assert count_characters("") == 0

    def test_ascii_text(self):
        assert count_characters("hello") == 5

    def test_includes_spaces(self):
        assert count_characters("hello world") == 11

    def test_japanese_text(self):
        assert count_characters("こんにちは") == 5


class TestCountCharactersNoSpaces:
    def test_empty_string(self):
        assert count_characters_no_spaces("") == 0

    def test_removes_spaces(self):
        assert count_characters_no_spaces("hello world") == 10

    def test_removes_tabs_and_newlines(self):
        assert count_characters_no_spaces("a\tb\nc") == 3


class TestCountWords:
    def test_empty_string(self):
        assert count_words("") == 0

    def test_whitespace_only(self):
        assert count_words("   \n\t  ") == 0

    def test_english_words(self):
        assert count_words("hello world foo") == 3

    def test_japanese_text(self):
        assert count_words("こんにちは世界") == 1

    def test_mixed_text(self):
        assert count_words("hello こんにちは world") == 3


class TestCountLines:
    def test_empty_string(self):
        assert count_lines("") == 0

    def test_single_line(self):
        assert count_lines("hello") == 1

    def test_multiple_lines(self):
        assert count_lines("line1\nline2\nline3") == 3


class TestCountSentences:
    def test_empty_string(self):
        assert count_sentences("") == 0

    def test_single_sentence_period(self):
        assert count_sentences("Hello world.") == 1

    def test_multiple_sentences(self):
        assert count_sentences("First. Second. Third.") == 3

    def test_japanese_sentences(self):
        assert count_sentences("最初の文。次の文。最後。") == 3

    def test_mixed_punctuation(self):
        assert count_sentences("Really? Yes! OK.") == 3


class TestCountParagraphs:
    def test_empty_string(self):
        assert count_paragraphs("") == 0

    def test_single_paragraph(self):
        assert count_paragraphs("Hello world.") == 1

    def test_multiple_paragraphs(self):
        text = "First paragraph.\n\nSecond paragraph.\n\nThird."
        assert count_paragraphs(text) == 3

    def test_ignores_single_newlines(self):
        text = "Line one.\nLine two."
        assert count_paragraphs(text) == 1


class TestGetWordFrequencies:
    def test_empty_string(self):
        assert get_word_frequencies("") == []

    def test_word_counts(self):
        result = get_word_frequencies("apple banana apple cherry apple banana")
        assert result[0] == ("apple", 3)
        assert result[1] == ("banana", 2)

    def test_top_n_limit(self):
        text = "a b c d e f g h i j k"
        result = get_word_frequencies(text, top_n=3)
        assert len(result) == 3

    def test_case_insensitive(self):
        result = get_word_frequencies("Hello hello HELLO")
        assert result[0] == ("hello", 3)


class TestAnalyze:
    def test_returns_all_keys(self):
        result = analyze("Hello world.")
        expected_keys = {
            "characters",
            "characters_no_spaces",
            "words",
            "lines",
            "sentences",
            "paragraphs",
        }
        assert set(result.keys()) == expected_keys

    def test_values_are_correct(self):
        result = analyze("Hello world.")
        assert result["characters"] == 12
        assert result["characters_no_spaces"] == 11
        assert result["words"] == 2
        assert result["lines"] == 1
        assert result["sentences"] == 1
