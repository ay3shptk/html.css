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

readme = "HTML.css\n## Make plain HTML pages beautiful with just one line of code \n\n ### How to use:\n\n Just add the one line of code corressponding to the flavor of choice in the ```<head>``` tag of your page. It's that simple 😌\n\n"

for flavor in flavors["flavors"]:
    render = template_data.replace("/* PRIMARY */", flavor["primary"]).replace("/* SECONDARY */", flavor["secondary"]).replace("/* TERTIARY */", flavor["tertiary"])
    write("flavor/" + flavor["name"].lower() + ".min.css", render)
    readme += "### " + flavor["name"] + ":\n\n" + '```<link href="https://cdn.statically.io/gh/ayshptk/html.css/main/flavor/'+ flavor["name"].lower() + '.min.css" rel="stylesheet" >```\n\n'

write("README.md", readme)