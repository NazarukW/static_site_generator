import unittest
from htmlnode import HtmlNode, LeafNode, ParentNode
from textnode import TextType, TextNode, text_node_to_html_node

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
    def test_to_html_tag_value(self):
        leaf = LeafNode("p", "example value")
        expected = "<p>example value</p>"
        self.assertEqual(expected, leaf.to_html())

    def test_tohtml_tag_value_props(self):
        leaf = LeafNode("a", "example value", props={"href": "http://example.com"})
        expected = "<a href=\"http://example.com\">example value</a>"
        self.assertEqual(expected, leaf.to_html())

    def test_to_html_tag_value_tree_props(self):
        tag="p"
        value = "example value"
        props = {"src": "image.jpg", "width": 100, "height": 200}
        leaf = LeafNode(tag, value, props=props)
        expected = "<p src=\"image.jpg\" width=100 height=200>example value</p>"
        self.assertEqual(expected, leaf.to_html())

    def test_to_html_ValueError(self):
        leaf = LeafNode("p", "")
        with self.assertRaises(ValueError):
            leaf.to_html()

class TestParentNode(unittest.TestCase):
    def test_to_html_tag_ValueError(self):
        parent = ParentNode("", [LeafNode("p", "example value")])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_to_html_children_ValueError(self):
        parent = ParentNode("p", [])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_to_html_tag_value_one_children(self):
        tag = "p"
        children = [LeafNode("h1", "example value1")]
        parent = ParentNode(tag, children)
        expected = "<p><h1>example value1</h1></p>"
        self.assertEqual(expected, parent.to_html())

    def test_to_html_tag_value_one_children_no_tag(self):
        tag = "p"
        children = [LeafNode("", "example value1")]
        parent = ParentNode(tag, children)
        expected = "<p>example value1</p>"
        self.assertEqual(expected, parent.to_html())

    def test_to_html_tag_value_two_children(self):
        tag = "p"
        children = [LeafNode("h1", "example value1"),
                    LeafNode("h2", "example value2")]
        parent = ParentNode(tag, children)
        expected = "<p><h1>example value1</h1><h2>example value2</h2></p>"
        self.assertEqual(expected, parent.to_html())

    def test_to_html_tag_value_prop_one_children(self):
        tag = "p"
        children = [LeafNode("h1", "example value1")]
        props = {"src": "image.jpg", "width": 100, "height": 200}
        parent = ParentNode(tag, children, props=props)
        expected = "<p src=\"image.jpg\" width=100 height=200><h1>example value1</h1></p>"
        self.assertEqual(expected, parent.to_html())

    def test_to_html_tag_value_one_children_with_prop(self):
        tag = "p"
        children = [LeafNode("a", "example value1", props={"href": "http://example.com"}),]
        parent = ParentNode(tag, children)
        expected = "<p><a href=\"http://example.com\">example value1</a></p>"
        self.assertEqual(expected, parent.to_html())

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_type(self):
        text_node = TextNode("Example Text", TextType.TEXT)
        node = text_node_to_html_node(text_node)
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, "Example Text")
