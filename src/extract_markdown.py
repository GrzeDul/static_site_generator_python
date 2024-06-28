import re
def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    list = []
    for match in matches:
        list.append(match)
    return list

def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    list = []
    for match in matches:
        list.append(match)
    return list
text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
print(extract_markdown_links(text))
# [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]