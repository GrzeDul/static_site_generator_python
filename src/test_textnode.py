import unittest

from textnode import TextNode

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    split_nodes_delimiter,
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node2", text_type_text)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_italic, "https://www.boot.dev")
        node2 = TextNode(
            "This is a text node", text_type_italic, "https://www.boot.dev"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )
    def test_split_nodes_delimeter(self):
        node1 = TextNode("*This* is text with a *bold block1* word", text_type_text)
        node2 = TextNode("That *bold block2**", text_type_text)
        node3 = TextNode("*bold block3* here", text_type_text)
        node4 = TextNode("*bold block4*", text_type_text)
        node5 = TextNode("just text4*", text_type_text)
        node6 = TextNode("just text5", text_type_text)
        node7 = TextNode("just text6", text_type_text)
        new_nodes = split_nodes_delimiter([node1, node2, node3, node4,  node5, node6, node7], "*", text_type_bold)
        self.assertEqual(new_nodes, 
        [
        TextNode("This" , "bold", None),
        TextNode(" is text with a " , "text", None),
        TextNode("bold block1", "bold", None),
        TextNode(" wordThat ", "text", None),
        TextNode("bold block2","bold", None),
        TextNode("bold block3","bold", None),
        TextNode(" here", "text", None),
        TextNode("bold block4","bold", None),
        TextNode("just text4","text", None),
        TextNode("just text5just text6","text", None)]
        )
    def test_split_node_empty(self):
        node = TextNode("****text***", text_type_text)
        new_nodes = split_nodes_delimiter([node],"*",text_type_bold)
        self.assertEqual(new_nodes, [TextNode("text", "bold", None)])

if __name__ == "__main__":
    unittest.main()
