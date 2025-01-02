import unittest
from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html_one_props(self):
        props = {"href": "http://example.com"}
        html = HtmlNode(props=props)
        supposed = " href=\"http://example.com\""
        self.assertEqual(supposed, html.props_to_html())

    def test_props_to_html_tree_props(self):
        props = {"src": "image.jpg", "width": 100, "height": 200}
        html = HtmlNode(props=props)
        supposed = " src=\"image.jpg\" width=100 height=200"
        self.assertEqual(supposed, html.props_to_html())

    def test_repr_all_none(self):
        html = HtmlNode()
        supposed = f"HtmlNode(Tag: None, value: None, children: None, props: None)"
        self.assertEqual(supposed, str(html))
