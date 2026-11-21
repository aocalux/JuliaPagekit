import os as os

template = ""

def get_template():
    content = ""

    with open("template.jhtml", "r") as file:
        for line in file:
            content += line

    return content



def tmp():
    content = ""

    with open("content/index.jhtml", "r") as file:
        for line in file:
            content += line

    with open("docs/index.html", "w") as index:
        index.write(template.replace("{body}", content))



def main():
    global template
    print("Hello World")

    template = get_template()
    tmp()



if __name__ == "__main__":
    main()