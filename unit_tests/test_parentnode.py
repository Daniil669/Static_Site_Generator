import unittest
from import_setup import add_src_to_path

add_src_to_path()

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_children(self):
        child = LeafNode("p", "This is paragraph.")
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><p>This is paragraph.</p></div>")

    def test_to_html_grandchild(self):
        grandchild = LeafNode("b", "Bold text.")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("p", [child])
        self.assertEqual(parent.to_html(), "<p><span><b>Bold text.</b></span></p>")

    def test_to_html_nochildren(self):
        parent = ParentNode("div", [])
        self.assertEqual(parent.to_html(), "<div></div>")

    def test_to_html_nograndchild(self):
        child = ParentNode("p", [])
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><p></p></div>")

    def test_to_html_children_props(self):
        child = LeafNode("p", "This is paragraph.", {"class": "my-paragraph"})
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), '<div><p class="my-paragraph">This is paragraph.</p></div>')

    def test_to_html_many_children(self):
        parent = ParentNode("p", [
            LeafNode(None, "This"),
            LeafNode("i", "is italic"),
            LeafNode("b", "and this is bold"),
            LeafNode(None, "text")
        ])
        self.assertEqual(parent.to_html(), "<p>This<i>is italic</i><b>and this is bold</b>text</p>")

    def test_to_html_many_grandchildren(self):
        parent = ParentNode("div", [
            ParentNode("div", [
                ParentNode("p", [
                    LeafNode(None, "This"),
                    LeafNode("i", "is italic"),
                    LeafNode("b", "and this is bold"),
                    LeafNode(None, "text") 
                ])
            ])
        ])
        self.assertEqual(parent.to_html(), "<div><div><p>This<i>is italic</i><b>and this is bold</b>text</p></div></div>")

    

if __name__ == "__main__":
    unittest.main()