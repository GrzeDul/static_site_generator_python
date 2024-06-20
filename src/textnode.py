from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text,text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(value = text_node.text)
    elif text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, props = {"href":text_node.url})
    elif text_node.text_type == text_type_image:
        return LeafNode("img",value="", props = {"src":text_node.src, "alt":text_node.value})
    else:
        raise ValueError(f"invalid text_type: {text_node.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    old_nodes_text = ""
    for node in old_nodes:
        old_nodes_text += node.text
    new_nodes_text = old_nodes_text.split(delimiter)
    print(new_nodes_text)
    new_nodes = []
    bold = False
    for node in new_nodes_text:
        if node == '':
            bold = True
            continue
        if bold and node != new_nodes_text[-1]:
            new_node = TextNode( text = node, text_type = text_type)
            new_nodes.append(new_node)
            bold = False
        else:
            new_node = TextNode(text = node,text_type = text_type_text)
            new_nodes.append(new_node)
            bold = True
    return new_nodes

node1 = TextNode("This is text with a *bold block1* word", text_type_text)
node2 = TextNode("That *bold block2**", text_type_text)
node3 = TextNode("*bold block3* was", text_type_text)
node4 = TextNode("*bold block4*", text_type_text)
node5 = TextNode("just text4*", text_type_text)
node6 = TextNode("just text5", text_type_text)
node7 = TextNode("just text6", text_type_text)
new_nodes = split_nodes_delimiter([node1, node2, node3, node4,  node5, node6, node7], "*", text_type_bold)
print(new_nodes)