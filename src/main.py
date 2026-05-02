from textnode import TextNode, TextType
from md_converter import extract_markdown_links

def main():
    Node = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
    print(Node)

main()