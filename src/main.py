import os
import shutil

from copystatic import copy_files_recursive
from md_converter import extract_title, markdown_to_html_node


dir_path_static = "./static"
dir_path_public = "public"
dir_path_content = "content"
template_path = "template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
   
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)

def get_filecontent(from_path):
    with open(from_path, "r") as f:
        file = f.read()
    return file

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = get_filecontent(from_path)
    template = get_filecontent(template_path)
    title = extract_title(markdown)
    markhtml = markdown_to_html_node(markdown).to_html()
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", markhtml)
    with open(dest_path, "w") as f:
        f.write(template)
    return

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    inhalt = os.listdir(dir_path_content)
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)
    for item in inhalt: 
        if os.path.isfile(dir_path_content + "/" + item):
            generate_page(dir_path_content + "/" + item, template_path, dest_dir_path + "/" + item.replace(".md", ".html"))
        else:
            generate_pages_recursive(dir_path_content +  "/" + item, template_path, dest_dir_path + "/" + item)
    return 

    

main()