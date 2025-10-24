import unittest
from import_setup import add_src_to_path

add_src_to_path()

from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quotes(self):
        md = """
> Quote _1_ **alright** !
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,
                         "<div><backquote>Quote <i>1</i> <b>alright</b> !</backquote></div>")
        
    def test_heading(self):
        for i in range(1, 7):
            heading = "#" * i+ " " + "Heading"
            node = markdown_to_html_node(heading)
            html = node.to_html()
            self.assertEqual(html, f"<div><h{i}>Heading</h{i}></div>")

    def test_ordered_list(self):
        md = """
1. This is **bolded** item
2. text in a p
3. This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is <b>bolded</b> item</li><li>text in a p</li><li>This is another paragraph with <i>italic</i> text and <code>code</code> here</li></ol></div>",
        )

    def test_unordered_list(self):
        md = """
- This is **bolded** item
- text in a p
- This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is <b>bolded</b> item</li><li>text in a p</li><li>This is another paragraph with <i>italic</i> text and <code>code</code> here</li></ul></div>",
        )



if __name__ == "__main__":
    unittest.main()