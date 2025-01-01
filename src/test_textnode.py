import unittest

from textnode import TextType, TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test node", TextType.BOLD)
        node2 = TextNode("This is a test node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_diff_url(self):
        node = TextNode("This is a test node", TextType.BOLD)
        node2 = TextNode("This is a test node", TextType.BOLD, "www.example.com")
        self.assertNotEqual(node, node2)

    def test_diff_text(self):
        node = TextNode("This is a test node", TextType.BOLD)
        node2 = TextNode("This is a different test node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_diff_texttype(self):
        node = TextNode("This is a test node", TextType.BOLD)
        node2 = TextNode("This is a test node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_none_url(self):
        node = TextNode("This is a test node", TextType.BOLD)
        self.assertEqual(node.url, None)

if __name__ == '__main__':
    unittest.main()