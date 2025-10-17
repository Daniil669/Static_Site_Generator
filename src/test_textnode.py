import unittest

from textnode import TextType, TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a plain text.", TextType.PLAIN_TEXT)
        node2 = TextNode("This is a plain text.", TextType.PLAIN_TEXT)
        self.assertEqual(node1, node2)

    def test_eq_false(self):
        node1 = TextNode("Text", TextType.BOLD_TEXT)
        node2 = TextNode("Text", TextType.ITALIC_TEXT)
        self.assertNotEqual(node1, node2)

    def test_eq_false2(self):
        node1 = TextNode("Text 1", TextType.PLAIN_TEXT)
        node2 = TextNode("Text 2", TextType.PLAIN_TEXT)
        self.assertNotEqual(node1, node2)

    def test_eq_url_false(self):
        node1 = TextNode("URL", TextType.LINK, None)
        node2 = TextNode("URL", TextType.LINK, "https://x.com/home")
        self.assertNotEqual(node1, node2)

    def test_eq_url(self):
        node1 = TextNode("X", TextType.LINK, "https://x.com/home")
        node2 = TextNode("X", TextType.LINK, "https://x.com/home")
        self.assertEqual(node1, node2)

    def test_repr(self):
        node = TextNode("This is a link", TextType.LINK, "https://x.com/home")
        self.assertEqual("TextNode(This is a link, link, https://x.com/home)", repr(node))


if __name__ == "__main__":
    unittest.main()