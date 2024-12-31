from textnode import TextNode, TextType

def main():
    dummy_TN = TextNode("This is a dummy node", TextType.BOLD, "https://www.boot.dev")
    print(dummy_TN)

if __name__ == "__main__":
    main()