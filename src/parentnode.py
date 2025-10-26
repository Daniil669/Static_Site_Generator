from htmlnode import HTMLNode
from __future__ import annotations

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str | None] | None = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("Parent node must have a tag.")
        if self.children is None:
            raise ValueError("Parent node must have a list of children.")
        parent_string = f"<{self.tag}>"
        for child in self.children:
            child_string = child.to_html()
            parent_string += child_string
        parent_string += f"</{self.tag}>"
        return parent_string

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"