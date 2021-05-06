# Pair Generator

Takes a line-separated list of developers names and generates a pair. For example:

```
Bob
Tony
Olivia
Imogen
```
Running the script on the above would return two developers names in the following format:

```
Olivia & Imogen
```

## Prerequisites

A config.json file is required in the root folder of the project. This should contain the file to be read, the first line to read from and the last line to read from.

e.g.

```
{
  "inputFile": "/foo/bar/developerList",
  "firstLine": 6,
  "lastLine": 11
}
```

This means the pair generator will read the names between the 6th and 11th lines of the file provided.