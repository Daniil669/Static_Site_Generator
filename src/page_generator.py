import os
from markdown_to_html import markdown_to_html_node
from htmlnode import HTMLNode

def extract_title(markdown: str) -> str:
    blocks: list[str] = markdown.split("\n")
    for block in blocks:
        if block.startswith("# "):
            return block[2:]
    raise ValueError("No title found")

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:

    if not os.path.exists(from_path):
        raise ValueError(f"source path doesn't exist")
    
    if not os.path.exists(template_path):
        raise ValueError(f"template path doesn't exist")
    
    if not os.path.exists(dest_path):
        print("Destination dir doesn't exist, creating it")
        os.mkdir(dest_path)
    
    ## change
    if not "index.md" in os.listdir(from_path):
        raise Exception(f"index.md not in the {from_path}")
    else:
        from_path = os.path.join(from_path, "index.md")
    ## 

    if not "template.html" in os.listdir(os.path.dirname(template_path)):
        raise Exception(f"template.html not in the root of the project")

    if not "index.html" in os.listdir(dest_path):
        dest_path_html: str = os.path.join(dest_path, "index.html")
    
    print(f"Generating page from {from_path} to {dest_path_html} using {template_path}")

    with open(from_path, "r") as md_file:
        md_text: str = md_file.read()

    with open(template_path, "r") as html_file:
        html_text: str = html_file.read()

    html_node: HTMLNode = markdown_to_html_node(md_text)
    content: str = html_node.to_html()
    title: str = extract_title(md_text)

    html_page: str = html_text.replace("{{ Title }}", title).replace("{{ Content }}", content)

    with open(dest_path_html, "w") as index_html:
        index_html.write(html_page)
    
