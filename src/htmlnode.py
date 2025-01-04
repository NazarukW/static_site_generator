class HtmlNode:
    def __init__(self, tag: str=None, value: str=None, children: list=None, props: dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""
        prop = ""
        for k, v in self.props.items():
            if isinstance(v, str):
                prop += f" {k}=\"{v}\""
            else:
                prop += f" {k}={v}"
        return prop

    def __repr__(self):
        return f"HtmlNode(Tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"

class LeafNode(HtmlNode):
    def __init__(self, tag: str, value: str, props: dict=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None or self.value == "":
            raise ValueError("Invalid HTML: no value")
        if self.tag is None or self.tag == "":
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HtmlNode):
    def __init__(self, tag: str, children: list, props: dict=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None or self.tag == "":
            raise ValueError("Invalid HTML: no tag")
        if self.children is None or self.children == []:
            raise ValueError("Invalid HTML: no children")
        node = f"<{self.tag}{self.props_to_html()}>"
        for item in self.children:
            node += f"{item.to_html()}"
        node += f"</{self.tag}>"
        return node