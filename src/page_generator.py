import os
from markdown_to_html import markdown_to_html_node
from htmlnode import HTMLNode

def extract_title(markdown: str) -> str:
    blocks: list[str] = markdown.split("\n")
    for block in blocks:
        if block.startswith("# "):
            return block[2:]
    raise ValueError("No title found")

def generate_page(from_path: str, template_path: str, dest_path: str, base_path: str) -> None:

    if not os.path.exists(from_path):
        raise ValueError(f"source path doesn't exist")
    
    if not os.path.exists(template_path):
        raise ValueError(f"template path doesn't exist")

    if not "index.html" in os.listdir(dest_path):
        dest_path_html: str = os.path.join(dest_path, "index.html")

    with open(from_path, "r") as md_file:
        md_text: str = md_file.read()

    with open(template_path, "r") as html_file:
        html_text: str = html_file.read()

    html_node: HTMLNode = markdown_to_html_node(md_text)
    content: str = html_node.to_html()
    title: str = extract_title(md_text)

    html_page: str = html_text.replace("{{ Title }}", title).replace("{{ Content }}", content).replace('href="/', f'href="{base_path}').replace('src="/', f'src="{base_path}')

    with open(dest_path_html, "w") as index_html:
        index_html.write(html_page)
    

def generate_pages_recursive(content_path: str, template_path: str, dest_path: str, base_path: str) -> None:
    content_files: list[str] = os.listdir(content_path)
    for file in content_files:
        from_path = os.path.join(content_path, file)
        if os.path.isfile(from_path):
            generate_page(from_path, template_path, dest_path, base_path)
        else:
            new_dest_path = os.path.join(dest_path, file)
            os.mkdir(new_dest_path)
            generate_pages_recursive(from_path, template_path, new_dest_path, base_path)