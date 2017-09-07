from unittest import TestCase
from word_count import create_word_dict

class TestClean_text(TestCase):

    def test_word_count_ignore_capital_case(self):
        f = "text_examples/f1.txt"
        word_dict = create_word_dict(f)
        assert "hello" in word_dict and word_dict['hello'] == 3

    def test_word_count_ignore_punctuation(self):
        f = "text_examples/f2.txt"
        word_dict = create_word_dict(f)
        assert "hello" in word_dict and word_dict['hello'] == 3

    def test_word_count_file_too_big_for_memory(self):
        f = "text_examples/f3.txt"
        # Read 8 bytes at the time.
        word_dict = create_word_dict(f, buff_size=8)
        assert "hello" in word_dict
        assert "world" in word_dict
        assert "this" in word_dict
        assert "text" in word_dict
        assert "will" in word_dict
        assert "be" in word_dict
        assert "read" in word_dict
        assert "in" in word_dict
        assert "chunks" in word_dict
