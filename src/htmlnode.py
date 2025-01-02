class HtmlNode:
    def __init__(self, tag: str=None, value: str=None, children: list=None, props: dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        prop = ""
        if self.props is None:
            return ""
        for k, v in self.props.items():
            if isinstance(v, str):
                prop += f" {k}=\"{v}\""
            else:
                prop += f" {k}={v}"
        return prop

    def __repr__(self):
        return f"HtmlNode(Tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"