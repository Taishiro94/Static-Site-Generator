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