from pathlib import Path

root = ""
project_file = Path(root, ".is_JuliaPagekit_project")

index_jhtml = """_JuliaPagekit-Title: This is the Page Title
_JuliaPagekit-Description: This is The Page Discription
_JuliaPagekit-PageID: test1
_JuliaPagekit-Head: <link rel="stylesheet" href="CUSTOM STYLE FOR THIS PAGE LEVE BlANKT TO DISABLE">
_JuliaPagekit-Page-Template: test.template.jhtml

__CustomTemplate-test: hi
__CustomTemplate-test2: hi
__CustomTemplate-abcs: www.aocalux.com

<p>Test</p>
defefef
a
{snippet}
<br>
{JuliaPagekit.email={email}} <br>
{JuliaPagekit.email=info@example.com} <br>
{JuliaPagekit.email=info@beispiel.de} <br>
{JuliaPagekit.email=info2@example.com} <br>
<b>Das is {JuliaPagekit.ptext=sehr sehr geheimer Text} der ohne JS nicht vollständig ist</b> <br> <br>

Magic: {&ZeroWidthSpace;JuliaPagekit.email=info2@example.com&ZeroWidthSpace;} => {JuliaPagekit.email=info2@example.com}<br>
"""

global_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{snippet} {JuliaPagekit.page-title}</title>
    <meta name="description" content="{JuliaPagekit.description}">
    {JuliaPagekit.style}
</head>
<body>
    <a href="index2.html" id="test1">1</a>
    <a href="index2.html" id="test2">2</a>
    <a href="index2.html" id="test3">3</a>
    {JuliaPagekit.body}
    <script>
        document.getElementById("{JuliaPagekit.pageid}").style["color"] = "red";
    </script>
</body>
</html>"""

robots_template = """# This robots.txt file controls crawling of URLs under example.com.

# Block the Internet Archive / Wayback Machine crawlers
User-agent: ia_archiver
Disallow: /

User-agent: archive.org_bot
Disallow: /

User-agent: *
Disallow: /_fileadmin/
Disallow: /static/
Disallow: /.well-known
Disallow: /security.txt
{JuliaPagekit.auto-disallow}"""

sec_template = """Contact: mailto:admin@example.com
Expires: 2026-12-31T23:00:00.000Z
Preferred-Languages: en, de"""

snip_template = """{domain} = example.com
{snippet} = <b>Replace With Text</b>"""

test_template = """<h1> {test} </h1>
<h2> {test2} </h2>
{snippet}
{JuliaPagekit.body}
<h2> {test2} </h2>
<a href="https://{abcs}">{abcs}</a>"""

test_templateconf = """{test}
{test2}
{abcs}"""

def init():
    if project_file.exists():
        return
    else:
        make_project(input("Name for your project: "))
        exit(0)


def make_project(project_name):
    Path(root, "docs/").mkdir(
        parents=True,
        exist_ok=True
    )
    Path(root, "templates/custom/").mkdir(
        parents=True,
        exist_ok=True
    )
    Path(root, "content/static/").mkdir(
        parents=True,
        exist_ok=True
    )
    Path(root, "content/_fileadmin/").mkdir(
        parents=True,
        exist_ok=True
    )
    Path(root, "content/_prerendered/").mkdir(
        parents=True,
        exist_ok=True
    )

    with open(Path(root, "content/index.jhtml"), "w") as index:
        index.write(index_jhtml)

    with open(Path(root, "templates/global.template.jhtml"), "w") as gloabal:
        gloabal.write(global_template)

    with open(Path(root, "templates/robots.jtxt"), "w") as robots:
        robots.write(robots_template)

    with open(Path(root, "templates/security.jtxt"), "w") as sec:
        sec.write(sec_template)

    with open(Path(root, "templates/text_snippets.placeholder.jconf"), "w") as snip:
        snip.write(snip_template)

    with open(Path(root, "templates/custom/test.template.jhtml"), "w") as test:
        test.write(test_template)

    with open(Path(root, "templates/custom/test.template.jhtml.jconf"), "w") as testconf:
        testconf.write(test_templateconf)

    with open(project_file, "w") as pj_file:
        pj_file.write(f"JuliaPagekit Project - {project_name} \n JuliaPagekit by aocalux - https://github.com/aocalux/JuliaPagekit")
        print(f"[JuliaPagekit] project {project_name} created")