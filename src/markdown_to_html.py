from htmlnode import HTMLNode
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_htlm_node
from parentnode import ParentNode
from leafnode import LeafNode

def clear_markdown_front_char(text: str) -> str:
    return " ".join(text.split(" ")[1:])

def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes: list[TextNode] = text_to_textnodes(text)
    children: list[LeafNode] = []
    for text_node in text_nodes:
        child = text_node_to_htlm_node(text_node)
        children.append(child)
    return children

def create_list_items(text: str) -> list[HTMLNode]:
    children: list[HTMLNode] = []
    list_items: list[str] = text.split("\n")
    for list_item in list_items:
        list_item = clear_markdown_front_char(list_item)
        children.append(ParentNode("li", text_to_children(list_item)))
    return children

def heading_to_html_node(heading: str) -> ParentNode:
    tag: str = ""
    if text.startswith("# "):
        tag = "h1"
    elif text.startswith("## "):
        tag = "h2"
    elif text.startswith("### "):
        tag = "h3"
    elif text.startswith("#### "):
        tag = "h4"
    elif text.startswith("##### "):
        tag = "h5"
    else:
        tag = "h6"
    text = clear_markdown_front_char(text)
    children: list[LeafNode] = text_to_children(text)
    return ParentNode(tag, children)

def code_to_html_node(text: str) -> ParentNode:
    tag:  str = "pre"
    text_node: TextNode = TextNode(text.replace("```", "").replace("\n", "", 1), TextType.CODE_TEXT)
    code_node: LeafNode = text_node_to_htlm_node(text_node)
    return ParentNode(tag, [code_node])

def quote_to_html_node(text: str) -> ParentNode:
    tag: str = "backquote"
    text = clear_markdown_front_char(text)
    children: list[LeafNode] = text_to_children(text)
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


def create_html_node(text: str) -> HTMLNode:
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


def markdown_to_html_node(markdown_text: str) -> HTMLNode:
    markdown_blocks: list[str] = markdown_to_blocks(markdown_text)
    children: list[HTMLNode] = []

    for markdown_block in markdown_blocks:
        node: HTMLNode = create_html_node(markdown_block)
        children.append(node)

    return ParentNode("div", children)
