import shutil as shutil
from pathlib import Path

import read_write as rw
import gen_page as gen

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
    txt_files()


def txt_files():
    shutil.copy("templates/security.jtxt", "docs/security.txt")
    print("[JuliaPagekit] created security.txt")
    shutil.copy("templates/robots.jtxt", "docs/robots.txt")
    print("[JuliaPagekit] created robots.txt")


def main():
    print("[JuliaPagekit] JuliaPagekit by aocalux - https://github.com/aocalux/JuliaPagekit")
    print("[JuliaPagekit] Warning: JuliaPagekit is currently in experimental stages!")

    remove_old_build()
    global_template = rw.get_template("templates/global.template.jhtml")
    raw_pages = rw.get_raw_pages()
    copy_statics()

    for page in raw_pages:
        page_assembelt = gen.make_page(page, global_template)

        rw.make_folders(page)
        rw.write_page(page, page_assembelt)


if __name__ == "__main__":
    main()
