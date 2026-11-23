import os as os
from typing import Any


def make_robotstxt(raw_pages):
    disallow_list = []
    disallow_renderd(disallow_list, raw_pages)

    disallow_prerendered(disallow_list)

    print(f"[JuliaPagekit] detected {disallow_list} to be added to robots.txt")

    write_robotstxt(disallow_list)


def write_robotstxt(disallow_list: list[Any]):
    with open("templates/robots.jtxt", "r") as robotsjtxt:
        content = ""
        for line in robotsjtxt:
            content = content + line

        disallow_file = ""
        for disallow in disallow_list:
            disallow_file += "Disallow: " + disallow.replace(".jhtml", ".html") + "\n"
        content = content.replace("{JuliaPagekit.auto-disallow}", disallow_file)

        with open("docs/robots.txt", "w") as robots:
            robots.write(content)
            print("[JuliaPagekit] created robots.txt")


def disallow_prerendered(disallow_list: list[Any]):
    prepages = []
    for root, _, files in os.walk("content/_prerendered/"):
        for file in files:
            prepages.append(os.path.join(root.replace("content/_prerendered/", ""), file))

    for prepage in prepages:
        for folder in prepage.split("/"):
            if folder.startswith("_"):
                if folder.endswith(".html") or folder.endswith(".txt") or folder.endswith(".md") or folder.endswith(
                        ".php") or folder.endswith(".htm"):
                    disallow_list.append(prepage)
                else:
                    disallow_list.append(prepage.split(folder)[0] + folder + "/")


def disallow_renderd(disallow_list: list[Any], raw_pages):
    for page in raw_pages:
        for folder in page.split("/"):
            if folder.startswith("_"):
                if folder.endswith(".jhtml"):
                    disallow_list.append(page)
                else:
                    disallow_list.append(page.split(folder)[0] + folder + "/")
