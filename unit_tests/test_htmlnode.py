import unittest
from import_setup import add_src_to_path

add_src_to_path()

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr1(self):
        node = HTMLNode()
        self.assertEqual("HTMLNode(None, None, children: None, None)", repr(node))

    def test_repr2(self):
        node = HTMLNode("h1", "HEADLINE", [], {"href": "https://x.com/home", "target":"_blank"})
        self.assertEqual("HTMLNode(h1, HEADLINE, children: [], {'href': 'https://x.com/home', 'target': '_blank'})", repr(node))

    def test_repr2_false(self):
        node = HTMLNode("h1", "HEADLINE", [], {})
        self.assertNotEqual("HTMLNode(h1, HEADLINE, children: [], {'href': 'https://x.com/home', 'target': '_blank'})", repr(node))

    def test_values(self):
        node = HTMLNode("div", "Textio")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Textio")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_props_to_html(self):
        node = HTMLNode("h1", "HEADLINE", [], {"href": "https://x.com/home", "target":"_blank"})
        self.assertEqual(' href="https://x.com/home" target="_blank"', node.props_to_html())

    def test_props_to_html_false(self):
        node = HTMLNode("h1", "HEADLINE", [], {"href": "https://x.com/home", "target":"_blank"})
        self.assertNotEqual(' href="https://x.com/home"target="_blank"', node.props_to_html())

    

if __name__ == "__main__":
    unittest.main()