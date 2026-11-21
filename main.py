# TODO: Clean up messy code!!!

import read_folder as read
import shutil as shutil
from pathlib import Path

compat = False

global_template = ""
raw_pages = ""


def tmp():
    global global_template
    Path("docs").mkdir(exist_ok=True)
    shutil.rmtree("docs/")

    for page in raw_pages:
        content = ["", "", "", ""]
        template_seption = ""
        template_seption_template = ""
        with open("content/" + page, "r") as file:
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
                        print(template_seption)
                        template_seption = "custom/" + template_seption
                        template_seption_template = read.get_template( "templates/" + template_seption)
                else:
                    content[3] += line


        if compat: global_template = global_template.replace("\n", "")

        page_assembelt = global_template.replace("{JuliaPagekit.page-title}", content[0]).replace("{JuliaPagekit.description}",
                                                                                                  content[1]).replace(
            "{JuliaPagekit.style}", content[2])

        if template_seption_template:
            if compat:
                template_seption_template = template_seption_template.replace("\n", "")
            content_new = ""
            for constom_template_string in read.get_template_conf(template_seption + ".jconf"):
                print(constom_template_string)
                for line in content[3].splitlines():
                    if line.startswith(f"__CustomTemplate-{constom_template_string.replace("{", "").replace("}", "")}: "):
                        template_seption_template = template_seption_template.replace(constom_template_string, line.replace(f"__CustomTemplate-{constom_template_string.replace("{", "").replace("}", "")}: ", ""))

            for line in content[3].splitlines():
                if not line.startswith("__CustomTemplate-"):
                    content_new +=  line + "\n"

            page_assembelt = page_assembelt.replace("{JuliaPagekit.body}", template_seption_template.replace("{JuliaPagekit.body}", content_new))
        else:
            page_assembelt = page_assembelt.replace("{JuliaPagekit.body}", content[3])

        for text_replacement in read.get_template_conf("text_snippets.placeholder.jconf"):
            replacement = text_replacement.split(" ")
            replacement_key = replacement[0]
            replacement[0] = ""
            replacement[1] = ""
            replacement_string = ""
            for string in replacement: replacement_string += " " + string

            page_assembelt = page_assembelt.replace(replacement_key, replacement_string)

        Path("docs", Path(page).parent).mkdir(
            parents=True,
            exist_ok=True
        )


        page_assembelt += "\n\n <!-- \n from file: " + page
        page_assembelt += "\n global_template: " + "templates/global.template.jhtml"
        if template_seption: page_assembelt += "\n custom_template: templates/" + template_seption + ", " + template_seption + ".jconf"
        page_assembelt += "\n -->"
        page_assembelt += "\n\n <!-- This Page is using JuliaPagekit by aocalux - https://github.com/aocalux/JuliaPagekit -->"

        with open("docs/" + page.replace(".jhtml", ".html"), "w") as index:
            index.write(page_assembelt)


def main():
    global global_template, raw_pages
    print("Hello World")

    global_template = read.get_template("templates/global.template.jhtml")
    raw_pages = read.get_raw_pages()
    tmp()
    print(raw_pages)


if __name__ == "__main__":
    main()
