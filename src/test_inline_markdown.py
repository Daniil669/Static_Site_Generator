import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.PLAIN_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" word", TextType.PLAIN_TEXT),
        ])


    def test_split_nodes_delimiter_bold(self):
        node = TextNode("**This text is bold**", TextType.BOLD_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(new_nodes, [
            TextNode("**This text is bold**", TextType.BOLD_TEXT)
        ])


    def test_split_nodes_delimiter_many_nodes(self):
        node1 = TextNode("This is _italic words_ in here and _italic_ here", TextType.PLAIN_TEXT)
        node2 = TextNode("Just some _ no code inside this line _, and that it", TextType.PLAIN_TEXT)
        node3 = TextNode("No italy, but _ italic text _ ", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node1, node2, node3], "_", TextType.ITALIC_TEXT)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.PLAIN_TEXT),
            TextNode("italic words", TextType.ITALIC_TEXT),
            TextNode(" in here and ", TextType.PLAIN_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" here", TextType.PLAIN_TEXT),
            TextNode("Just some ", TextType.PLAIN_TEXT),
            TextNode(" no code inside this line ", TextType.ITALIC_TEXT),
            TextNode(", and that it", TextType.PLAIN_TEXT),
            TextNode("No italy, but ", TextType.PLAIN_TEXT),
            TextNode(" italic text ", TextType.ITALIC_TEXT),
            TextNode(" ", TextType.PLAIN_TEXT)
        ])

    def test_split_nodes_delimiter_code_and_bold(self):
        node = TextNode("Let's test `code thing` and **bold**", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD_TEXT)
        self.assertEqual(new_nodes, [
            TextNode("Let's test ", TextType.PLAIN_TEXT),
            TextNode("code thing", TextType.CODE_TEXT),
            TextNode(" and ", TextType.PLAIN_TEXT),
            TextNode("bold", TextType.BOLD_TEXT)
        ])

class TestExtractImages(unittest.TestCase):
    def test_extract_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ])

    def test_extract_images_no_images(self):
        text = "This is a simple (text) and it [has] no links!"
        images = extract_markdown_images(text)
        self.assertEqual(images, [])

    def test_extract_images_syntex_problem(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif and obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [])


    def test_extract_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ])

    def test_extract_images_no_links(self):
        text = "This is a simple (text) and it [has] no links!"
        links = extract_markdown_links(text)
        self.assertEqual(links, [])

if __name__ == "__main__":
    unittest.main()