from random import choice
import json
import os

filePath = os.path.dirname(__file__)

with open(f"{filePath}/config.json") as jsonConfig:
  config = json.load(jsonConfig)

with open(config.get("inputFile")) as gitTemplateFile:
  gitTemplate = gitTemplateFile.read()

firstLine = config.get("firstLine") - 1
lastLine = config.get("lastLine") - 1

lines = gitTemplate.split('\n')

names = lines[firstLine:lastLine]
name1 = choice(names)
names.remove(name1)
name2 = choice(names)

print(f"{name1} & {name2}")