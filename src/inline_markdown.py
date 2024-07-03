import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.finditer(pattern, text)
    return list(matches)


def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.finditer(pattern, text)
    return list(matches)

def split_nodes_image(old_nodes):
    for old_node in old_nodes:
        matches = extract_markdown_images(old_node.text)
        result = []
        last_end = 0
        for match in matches:
            start, end = match.span()
            if last_end != start:
                result.append(TextNode(old_node.text[last_end:start], text_type_text))
            result.append(TextNode(match.group(1), text_type_image, match.group(2)))
            last_end = end

        if last_end < len(old_node.text):
            result.append(TextNode(old_node.text[last_end:], text_type_text))
    return result

def split_nodes_link(old_nodes):
    for old_node in old_nodes:
        matches = extract_markdown_links(old_node.text)
        result = []
        last_end = 0
        for match in matches:
            start, end = match.span()
            if last_end != start:
                result.append(TextNode(old_node.text[last_end:start], text_type_text))
            result.append(TextNode(match.group(1), text_type_link, match.group(2)))
            last_end = end
        if last_end < len(old_node.text):
            result.append(TextNode(old_node.text[last_end:], text_type_text))
    return result
        