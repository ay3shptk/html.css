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
    render_invert = template_data.replace("/* PRIMARY */", flavor["tertiary"]).replace("/* SECONDARY */", flavor["secondary"]).replace("/* TERTIARY */", flavor["primary"])
    write("flavor/" + flavor["name"].lower() + ".min.css", render)
    write("flavour/" + flavor["name"].lower() + ".min.css", render)
    write("flavor/invert/" + flavor["name"].lower() + ".min.css", render_invert)
    write("flavour/invert/" + flavor["name"].lower() + ".min.css", render_invert)    
    readme += "### " + flavor["name"] + ":\n\n" + '```<link href="https://cdn.statically.io/gh/ayshptk/html.css/main/flavor/'+ flavor["name"].lower() + '.min.css" rel="stylesheet" >```\n\n'

readme += "### Bonus:\n You can easily switch the foreground and background colors with each other by adding `invert/` just before the name of the css file.\n\n<b>For Example:</b>\n\n```https://cdn.statically.io/gh/ayshptk/html.css/main/flavor/purple.min.css```\n\nwill become\n\n```https://cdn.statically.io/gh/ayshptk/html.css/main/flavor/invert/purple.min.css```"

write("README.md", readme)