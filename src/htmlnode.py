class HTMLNode():
    def __init__(self,tag = None, value = None,children = None,props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise Exception(NotImplementedError)
    def props_to_html(self):
        str = ""
        if self.props:
            for key in self.props.keys():
                str+= f' {key}="{self.props[key]}"'
        return str
    def __repr__(self):
        return (
            f"HTMLNode("
            f"{self.tag}"
            f"{', '+self.value if self.value is not None else ''}"
            f"{', '+ self.children if self.children is not None else ''}"
            f"{', '+ self.props if self.children is not None else ''})"
            )
class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):            
        super().__init__(tag, value, props = props)
    def to_html(self):
        if not self.value:
            raise ValueError("no value to create node")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag = None, value= None, children = None, props = None):
        super().__init__(tag, value, children, props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("no tag to create node")
        if self.children is None:
            raise ValueError("no children to create node")
        node_html = f"<{self.tag}{self.props_to_html()}>{self.value if self.value else ''}"
        if self.children:
            for child in self.children:
                node_html+=child.to_html()
        node_html+=f'</{self.tag}>'
        return node_html
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
