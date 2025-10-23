from enum import Enum
from htmlnode import HTMLNode
# import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks: list[str] = []
    for block in markdown.split("\n\n"):
        if block != "":
            blocks.append(block.strip())
    return blocks

# def is_ordered_list(text: str) -> bool:

#     numbers: list[str] = re.findall(r'^[1-9]\. ', text, re.MULTILINE)
#     if not numbers:
#         return False
#     for i in range(len(numbers)):
#         # print(f"i: {i}, i+1: {i+1}, numbers[i][0]: {numbers[i][0]}")
#         if i+1 != int(numbers[i][0]):
#             return False
#     return True

def block_to_block_type(markdown_text: str) -> BlockType:
    # if re.search(r'^#{1-6} ', markdown_text):
    #     return BlockType.HEADING
    # if re.search(r'```.*```', markdown_text, re.DOTALL):
    #     return BlockType.CODE
    # if re.search(r'^>', markdown_text, re.MULTILINE):
    #     return BlockType.QUOTE
    # if re.search(r'^- |^\*{1} ', markdown_text, re.MULTILINE):
    #     return BlockType.UNORDERED_LIST
    # if is_ordered_list(markdown_text):
    #     return BlockType.ORDERED_LIST
    # MAKE IT SIMPLER
    lines: list[str] = markdown_text.split("\n")
    if markdown_text.startswith(("#", "##", "###", "####", "#####", "######")):
        return BlockType.HEADING
    if markdown_text.startswith("```") and markdown_text.endswith("```"):
        return BlockType.CODE
    if markdown_text.startswith("> "):
        for line in lines:
            if not line.startswith("> "):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if markdown_text.startswith(("- ", "* ")):
        for line in lines:
            if not line.startswith(("- ", "* ")):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if markdown_text.startswith("1. "):
        for i in range(len(lines)):
            if not lines[i].startswith(f"{i+1}. "):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown_text: str) -> HTMLNode:
    pass