from unittest import TestCase
from word_count import clean_text

punctuation = [".", "!", "?"]


class TestClean_text(TestCase):
    def test_clean_text_punctuation_end(self):
        text = "hello world."
        assert clean_text(text, punctuation) == "hello world"

    def test_clean_text_punctuation_removed(self):
        text = "hello! world"
        assert clean_text(text, "hello world")

    def test_clean_text_punctuation_standalone(self):
        text = "hello ! world"
        assert clean_text(text, punctuation) == "hello world"

    def test_clean_text_punctuation_standalone_sequence(self):
        text = "hello !! world"
        assert clean_text(text, punctuation) == "hello world"
