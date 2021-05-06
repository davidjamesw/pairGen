from random import choice
import json

with open("config.json") as jsonConfig:
  config = json.load(jsonConfig)

with open(config.get("inputFile")) as gitTemplateFile:
  gitTemplate = gitTemplateFile.read()

firstLine = config.get("firstLine")
lastLine = config.get("lastLine")

lines = gitTemplate.split('\n')

names = lines[firstLine:lastLine]
name1 = choice(names)
names.remove(name1)
name2 = choice(names)

print(f"{name1} & {name2}")