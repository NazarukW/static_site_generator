import unittest
from htmlnode import HtmlNode, LeafNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html_None(self):
        node = HtmlNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_one_props(self):
        props = {"href": "http://example.com"}
        html = HtmlNode(props=props)
        expected = " href=\"http://example.com\""
        self.assertEqual(expected, html.props_to_html())

    def test_props_to_html_tree_props(self):
        props = {"src": "image.jpg", "width": 100, "height": 200}
        html = HtmlNode(props=props)
        expected = " src=\"image.jpg\" width=100 height=200"
        self.assertEqual(expected, html.props_to_html())

    def test_repr_all_none(self):
        html = HtmlNode()
        expected = f"HtmlNode(Tag: None, value: None, children: None, props: None)"
        self.assertEqual(expected, str(html))

class TestLeafNode(unittest.TestCase):
    def test_props_to_html_tag_value(self):
        leaf = LeafNode("p", "example value")
        expected = "<p>example value</p>"
        self.assertEqual(expected, leaf.to_html())

    def test_repr_all_tag_value_tag_props(self):
        leaf = LeafNode("a", "example value", props={"href": "http://example.com"})
        expected = "<a href=\"http://example.com\">example value</a>"
        self.assertEqual(expected, leaf.to_html())

    def test_repr_all_tag_value_tree_props(self):
        tag="p"
        value = "example value"
        props = {"src": "image.jpg", "width": 100, "height": 200}
        leaf = LeafNode(tag, value, props=props)
        expected = "<p src=\"image.jpg\" width=100 height=200>example value</p>"
        self.assertEqual(expected, leaf.to_html())
