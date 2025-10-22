import unittest
from import_setup import add_src_to_path

add_src_to_path()
from textnode import TextNode, TextType
from inline_markdown import (split_nodes_delimiter, extract_markdown_images, 
                             extract_markdown_links, split_nodes_image, 
                             split_nodes_link, text_to_textnodes)

class TestSplitNodesDelimiter(unittest.TestCase):
    # split_nodes_delimiter function tests
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

    # extract_markdown_images tests
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

    # extract_markdown_links tests
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

    # split_nodes_images tests
    def test_split_images1(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images2(self):
        node1 = TextNode("Images: ![image1](1) and ![image2](2). By the way, ![image1](1) is better.", TextType.PLAIN_TEXT)
        node2 = TextNode("![image_1](link1), ![image_2](link2), ![image_3](link3).", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_image([node1, node2])
        self.assertEqual(new_nodes, [
            TextNode("Images: ", TextType.PLAIN_TEXT),
            TextNode("image1", TextType.IMAGE, "1"),
            TextNode(" and ", TextType.PLAIN_TEXT),
            TextNode("image2", TextType.IMAGE, "2"),
            TextNode(". By the way, ", TextType.PLAIN_TEXT),
            TextNode("image1", TextType.IMAGE, "1"),
            TextNode(" is better.", TextType.PLAIN_TEXT),
            TextNode("image_1", TextType.IMAGE, "link1"),
            TextNode(", ", TextType.PLAIN_TEXT),
            TextNode("image_2", TextType.IMAGE, "link2"),
            TextNode(", ", TextType.PLAIN_TEXT),
            TextNode("image_3", TextType.IMAGE, "link3"),
            TextNode(".", TextType.PLAIN_TEXT)
        ])

    # split_nodes_links tests
    def test_split_links1(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    # text_to_textnodes tests
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev). That's it."
        text_nodes = text_to_textnodes(text)
        self.assertEqual(text_nodes, [
            TextNode("This is ", TextType.PLAIN_TEXT),
            TextNode("text", TextType.BOLD_TEXT),
            TextNode(" with an ", TextType.PLAIN_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word and a ", TextType.PLAIN_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" and an ", TextType.PLAIN_TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.PLAIN_TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(". That's it.", TextType.PLAIN_TEXT)
        ])

    

if __name__ == "__main__":
    unittest.main()