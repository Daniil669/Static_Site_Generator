import unittest
from import_setup import add_src_to_path

add_src_to_path()

from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdowndToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md: str = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
            """
        blocks: list[str] = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    

    def test_block_to_block_paragraph(self):
        markdown_text = "This is **bolded** paragraph"
        block_type = block_to_block_type(markdown_text)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_headlines(self):
        markdown_text = " Headline"
        for i in range(1, 7):
            heading = "#"*i+markdown_text
            block_type = block_to_block_type(heading)
            self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_code(self):
        code = """```
                {
                "firstName": "John",
                "lastName": "Smith",
                "age": 25
                }
                ```"""
        block_type = block_to_block_type(code)
        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_block_quote(self):
        quote = """> Amazing quote\n> Amazing quote 2\n> Amazing quote 3"""
        block_types = block_to_block_type(quote)
        self.assertEqual(block_types, BlockType.QUOTE)

    def test_block_to_block_ordered_list(self):
        ordred_list = """1. Item\n2. Item2\n3. Item3"""
        block_types = block_to_block_type(ordred_list)
        self.assertEqual(block_types, BlockType.ORDERED_LIST)

    def test_block_to_block_unordered_list(self):
        ordred_list = """- Item **bold**\n- Item2\n- Item3"""
        block_types = block_to_block_type(ordred_list)
        self.assertEqual(block_types, BlockType.UNORDERED_LIST)

    def test_block_to_block_ordered_list_false(self):
        ordred_list_false = """1. Item\n2. Item2\n4. Item3"""
        block_types = block_to_block_type(ordred_list_false)
        self.assertNotEqual(block_types, BlockType.ORDERED_LIST)

    

    

if __name__ == "__main__":
    unittest.main()