from textnode import TextNode, TextType

def main():
    Node = TextNode("This is some anchor text", TextType("link"), "https://www.boot.dev")
    print(Node)

main()