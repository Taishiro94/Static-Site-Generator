from textnode import TextNode, TextType
from md_converter import markdown_to_html_node

def main():
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
    Node = markdown_to_html_node(md)
    print(Node)

main()