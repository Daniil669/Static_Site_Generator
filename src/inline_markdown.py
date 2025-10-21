from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:

    if delimiter == "" or delimiter == " ":
        raise ValueError('Delimiter cannot be empty string "" or contain space " "')
    
    
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        
        text_types = node.text.split(delimiter)
        if len(text_types) % 2 == 0:
            raise ValueError("Invalid Markdown syntex, formated section not closed")
        
        for i in range(len(text_types)):
            ts = text_types[i]
            if ts == "":
                continue
            if i%2==1:
                new_nodes.append(TextNode(ts, text_type))
                continue
            new_nodes.append(TextNode(ts, TextType.PLAIN_TEXT))
        
    return new_nodes

def split_nodes_images(old_nodes: list) -> list:
    pass

def split_nodes_link(old_nodes: list) -> list:
    pass

def extract_markdown_images(text: str) -> list[tuple]:
    return re.findall(r'!\[([^\[\]]*)\]\(([^\(\)]*)\)', text)

def extract_markdown_links(text: str) -> list[tuple]:
    return re.findall(r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)', text)