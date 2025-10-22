import unittest
from import_setup import add_src_to_path

add_src_to_path()
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_tags(self):
        tags = ["p", "div", "h1"]
        for tag in tags:
            node = LeafNode(tag, f"This is a {tag}.")
            self.assertEqual(node.to_html(), f"<{tag}>This is a {tag}.</{tag}>")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "This is a link.", {"href": "https://x.com/home", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://x.com/home" target="_blank">This is a link.</a>')

    def test_leaf_to_html_notag(self):
        node = LeafNode(None, "This is only value.")
        self.assertEqual(node.to_html(), "This is only value.")

    def test_leaf_repr(self):
        node = LeafNode("h1", "This is a headline")
        self.assertEqual("LeafNode(h1, This is a headline, None)", repr(node))



if __name__ == "__main__":
    unittest.main()