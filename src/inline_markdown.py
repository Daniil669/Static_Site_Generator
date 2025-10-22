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

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT: #added
            new_nodes.append(node)
            continue
        text: str = node.text
        images: list[tuple] = extract_markdown_images(text)
        if not images:
            new_nodes.append(node) # fixed
            continue
        
        for i in range(len(images)):
            img_alt: str = images[i][0]
            img_link: str = images[i][1]

            sections: list[str] = text.split(f"![{img_alt}]({img_link})", 1)
            if len(sections) != 2: # added
                raise ValueError("Invalid Markdown syntex, formated section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(img_alt, TextType.IMAGE, img_link))
            text = sections[1] if len(sections) == 2 else ""
            # if i == len(images)-1 and text:
        if text:
            new_nodes.append(TextNode(text, TextType.PLAIN_TEXT))

    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        text: str = node.text
        links: list[tuple] = extract_markdown_links(text)
        if not links:
            new_nodes.append(node)
            continue
        
        for i in range(len(links)):
            link_text: str = links[i][0]
            link: str = links[i][1]

            sections: list[str] = text.split(f"[{link_text}]({link})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid Markdown syntex, formated section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, link))
            text = sections[1] if len(sections) == 2 else ""
        if text:
                new_nodes.append(TextNode(text, TextType.PLAIN_TEXT))

    return new_nodes

def extract_markdown_images(text: str) -> list[tuple]:
    return re.findall(r'!\[([^\[\]]*)\]\(([^\(\)]*)\)', text)

def extract_markdown_links(text: str) -> list[tuple]:
    return re.findall(r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)', text)

def text_to_textnodes(text: str) -> list[TextNode]:
    text_nodes: list[TextNode] = [TextNode(text, TextType.PLAIN_TEXT)]
    text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD_TEXT)
    text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC_TEXT)
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE_TEXT)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    return text_nodes