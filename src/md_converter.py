import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        # If an "old node" is not a TextType.TEXT type, just add it to the new list as-is
            
        nodestring = node.text.split(delimiter)
        if len(nodestring) % 2 == 0:
            raise ValueError("invalid markdown syntax")
        i = 0
        splitnode = []
        for i in range(len(nodestring)):
            if nodestring[i] == "":
                continue
            if i % 2 == 0:
                splitnode.append(TextNode(nodestring[i], TextType.TEXT))
            else:
                splitnode.append(TextNode(nodestring[i], text_type))
        new_nodes.extend(splitnode)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
  