import pandas, json
from os import path

x = pandas.read_excel("data/links.xlsx")

courses = path.join(path.dirname(path.realpath(__file__)), "courses.json")
with open(courses) as f:
    coursecodes = json.loads(f.read())

pptmimeList = ["application/vnd.ms-powerpoint","application/vnd.openxmlformats-officedocument.presentationml.presentation"]

outfile = open("data/links.json","w")

data = []

for i in range(len(x.index)):
    
    id = x.loc[i]["id"]
    name = x.loc[i]["name"]
    mime = x.loc[i]["mimeType"]
    tag = json.loads(x.loc[i]["tags"].replace("'",'"'))

    newEntry = [id, name, mime, tag]
    newtag = []

    typicalAncestors = []
    for c in coursecodes:
        for t in tag:
            if c in t:
                typicalAncestors.append(t)
                if "course:" + c not in newtag:
                    newtag.append("course:" + c)

    for t in tag:
        tl = t.lower()
        if "reference book" in tl:
            newtag.append("kind:book")
            typicalAncestors.append(t)
            break
        elif "note" in tl:
            newtag.append("kind:notes")
            typicalAncestors.append(t)
            break
        elif "ppt" in tl:
            newtag.append("kind:lecture-ppt")
            typicalAncestors.append(t)
            break
    
    if mime in pptmimeList and "kind:lecture-ppt" not in newtag:
        newtag.append("kind:lecture-ppt")
    
    for t in tag:
        if t not in typicalAncestors and t:
            newtag.append("other:"+t)

    newEntry[-1] = newtag
    data.append(newEntry)

outfile.write(json.dumps(data))
outfile.close()
