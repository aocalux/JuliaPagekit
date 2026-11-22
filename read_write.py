import os as os
from pathlib import Path


def get_raw_pages():
    folder_path = "content/"
    pages = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".jhtml"):
                pages.append(os.path.join(root.replace("content/", ""), file))

    return pages


def get_template(path):
    content = ""

    with open(path, "r") as file:
        for line in file:
            content += line

    return content


def get_template_conf(path):
    content = []

    with open("templates/" + path, "r") as file:
        for line in file:
            content.append(line.replace("\n", ""))

    return content


def make_folders(page: str):
    Path("docs", Path(page).parent).mkdir(
        parents=True,
        exist_ok=True
    )


def write_page(page: str, page_assembelt):
    with open("docs/" + page.replace(".jhtml", ".html"), "w") as index:
        index.write(page_assembelt)
