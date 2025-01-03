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
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value is None or self.value == "":
            raise ValueError
        elif self.tag is None or self.tag == "":
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def props_to_html(self):
        return super().props_to_html()


