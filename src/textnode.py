from enum import Enum

class TextType(Enum):
    PLAIN_TEXT = "plain"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object) -> bool:#text_node_1, text_node_2
        # if text_node_1.text == text_node_2.text and text_node_1.text_type == text_node_2.text_type and text_node_1.url == text_node_2.url:
        #     return True
        # return False
        if not isinstance(other, TextNode):
            raise TypeError("Two objects should be and instances of TextNode class.")
            #return False
        
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"