class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not Implemented yet")
    
    def props_to_html(self):
        propstring =""
        if not self.props or self.props =="":
            return ""
        for kvp in self.props:
            key = kvp
            val = self.props[kvp]
            propstring += f' {key}="{val}"'
        return propstring
    
    def __repr__(self):
       return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("No tag")
        if not self.children:
            raise ValueError("No Children")
        output = ""
        for child in self.children:
            output += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{output}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"



class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
