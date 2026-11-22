import shutil as shutil
from pathlib import Path

import read_write as rw
import gen_page as gen
import setup as setup
import process_emails as emails
import process_sensitivtext as ptext

pagekit_credit = "\n\n <!-- This Page is using JuliaPagekit by aocalux - https://github.com/aocalux/JuliaPagekit -->"
compat = False


def remove_old_build():
    Path("docs").mkdir(exist_ok=True)
    shutil.rmtree("docs/")
    print("[JuliaPagekit] removed old build in docs/")


def copy_statics():
    Path("content/static").mkdir(exist_ok=True)
    Path("content/_fileadmin").mkdir(exist_ok=True)
    shutil.copytree("content/static", "docs/static")
    print("[JuliaPagekit] copied static content from content/static to docs/static")
    shutil.copytree("content/_fileadmin", "docs/_fileadmin")
    print("[JuliaPagekit] copied static content from content/_fileadmin to docs/_fileadmin")


def txt_files(raw_pages):
    make_robotstxt(raw_pages)

    shutil.copy("templates/security.jtxt", "docs/security.txt")
    print("[JuliaPagekit] created security.txt")


def make_robotstxt(raw_pages):
    disallow_list = []
    for page in raw_pages:
        for folder in page.split("/"):
            if folder.startswith("_"):
                if folder.endswith(".jhtml"):
                    disallow_list.append(page)
                else:
                    disallow_list.append(page.split(folder)[0] + folder + "/")

    print(f"[JuliaPagekit] detected {disallow_list} to be added to robots.txt")
    with open("templates/robots.jtxt", "r") as robotsjtxt:
        content = ""
        for line in robotsjtxt:
            content = content + line

        disallow_file = ""
        for disallow in disallow_list:
            disallow_file += "Disallow: " + disallow + "\n"
        content = content.replace("{JuliaPagekit.auto-disallow}", disallow_file)

        with open("docs/robots.txt", "w") as robots:
            robots.write(content)
            print("[JuliaPagekit] created robots.txt")


def main():
    setup.init()
    print("[JuliaPagekit] JuliaPagekit by aocalux - https://github.com/aocalux/JuliaPagekit")
    print("[JuliaPagekit] Warning: JuliaPagekit is currently in experimental stages!")

    remove_old_build()
    global_template = rw.get_template("templates/global.template.jhtml")
    raw_pages = rw.get_raw_pages()
    copy_statics()
    txt_files(raw_pages)

    for page in raw_pages:
        page_assembelt = gen.make_page(page, global_template)
        masked_emails_page = emails.hide_plaintext_mail(page_assembelt)
        masked_text = ptext.hide_text(masked_emails_page)

        rw.make_folders(page)
        rw.write_page(page, masked_text)


if __name__ == "__main__":
    main()
