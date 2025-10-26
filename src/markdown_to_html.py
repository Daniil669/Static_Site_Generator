from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_htlm_node
from parentnode import ParentNode
from leafnode import LeafNode
from htmlnode import HTMLNode

def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes: list[TextNode] = text_to_textnodes(text)
    children: list[HTMLNode] = []
    for text_node in text_nodes:
        child = text_node_to_htlm_node(text_node)
        children.append(child)
    return children

def create_list_items(text: str) -> list[HTMLNode]:
    children: list[HTMLNode] = []
    list_items: list[str] = text.split("\n")
    for list_item in list_items:
        content = " ".join(list_item.split(" ")[1:])
        children.append(ParentNode("li", text_to_children(content)))
    return children

def heading_to_html_node(heading: str) -> ParentNode:
    hash_tag: int = 0
    for char in heading:
        if char == "#":
            hash_tag += 1
        if char == " ":
            break
    if hash_tag + 1 >= len(heading):
        raise ValueError(f"Invalid number of hashtag symbols")
    tag: str = f"h{hash_tag}"
    children: list[HTMLNode] = text_to_children(heading[hash_tag + 1:])
    return ParentNode(tag, children)

def code_to_html_node(text: str) -> ParentNode:
    if not text.startswith("```") or not text.endswith("```"):
        raise ValueError("Invalid code block")
    tag:  str = "pre"
    text_node: TextNode = TextNode(text[4:-3], TextType.PLAIN_TEXT)
    code_node: ParentNode = ParentNode("code", [text_node_to_htlm_node(text_node)])
    return ParentNode(tag, [code_node])

def quote_to_html_node(text: str) -> ParentNode:
    lines: list[str] = text.split("\n")
    quotes: list[str] = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        quotes.append(line.lstrip(">").strip())
    tag: str = "blockquote"
    content = " ".join(quotes)
    children: list[HTMLNode] = text_to_children(content)
    return ParentNode(tag, children)

def lists_to_html_node(text: str, list_type: str) -> ParentNode:
    tag: str = list_type
    children: list[HTMLNode] = create_list_items(text)
    return ParentNode(tag, children)

def paragraph_to_html_node(text: str) -> ParentNode:
    tag: str = "p"
    lines = text.split("\n")
    paragraph = " ".join(lines)
    children: list[HTMLNode] = text_to_children(paragraph)
    return ParentNode(tag, children)


def create_html_node(text: str) -> ParentNode:
    block_type: BlockType = block_to_block_type(text)
    match(block_type):
        case BlockType.HEADING:
            return heading_to_html_node(text)
        case BlockType.CODE:
            return code_to_html_node(text)
        case BlockType.QUOTE:
            return quote_to_html_node(text)
        case BlockType.UNORDERED_LIST:
            return lists_to_html_node(text, "ul")
        case BlockType.ORDERED_LIST:
            return lists_to_html_node(text, "ol")
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(text)


def markdown_to_html_node(markdown_text: str) -> ParentNode:
    markdown_blocks: list[str] = markdown_to_blocks(markdown_text)
    children: list[HTMLNode] = []

    for markdown_block in markdown_blocks:
        node: HTMLNode = create_html_node(markdown_block)
        children.append(node)

    return ParentNode("div", children)
