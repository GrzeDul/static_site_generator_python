import unittest
from htmlnode import (HTMLNode, LeafNode, ParentNode)
class TestHTMLNode(unittest.TestCase):
    def test_props_html(self):
        node= HTMLNode("a", "text abcd", props = {
        "src": "google.com",
        "name": "link"
        })
        self.assertEqual(node.props_to_html(), ' src="google.com" name="link"')
    def test_props_html_none(self):
        node= HTMLNode("a", "text abcd",)
        self.assertEqual(node.props_to_html(), '')
    def test_repr(self):
        node= HTMLNode("a", "text abcd",)
        self.assertEqual(str(node),"HTMLNode(a, text abcd)")
    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    def test_leaf_to_html(self):
        node= LeafNode("a", "text abcd", props = {
        "src": "google.com",
        "name": "link"
        })
        self.assertEqual(node.to_html(),'<a src="google.com" name="link">text abcd</a>')
    def test_parent_to_html(self):
        node= ParentNode(
        "a",
        "text abcd",
        [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        ], 
        {
        "src": "google.com",
        "name": "link"
        }
        )
        self.assertEqual(node.to_html(), '<a src="google.com" name="link">text abcd<b>Bold text</b>Normal text<i>italic text</i>Normal text</a>')
    def test_parent_with_grandchildren(self):
        node = ParentNode("div",  children = 
        [
        ParentNode("p", children = 
        [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        ]
        ),
        ParentNode("p", children = 
        [
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        ], props = {"name": "text"}),
        ParentNode("div", children =
        [
        LeafNode(None, "Normal text")    
        ])
        ]
        )
        self.assertEqual(node.to_html(), '<div><p><b>Bold text</b>Normal text</p><p name="text"><i>italic text</i>Normal text</p><div>Normal text</div></div>')
if __name__ == "__main__":
    unittest.main()
