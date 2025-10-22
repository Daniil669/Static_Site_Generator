import unittest
from import_setup import add_src_to_path

add_src_to_path()

from textnode import TextType, TextNode, text_node_to_htlm_node

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

class TestTextToHTML(unittest.TestCase):

    def test_plain_text(self):
        node = TextNode("This is a plain text", TextType.PLAIN_TEXT)
        html_node = text_node_to_htlm_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a plain text")

    def test_bold_text(self):
        node = TextNode("This is a bold text", TextType.BOLD_TEXT)
        html_node = text_node_to_htlm_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text")

    def test_italic_text(self):
        node = TextNode("This is a italic text", TextType.ITALIC_TEXT)
        html_node = text_node_to_htlm_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic text")

    def test_code(self):
        node = TextNode("This is a code", TextType.CODE_TEXT)
        html_node = text_node_to_htlm_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code")

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://x.com/home")
        html_node = text_node_to_htlm_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props, {"href": "https://x.com/home"})

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://x.com/home")
        html_node = text_node_to_htlm_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://x.com/home", "alt": "This is an image"})
    


if __name__ == "__main__":
    unittest.main()