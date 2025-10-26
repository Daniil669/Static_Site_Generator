import unittest
from import_setup import add_src_to_path

add_src_to_path()

from page_generator import extract_title

class TestPageGenerator(unittest.TestCase):
    def test_extract_title(self):
        md = """
paragraph 

## h2

# Heading/title
"""
        title = extract_title(md)
        self.assertEqual(title, "Heading/title")

    def test_eq(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

    def test_eq_double(self):
        actual = extract_title(
            """
# This is a title

# This is a second title that should be ignored
"""
        )
        self.assertEqual(actual, "This is a title")

    def test_eq_long(self):
        actual = extract_title(
            """
# title

this is a bunch

of text

- and
- a
- list
"""
        )
        self.assertEqual(actual, "title")

    def test_none(self):
        try:
            extract_title(
                """
no title
"""
            )
            self.fail("Should have raised an exception")
        except Exception as e:
            pass

if __name__ == "__main__":
    unittest.main()