"""CLI モジュールのテスト。"""

from src.cli import format_report


class TestFormatReport:
    def test_basic_report(self):
        stats = {
            "characters": 100,
            "characters_no_spaces": 80,
            "words": 20,
            "lines": 5,
            "sentences": 3,
        }
        report = format_report(stats)
        assert "文字数:         100" in report
        assert "単語数:         20" in report
        assert "行数:           5" in report

    def test_report_with_frequencies(self):
        stats = {
            "characters": 10,
            "characters_no_spaces": 8,
            "words": 3,
            "lines": 1,
            "sentences": 1,
        }
        frequencies = [("hello", 5), ("world", 3)]
        report = format_report(stats, frequencies)
        assert "単語出現頻度" in report
        assert "hello: 5" in report
        assert "world: 3" in report

    def test_report_without_frequencies(self):
        stats = {
            "characters": 0,
            "characters_no_spaces": 0,
            "words": 0,
            "lines": 0,
            "sentences": 0,
        }
        report = format_report(stats)
        assert "単語出現頻度" not in report
