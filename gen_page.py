from typing import Any

import read_write as rw
from main import compat, pagekit_credit


def make_page(page: str, global_template):
    content = ["", "", "", "", "", ""]
    template_seption = ""
    template_seption_template = ""
    with (open("content/" + page, "r") as file):
        for line in file:
            if line.startswith("_JuliaPagekit-Title: "):
                content[0] = line.replace("_JuliaPagekit-Title: ", "").replace("\n", "")
            elif line.startswith("_JuliaPagekit-Description: "):
                content[1] = line.replace("_JuliaPagekit-Description: ", "").replace("\n", "")
            elif line.startswith("_JuliaPagekit-Head: "):
                content[2] = line.replace("_JuliaPagekit-Head: ", "")
            elif line.startswith("_JuliaPagekit-Page-Template: "):
                template_seption = line.replace("_JuliaPagekit-Page-Template: ", "").replace("\n", "")
                if template_seption:
                    print("[JuliaPagekit] template in template for content/" + page + " with template " + template_seption)
                    template_seption = "custom/" + template_seption
                    template_seption_template = rw.get_template("templates/" + template_seption)
            elif line.startswith("_JuliaPagekit-PageID: "):
                content[4] = line.replace("_JuliaPagekit-PageID: ", "").replace("\n", "")
            elif line.startswith("_JuliaPagekit-modified: "):
                content[5] = line.replace("_JuliaPagekit-modified: ", "").replace("\n", "")
            else:
                content[3] += line

    if compat: global_template = global_template.replace("\n", "")

    page_assembelt = global_template.replace("{JuliaPagekit.page-title}", content[0]).replace(
        "{JuliaPagekit.description}",
        content[1]).replace(
        "{JuliaPagekit.style}", content[2]).replace("{JuliaPagekit.pageid}", content[4]).replace("{JuliaPagekit.modified}", content[5])

    if template_seption_template:
        page_assembelt = template_in_template(content, page_assembelt, template_seption, template_seption_template)
    else:
        page_assembelt = page_assembelt.replace("{JuliaPagekit.body}", content[3])

    for text_replacement in rw.get_template_conf("text_snippets.placeholder.jconf"):
        replacement = text_replacement.split(" ")
        replacement_key = replacement[0]
        replacement[0] = ""
        replacement[1] = ""
        replacement_string = ""
        for string in replacement: replacement_string += " " + string
        replacement_string = replacement_string.strip()

        page_assembelt = page_assembelt.replace(replacement_key, replacement_string)

    page_assembelt += "\n\n <!-- \n from file: " + page
    page_assembelt += "\n global_template: " + "templates/global.template.jhtml"
    if template_seption:
        page_assembelt += "\n custom_template: templates/" + template_seption + ", " + template_seption + ".jconf"
    page_assembelt += "\n -->"
    page_assembelt += pagekit_credit
    return page_assembelt


def template_in_template(content: list[str], page_assembelt, template_seption: str,
                         template_seption_template: str | Any) -> Any:
    if compat:
        template_seption_template = template_seption_template.replace("\n", "")
    content_new = ""
    for constom_template_string in rw.get_template_conf(template_seption + ".jconf"):
        for line in content[3].splitlines():
            if line.startswith(f"__CustomTemplate-{constom_template_string.replace("{", "").replace("}", "")}: "):
                template_seption_template = template_seption_template.replace(constom_template_string, line.replace(
                    f"__CustomTemplate-{constom_template_string.replace("{", "").replace("}", "")}: ", ""))

    for line in content[3].splitlines():
        if not line.startswith("__CustomTemplate-"):
            content_new += line + "\n"

    page_assembelt = page_assembelt.replace("{JuliaPagekit.body}",
                                            template_seption_template.replace("{JuliaPagekit.body}", content_new))
    return page_assembelt
