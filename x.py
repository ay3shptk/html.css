import json

raw = open("flavors.json")
flavors = json.load(raw)
raw.close()

template = open("raw-data/template-min")
template_data = template.read()
template.close()


def write(name, content):
    temporary = open(name, "w")
    temporary.write(content)
    temporary.close()

readme = "# How to use:\n\n Just add the one line of code corressponding to the flavor of choice in the ```<head>``` tag of your page. It's that simple 😌\n\n"

for flavor in flavors["flavors"]:
    render = template_data.replace("/* PRIMARY */", flavor["primary"]).replace("/* SECONDARY */", flavor["secondary"]).replace("/* TERTIARY */", flavor["tertiary"])
    write("flavors/" + flavor["name"].lower() + ".min.css", render)
    readme += "### " + flavor["name"] + ":\n\n" + '```<link href="https://cdn.statically.io/gh/ayshptk/html.css/main/flavors/'+ flavor["name"].lower() + '.min.css" rel="stylesheet" >```\n\n'

write("README.md", readme)