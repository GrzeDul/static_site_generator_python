import os
from markdown_blocks import markdown_to_html_node

title_placeholder = "{{ Title }}"
content_placeholder = "{{ Content }}"
page_file_name = "index.html"
md_filename = "index.md"

def extract_title(md):
    lines = md.split('\n')
    for line in lines:
        if line.startswith('#'):
            return line[1:].strip()
    raise Exception('No title in file')

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    template = ''
    with open(template_path) as template_file:
        template = template_file.read()
    pages_md = os.listdir(dir_path_content)
    for page_md in pages_md:
        if not os.path.isfile(os.path.join(dir_path_content,page_md)):
            generate_pages_recursive(os.path.join(dir_path_content,page_md), template_path, os.path.join(dest_dir_path,page_md))
        else:
            md = ''
            with open(os.path.join(dir_path_content, md_filename)) as md_file:
                md = md_file.read()
            parent_node = markdown_to_html_node(md)
            html = parent_node.to_html()
            title = extract_title(md)
            page_html = template.replace(title_placeholder, title)
            page_html = page_html.replace(content_placeholder, html)
            os.makedirs(dest_dir_path, exist_ok=True)
            destination = os.path.join(dest_dir_path, page_file_name)
            with open(destination, 'w') as final_page:
                final_page.write(page_html)