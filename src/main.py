from textnode import TextNode, TextType
from md_converter import text_to_textnodes

def main():
    Node = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
    print(Node)

main()